'''
Created on 2017. 10. 24.

@author: hsw
'''

import wx

if __name__ == '__main__':
    app = wx.App()
    frm = wx.Frame(None, title='grid test')
    
    pan = wx.Panel(frm)
    grid = wx.GridSizer(rows=2, cols=2, hgap =5, vgap =5)
    pan.SetSizer(grid)
    
    btn1 = wx.Button(pan,label='1')
    btn2 = wx.Button(pan,label='2')
    btn3 = wx.Button(pan,label='3')
    btn4 = wx.Button(pan,label='4')
    
    grid.Add(btn1, 0, wx.EXPAND)
    grid.Add(btn2, 0, wx.EXPAND)
    grid.Add(btn3, 0, wx.EXPAND)
    grid.Add(btn4, 0, wx.EXPAND)
    
       
    frm.Show(show=True)
       
    #app = wx.App()    
    app.MainLoop()
       
    
