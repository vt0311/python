'''
Created on 2017. 10. 24.

@author: acorn
'''
import wx

class Evt4Pan:
    def evt4PanFunc(self):
        wx.MessageBox('pan click !!!')

'''
def evt4PanFunc2(self, event):
    wx.MessageBox('pan click 222 !!!')
'''

if __name__ == "__main__":
    app = wx.App()
    frm = wx.Frame(None, title='panel test')
    frm.SetBackgroundColour('violet')
    
    pan = wx.Panel(frm)
    pan.SetBackgroundColour('red')

    evtObj = Evt4Pan()
    pan.Bind(wx.EVT_LEFT_DOWN, evtObj.evt4PanFunc)
    btn = wx.Button(pan, label='hi')
    
    
    #btn.SetPosition(50,50)
    frm.Show(show=True)
    app.MainLoop()
