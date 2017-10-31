'''
Created on 2017. 10. 24.

@author: hsw
'''
import wx
#from wx.lib.agw.buttonpanel import BoxSizer

if __name__ == '__main__':
    
    app = wx.App()
    frm = wx.Frame(None, title ='box test')
    
    pan = wx.Panel(frm)
    
    btn1 = wx.Button(pan, label='11')
    btn2 = wx.Button(pan, label='22')
    
    pan2 = wx.Panel(pan)
    
    btn3 = wx.Button(pan2, label='33')
    btn4 = wx.Button(pan2, label='44')
    
    ''' '''''''''''''''''''''''''''''''''''''''' '''
    box2 = wx.BoxSizer(wx.HORIZONTAL)
    #box1 = wx.BoxSizer(wx.VERTICAL)
   
    #box2.Add(btn1, 0, wx.ALIGN_CENTER)
    #box2.Add(btn2, 0, wx.ALIGN_CENTER)
    
    pan2.SetSizer(box2)
    box2.Add(btn3)
    box2.Add(btn4 )
    
    #box1 = wx.BoxSizer(wx.HORIZONTAL)
    box1 = wx.BoxSizer(wx.VERTICAL)
    #box2.Add(btn3 )
    #box2.Add(btn4)
    
   # pan2.SetSizer(box2)
    
    #box1.Add(pan2, 0, wx.ALIGN_RIGHT|wx.TOP, 50)
    
    box1.Add(btn1, 0, wx.ALIGN_CENTER)
    box1.Add(btn2, 0, wx.ALIGN_CENTER)
    box1.Add(pan2)
    pan.SetSizer(box1)
    
   # frm.setSizer(box1)
    
   # btn1 = wx.Button(frm, label='b1')
   # btn2 = wx.Button(frm, label='b2')
    
    frm.Show(show=True)
    
    app.MainLoop()
    
    