'''
Created on 2017. 10. 24.

@author: acorn
'''
import wx

class EvtHandler13:
    evFrm = None
    def __init__(self, inFrm):
        self.evFrm = inFrm
    def evtMenu(self,ev):
        #print(ev.GetEventObject().GetLabel())
        #print(ev.GetEventObject().GetMenuItems())
        cmd = ev.GetId()
        if cmd == 4:
            self.evFrm.close()
    
if __name__=='__main__':
    
    app = wx.App()
    frm = wx.Frame(None, title='menu test')
    
 #   menubar = menu.Append(wx.ID_ANY, "새파일")
    mbar = wx.MenuBar()
    mnu = wx.Menu()
    
    #mitem1 = wx.MenuItem(mnu, text='Close')
    #mitem1 = mnu.Append('1', 'New')
    mitem1 = mnu.Append(0, 'New')  
    mitem2 = mnu.Append(1, 'Open')
    mitem3 = mnu.Append(2, 'Save')
    mitem4 = mnu.AppendSeparator()
    mitem5 = mnu.Append(4, 'Close')
    
    #mnu.Append(0, mitem1, 'Close', wx.ITEM_NORMAL)
    mbar.Append(mnu, 'file')
    
    #mitem1 = mnu.Append('1', 'New')
    
    '''
    mnu.Append(0, 'New')  
    mnu.Append(0, 'Open')
    mnu.Append(0, 'Save')
    '''
    mnu.AppendSeparator()
    
    clsitem = mnu.Append(0, 'Close')
    mbar.Append(mnu, 'File')      
   # mnu = wx.Menu('Save')
   # mnu = wx.Menu('close')
    
   # menubar.Append(mnu, 'File')
    frm.SetMenuBar(mbar)
    
    evObj = EvtHandler13()
    frm.Bind(wx.EVT_MENU, evObj.evtMenu, clsitem)
    
    frm.Show(show=True)
    app.MainLoop()
    
    
    