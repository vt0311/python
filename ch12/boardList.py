'''
Created on 2017. 10. 25.

@author: hsw
checked
'''

import wx
#from ch12 import 
from ch12.boardlistevt import BoardListEvt



class BoardList:
    lfrm = None
    lbtn2 = None
    def makeGui(self):
        self.lfrm = wx.Frame(None, title='BoardList')
        lpan = wx.Panel(self.lfrm)
        lbtn1 = wx.Button(lpan, label='select(조회)', name='select')
        self.lbtn2 = wx.Button(lpan, label='insert(입력)', name='insert')
        
        llistbox = wx.ListBox(lpan)
        
        # for i in cursor.fetchall():
        #    llitbox.Append(i)
        
        lVtBox = wx.BoxSizer(wx.VERTICAL)
        
        lpan.SetSizer(lVtBox)
        
        lVtBox.Add(lbtn1, 0, wx.ALIGN_RIGHT)
        lVtBox.Add(llistbox, 1, wx.EXPAND)
        lVtBox.Add(self.lbtn2, 0, wx.ALIGN_RIGHT)
       
        self.lfrm.Show(show=True)
        
        #bWriteObj = BoardWrite()
        
        boardlistev = BoardListEvt(llistbox)
        lbtn1.Bind(wx.EVT_LEFT_DOWN, boardlistev.boardListEvt)
        #self.lbtn2.Bind(wx.EVT_LEFT_DOWN, boardlistev.boardListEvt)
'''    
if __name__ == '__main__':
    app = wx.App()
    
    boardlistObj = BoardList()
    boardlistObj.makeGui()
 
        
    app.MainLoop()
'''

