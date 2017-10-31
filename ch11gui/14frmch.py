'''
Created on 2017. 10. 24.

@author: hsw
'''
import wx

class evHandler14:
    evFrm1 = None
    evFrm2 = None
    
    def __init__(self, inFrm1, inFrm2):
        self.evFrm1 = inFrm1
        self.evFrm2 = inFrm2
    def btnEvFunc(self, ev):
        cmd = ev.GetEventObject().GetName()
        if cmd == '1':
            self.evFrm1.Show(False)
            self.evFrm2.Show(True)
        elif cmd =='2':
            self.evFrm2.Show(False)
            self.evFrm1.Show(True)

if __name__ == '__main__' :
    app = wx.App()
    
    frm1 = wx.Frame(None, title='11111')
    btn1 = wx.Button(frm1, label='11111', name='1')
    
    frm2 = wx.Frame(None, title='22222')
    btn2 = wx.Button(frm2, label='22222', name='2')
    
    evObj = evHandler14(frm1, frm2)
    btn1.Bind(wx.EVT_LEFT_DOWN, evObj.btnEvFunc)
    btn2.Bind(wx.EVT_LEFT_DOWN, evObj.btnEvFunc)
    
    
    frm1.Show(show=True)
    app.MainLoop()
    
    