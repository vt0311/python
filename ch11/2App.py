'''
Created on 2017. 10. 23.

@author: acorn
'''
import wx

class MyApp(wx.App):
    '''
    classdocs
    '''

    def OnInit(self):
        '''
        Constructor
        '''
        frame=wx.Frame(None, title='hello')
        frame.Show(show=True)
        return True
    
if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()