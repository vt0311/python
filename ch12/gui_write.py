'''
Created on 2017. 10. 25.

@author: hsw
checked
'''

import wx
from ch12.evt_write import BoardWriteEvt

class BoardWrite:
    
    wfrm = None
    wbtn1 = None
    
    def makeGui(self):
        self.wfrm = wx.Frame(None, title='BoardWrite')
        wpan = wx.Panel(self.wfrm)
        
     #   wbtn1 = wx.Button(wpan, label='select(조회)', name='select')
     #   wbtn2 = wx.Button(wpan, label='insert(입력)', name='insert')
        
    #    wlistbox = wx.ListBox(wpan)

        
        wGrid = wx.GridSizer(rows=4, cols=2, hgap =5, vgap =5)
        
        wpan.SetSizer(wGrid)
        
        titleLabel = wx.StaticText(wpan, label="제목: ")
        writerLabel = wx.StaticText(wpan, label="작성자: ")
        contentsLabel = wx.StaticText(wpan, label="내용: ")
        
        titleTxt = wx.TextCtrl(wpan)
        writerTxt = wx.TextCtrl(wpan)
        contentsTxt = wx.TextCtrl(wpan)
        
        self.wbtn1 = wx.Button(wpan, label='List', name='List')
        wbtn2 = wx.Button(wpan, label='Write', name='Write')
        
        wGrid.Add(titleLabel,1,wx.EXPAND)
        wGrid.Add(titleTxt,1,wx.EXPAND)
        wGrid.Add(writerLabel,1,wx.EXPAND)
        wGrid.Add(writerTxt,1,wx.EXPAND)
        wGrid.Add(contentsLabel,1,wx.EXPAND)
        wGrid.Add(contentsTxt,1,wx.EXPAND)
        wGrid.Add(self.wbtn1,1,wx.EXPAND)
        wGrid.Add(wbtn2,1,wx.EXPAND)
         
        #self.wfrm.Show(show=True)
        
        '''
        wVtBox.Add(wbtn1, 0, wx.ALIGN_RIGHT)
        wVtBox.Add(llistbox, 1, wx.EXPAND)
        lVtBox.Add(lbtn2, 0, wx.ALIGN_RIGHT)
       
        lfrm.Show(show=True)
        
        
        boardlistev = BoardListEvt(llistbox)
        lbtn1.Bind(wx.EVT_LEFT_DOWN, boardlistev.boardListEvt)
        lbtn2.Bind(wx.EVT_LEFT_DOWN, boardlistev.boardListEvt)
          '''   
        wEvObj = BoardWriteEvt(titleTxt,writerTxt,contentsTxt)
        wbtn2.Bind(wx.EVT_LEFT_DOWN, wEvObj.bWEvt)   
