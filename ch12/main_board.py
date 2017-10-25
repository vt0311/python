'''
Created on 2017. 10. 25.

@author: hsw
checked
'''

import wx
from ch12.boardList import BoardList
from ch12.gui_write import BoardWrite
from ch12.evt_frm import FrameChangeEvt

if __name__ == '__main__':
    app = wx.App()
    
    bListObj = BoardList()
    bListObj.makeGui()
    
    bWriteObj = BoardWrite()
    bWriteObj.makeGui()
    
    frmEvt = FrameChangeEvt(bListObj.lfrm, bWriteObj.wfrm)
    bListObj.lbtn2.Bind(wx.EVT_LEFT_DOWN, frmEvt.frameChgEvt)
    bWriteObj.wbtn1.Bind(wx.EVT_LEFT_DOWN,frmEvt.frameChgEvt)
    #frm = wx.Frame(None, title='Board List')
    
    #pan = wx.Panel(frm)   
        
    app.MainLoop()