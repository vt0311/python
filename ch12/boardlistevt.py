'''
Created on 2017. 10. 25.

@author: hsw
checked
'''

import wx
from ch12 import board_dao 
#from ch12guiboard.board_dao import boardListSelect

class BoardListEvt:
    evListBox = None
    bWriteObj = None
    def __init__(self,fromFrmListBox):
        self.evListBox = fromFrmListBox
        #self.WriteObj = fromFrmWObj
        
    def boardListEvt(self, ev):
        cmd = ev.GetEventObject().GetName()
        print(cmd)
        if cmd =='select':
            #boardListDAO = BoardListDAO()
            tmpList = board_dao.boardListSelect()
            self.evListBox.Clear()
            for row in tmpList:
                tmpStr = str( row[0] )+ '  ' +str(  row[1])+ '  ' +str(  row[2]) + '  ' + str( row[4])
                self.evListBox.Append(tmpStr)
        '''          
        elif cmd == 'insert':
            #board_dao.boardListInsert(instr1, instr2, instr3, instr4 )
            self.bWriteObj = BoardWrite()
            self.bWriteObj.makeGui()
            #bWriteObj.Show(show=True)
            '''
                
'''       
class BoardListEvt:
    evListBox = None
    bWriteObj = None
    def __init__(self,fromFrmListBox):
        self.evListBox = fromFrmListBox
    def boardListEvt(self, ev):
        cmd = ev.GetEventObject().GetName()
        if cmd=='select':
            tmpList = board_dao.boardListSelect()
            self.evListBox.Clear()
            for row in tmpList:
                tmpStr=str(row[0])+'    '+row[1]+'    '+row[2]+'    '+str(row[4])
                self.evListBox.Append(tmpStr)
   ''' 