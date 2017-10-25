'''
Created on 2017. 10. 25.

@author: hsw
'''

import wx

class EvtHandler13:
    def evtList(self, ev):
        tmpInt = ev.GetEventObject().GetSelection()
        print(ev.GetEventObject().GetString(tmpInt))
        
if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='Board List')
    
    pan = wx.Panel(frm)
    
    btn1 = wx.Button(pan, label='글쓰기')
    btn2 = wx.Button(pan, label='조회')
    
    blist = wx.ListBox(frm)
    blist.Append('hi')  
    
    evObj = EvtHandler13()
    blist.Bind(wx.EVT_LISTBOX, evObj.evtList)
    
    frm.Show(show=True)
    app.MainLoop()      

