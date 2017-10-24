'''
Created on 2017. 10. 24.

@author: acorn
'''

import wx

class EvtHandler8:
    def calcFunc(self, evt):
        print(evt.GetButton().GetLabel())

class Gui8:
    def makeGui(self):
        frm = wx.Frame(None, title='textfield test')
        frm.SetSize(400,100)
        
        pan = wx.Panel(frm)
        
        text = wx.TextCtrl(pan)
        text.SetPosition((5,5))
        text.SetSize(360, 20)
        
        btn1 = wx.Button(pan, label='1')
        btn1.SetPosition((5,30))
        
        btn3 = wx.Button(pan, label='+')
        btn3.SetPosition((95,30))
        
        btn2 = wx.Button(pan, label='2')
        btn2.SetPosition((185,30))
        
        btn4 = wx.Button(pan, label='=')
        btn4.SetPosition((275,30))
        
        evtObj = EvtHandler8()
        
        btn1.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn2.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn3.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn4.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
          
        
        frm.Show(show=True)
    
    
    
if __name__ == '__main__':
    app = wx.App()
    gui = Gui8()
    gui.makeGui()
    app.MainLoop()
    
    
    