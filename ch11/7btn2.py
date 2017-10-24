'''
Created on 2017. 10. 24.

@author: acorn
'''
import wx

class EvtHandler7:
    def evt7Func(self, ev):
        print(ev.GetEventObject().id)
        print(ev.GetEventObject().GetName())

class Gui7:
    def makeGui(self):
        frm = wx.Frame(None, title='btn test')
        btn = wx.Button(frm, label='haha')
        btn.id = 'btn1'
        btn.SetName('+')
        evObject = EvtHandler7()
        
        btn.Bind(wx.EVT_LEFT_DOWN, evObject.evt7Func)
        frm.Show(show=True)

if __name__ == '__main__' :
    app = wx.App()
    gui = Gui7()
    gui.makeGui()
    app.MainLoop()
    
