import wx

import local_info
import map


#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):

        mp = map.Map(local_info.get_local_ip())
        mp_message = mp.get_csv_match().get_csv_title()[mp.get_column_num()]
        mp_message = mp_message.decode('utf-8')
        mp_message = mp_message.encode('gbk')

        self.log = log
        wx.Panel.__init__(self, parent, -1)

        box = wx.StaticBox(self, -1, "This is a wx.StaticBox")
        bsizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        t = wx.StaticText(self, -1, "Controls placed \"inside\" the box are really its siblings %s" % mp_message)
        bsizer.Add(t, 0, wx.TOP|wx.LEFT, 10)


        border = wx.BoxSizer()
        border.Add(bsizer, 1, wx.EXPAND|wx.ALL, 25)
        self.SetSizer(border)
        

#----------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win

#----------------------------------------------------------------------



overview = """<html><body>
<h2><center>wx.StaticBox</center></h2>

This control draws a box and can be used to group other controls.

</body></html>
"""



if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])

