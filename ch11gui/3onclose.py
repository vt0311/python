'''
Created on 2017. 10. 23.

@author: acorn
'''
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='onClose')
        self.Bind(wx.EVT_CLOSE, self.onClose)
    def onClose(self, event):
        if wx.MessageBox('close??', 'confirm', wx.YES_NO) != wx.YES:
          #  event.skip(False)
            pass
        else :
            self.Destroy()
        
if __name__ == "__main__":
    app = wx.App()
    frm = MyFrame()
    frm.Show(show=True)
    app.MainLoop()