import sys
import os
import thread
import cPickle
import time
import re

from socket import inet_ntoa
from subprocess import Popen, PIPE

import dpkt

try:
  import pcap

except ImportError:
  print "Failed to import pcap library!"
  print "If you are using Debian/Ubuntu Linux, please:"
  print " root@whatever:~# apt-get install python-pypcap"
  sys.exit(1)


class TracertException(Exception):
  pass

def tracert(host):
  """
  Traceroute
  eg: l = tracert("8.8.8.8")

  Return value: a list of routers

  """
  p = Popen(["traceroute", "-n", "-q", "2", "-I", host], stdout=PIPE, stderr=PIPE)
  p.wait()
  (o, e) = p.communicate()
  if e != '':
    e = e.replace("\n", "")
    raise TracertException(e)

  t = []

  r = re.compile(r"((\d{1,3}\.){3}\d{1,3})") # this matches a ip address
  for i in o.split("\n")[1:-1]: # prompt at head and empty line at tail
    s = r.search(i)
    if s:
      t.append(s.group())
    else:
      t.append(None)

  del p
  return t


def thread_func(arg):
  "thread func, trace route and store in rmap"

  global rmap, rmap_lock, taskqueue, taskqueue_lock, ending_flag
  global threadcount, threadcount_lock, my_ip, tracked, tracked_lock
  try:
    threadcount_lock.acquire()
    threadcount = threadcount + 1
    threadcount_lock.release()

    while True:
      while not len(taskqueue):
        time.sleep(1)

        if ending_flag:
          threadcount_lock.acquire()
          threadcount = threadcount - 1
          threadcount_lock.release()
          #print "Thread %d is terminated." % thread.get_ident()
          thread.exit()

      if ending_flag:
        threadcount_lock.acquire()
        threadcount = threadcount - 1
        threadcount_lock.release()
        #print "Thread %d is terminated." % thread.get_ident()
        thread.exit()

      taskqueue_lock.acquire()
      if len(taskqueue):
        ip = taskqueue.pop(0)
      else:
        taskqueue_lock.release()
        continue
      taskqueue_lock.release()

      print "Thread %d got work to do: %s" % (thread.get_ident(), ip)

      route = tracert(ip)
      tracked_lock.acquire()
      for i in route:
        tracked[i] = 1 # None is ok, i think, so not filtering
      tracked_lock.release()


      print "%s: %s" % (ip, repr(route))

      f = my_ip
      h = 1
      rmap_lock.acquire()
      for t in route:
        if t == None:
          h = h + 1
          continue
        rmap[(f,t)] = h
        h = 1
        f = t

      if h != 1:
        rmap[(f,None)] = ip # missing

      rmap_lock.release()

  except Exception, e:
    import traceback
    threadcount_lock.acquire()
    threadcount = threadcount - 1
    threadcount_lock.release()
    print "Thread %d is *CRASHED*!" % (thread.get_ident(), )
    print traceback.format_exc()
    thread.exit()

def get_ifaddr(ifn):
  """get ip address of specified iface
     >>> get_ifaddr("wlan0")
     "113.121.xx.xx"
  """
  import struct, socket, fcntl
  s = socket.socket()
  return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack("256s", ifn[:15]))[20:24])

def main():
  global rmap, rmap_lock, taskqueue, taskqueue_lock, ending_flag
  global threadcount, threadcount_lock, tracked, tracked_lock, my_ip

  if len(sys.argv) < 2:
    print "Please specify a network interface!"
    sys.exit(1)


  if os.geteuid():
    print "This tool require root privilege to run!"
    sys.exit(1)

  if os.path.exists("routemap.dat"): # is there a saved router map?
    print "Loading saved route map..."
    f = open("routemap.dat", "rb")
    rmap, my_ip = cPickle.load(f)
    f.close()

  my_ip = get_ifaddr(sys.argv[1])

  # add my ip to tracked
  tracked[my_ip] = 1

  # start working threads
  for i in xrange(20):
    thread.start_new_thread(thread_func, (None,))

  # start packet capture
  try:
    p = pcap.pcap(sys.argv[1])

    for i in p:
      pkt = dpkt.ethernet.Ethernet(i[1])
      while not isinstance(pkt, str):
        pkt = pkt.data
        if isinstance(pkt, dpkt.ip.IP):
          src = inet_ntoa(pkt.src)
          dst = inet_ntoa(pkt.dst)
          #print "%s => %s" % (src, dst)
          if not tracked.get(src):
            tracked[src] = 1
            print "Task: %s" % src
            taskqueue_lock.acquire()
            taskqueue.append(src)
            taskqueue_lock.release()


          if not tracked.get(dst):
            tracked[dst] = 1
            print "Task: %s" % dst
            taskqueue_lock.acquire()
            taskqueue.append(dst)
            taskqueue_lock.release()

  except KeyboardInterrupt:
    intr = True
    if taskqueue_lock.locked():
      taskqueue_lock.release()

  if intr:
    print "Waiting for all thread to terminate..."
    try:
      ending_flag = True
      while threadcount:
        print threadcount
        time.sleep(1)
    except KeyboardInterrupt:
      print "OK, OK, I'll terminate immediatly..."
      sys.exit(1)


  # save the result
  print "Saving route map..."
  f = open("routemap.dat", "wb")
  cPickle.dump((rmap, my_ip), f, 2)
  f.close()
  print "Program terminated."
  sys.exit(0)


class DbgLock:
  def __init__(self, name):
    self.lock = thread.allocate_lock()
    self.name = name

  def acquire(self):
    self.lock.acquire()
    print ":: Thread %d Locking %s" % (thread.get_ident(), self.name)

  def release(self):
    print ":: Thread %d Releasing %s" % (thread.get_ident(), self.name)
    self.lock.release()

  def locked(self):
    return self.lock.locked()
# ----------------------------------------------------

rmap = {} # Router map, all things goes here. this should be saved.
#rmap_lock = thread.allocate_lock()
rmap_lock = DbgLock("rmap")

taskqueue = [] # task queue, ips going to be tracked
#taskqueue_lock = thread.allocate_lock()
taskqueue_lock = DbgLock("taskqueue")

tracked = {} # ips already tracerouted
#tracked_lock = thread.allocate_lock()
tracked_lock = DbgLock("tracked")

ending_flag = False # whether to end collecting...

threadcount = 0
#threadcount_lock = thread.allocate_lock()
threadcount_lock = DbgLock("threadcount")

my_ip = ""

if __name__ == "__main__":
  main()


