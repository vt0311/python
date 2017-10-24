'''
Created on 2017. 10. 24.

@author: acorn
'''
import wx

class Evt4Button:
    def evt4BtnFunc(self, event):
        wx.MessageBox('btn click !!!')

class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='btn frm')
        pan = wx.Panel(self)
        btn = wx.Button(pan, label='hi btn')
        btn.SetPosition((100,20))
        
        evtObj = Evt4Button()
        btn.Bind(wx.EVT_LEFT_DOWN, evtObj.evt4BtnFunc)
        
        
if __name__ == '__main__':
    app = wx.App()
    frm = ButtonFrame()
    frm.Show(show=True)
    app.MainLoop()

