#!/usr/bin/python

import sys
import cPickle
import yapgvb
import random

def main():

  def get_vertex_info(ip):
    if nodetree.get(ip): # is source ip node already exist?
      vv = nodetree[ip][0] # vertex
      vl = nodetree[ip][1] # child vertex list

    else:
      vv = g.add_node(ip)
      #vv.shape = "circle"
      vv.color = "blue"
      vl = []
      nodetree[ip] = (vv, vl)

    return (vv, vl)

  nodetree = {}

  filename = "routemap.dat"
  if len(sys.argv) < 2:
    print "Didn't specify filename, use 'routemap.dat'"
  else:
    filename = sys.argv[1]

  f = open(filename, "rb")
  rmap, my_ip = cPickle.load(f)
  f.close()

  g = yapgvb.Digraph("RouteMap")

  get_vertex_info(my_ip)[0].color = "green"

  for v, deg in rmap.items():

    vertex, vertexlist = get_vertex_info(v[0])
    dup = False
    for ip, data in vertexlist:
      if ip == v[1]: # this is a duplicate
        dup = True
        break

    if dup:
      continue

    if v[1] is not None: # is it a LOST trace?
      if deg > 1:
        for i in range(1, deg):
          vt = g.add_node("* %d" % random.randint(0,100000000))
          vt.color = "red"
          vertex >> vt
          vertex = vt

      vertex_t, vertex_tlist = get_vertex_info(v[1])
      if vertex == vertex_t:
        print v
      else:
        edge = vertex >> vertex_t
        vertexlist.append((v[1], edge))


    else:

      vertex_t = g.add_node("LOST(%s)" % deg)
      vertex_t.color = "red"
      if vertex == vertex_t:
        print v
      else:
        edge = vertex >> vertex_t

  g.layout(yapgvb.engines.dot)

  print "Rendering..."
  g.render("result.svg")

if __name__ == "__main__":
  main()