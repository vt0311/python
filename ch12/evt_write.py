'''
Created on 2017. 10. 25.

@author: hsw
'''

import wx
from ch12 import board_dao

class BoardWriteEvt:

    evTTxt = None
    evWTxt = None
    evCTxt = None
    
    def __init__(self, inTTxt, inWTxt, inCTxt):
        self.evTTxt = inTTxt
        self.evWTxt = inWTxt
        self.evCTxt = inCTxt
        
    def bWEvt(self, ev):
        cmd = ev.GetEventObject().GetName()
        board_dao.boardListInsert(self.evTTxt.GetValue(), self.evWTxt.GetValue(), self.evCTxt.GetValue())
        
    
    
    