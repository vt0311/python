'''
Created on 2017. 10. 25.

@author: acorn
'''

import wx
import cx_Oracle


conn = cx_Oracle.connect('scott/tiger@localhost:1521/xe')
cursor = conn.cursor()
cursor.execute('select * from board')
for row in cursor:
                print(row) 

class BoardListEvt:
    evList = None
    def __init__(self, fromFrmList):
        evList = fromFrmList
        
    def boardListEvt(self, ev):
        cmd = ev.GetEventObject().GetName()
        print(cmd)
        if cmd =='select':
            pass
        elif cmd == 'insert':
            pass

class BoardList:
    def makeGui(self):
        lfrm = wx.Frame(None, title='BoardList')
        lpan = wx.Panel(lfrm)
        lbtn1 = wx.Button(lpan, label='select(조회)', name='select')
        lbtn2 = wx.Button(lpan, label='insert(입력)', name='insert')
        
        llistbox = wx.ListBox(lpan)
        
       # for i in cursor.fetchall():
        #    llitbox.Append(i)
            
           
        
        lVtBox = wx.BoxSizer(wx.VERTICAL)
        
        lpan.SetSizer(lVtBox)
        
        lVtBox.Add(lbtn1, 0 ,wx.ALIGN_RIGHT)
        lVtBox.Add(llistbox, 1, wx.EXPAND)
        lVtBox.Add(lbtn2, 0 ,wx.ALIGN_RIGHT)
       
        lfrm.Show(show=True)
        
        
        boardlistev = BoardListEvt(llistbox)
        lbtn1.Bind(wx.EVT_LEFT_DOWN, boardlistev.boardListEvt)
        lbtn2.Bind(wx.EVT_LEFT_DOWN, boardlistev.boardListEvt)
    
if __name__ == '__main__':
    app = wx.App()
    
    boardlistObj = BoardList()
    boardlistObj.makeGui()
    
    
    frm = wx.Frame(None, title='Board List')
    
 
    
    pan = wx.Panel(frm)   
        
    app.MainLoop()



cursor.close()
conn.close()

