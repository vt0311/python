'''
Created on 2017. 10. 23.

@author: acorn
'''
import wx

class MyFrame(wx.Frame):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        wx.Frame.__init__(self, parent=None, title='hello')
    
app = wx.App()

frm = MyFrame()

frm.Show(show=True)

app.MainLoop()