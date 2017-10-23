'''
Created on 2017. 10. 23.

@author: acorn
'''
import wx


class EvtM:
    frm = None
    def __init__(self, f):
        self.frm = f
    def onMouseLeftDown(self, evt):
        self.frm.SetSize(200, 400)
    def onMouseRightDown(self, evt):
        self.frm.SetSize(400, 200)


app = wx.App()
frame = wx.Frame(None, title='test')
evtObj = EvtM(frame)

frame.Bind(wx.EVT_LEFT_DOWN, evtObj.onMouseLeftDown)
frame.Bind(wx.EVT_RIGHT_DOWN, evtObj.onMouseRightDown)
frame.Show(show=True)             
             
app.MainLoop()     