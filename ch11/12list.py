'''
Created on 2017. 10. 24.

@author: hsw
'''
import wx

class EvtHandler12:
    def evtList(self,ev):
        tmpInt = ev.GetEventObject().GetSelection()
        print(ev.GetEventObject().GetString(tmpInt))
        

if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None,title='list test')
    
    list1 = wx.ListBox(frm)
    list1.Append('hi')
    list1.Append('hello')
    list1.Append('good')
    
    evObj = EvtHandler12()
    list1.Bind(wx.EVT_LISTBOX, evObj.evtList)
    
    frm.Show(show=True)
    app.MainLoop()