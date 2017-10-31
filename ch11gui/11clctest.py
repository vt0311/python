'''
Created on 2017. 10. 24.

@author: hsw
'''
import wx

class EvtHandler11:
    
    tmpText = None
    firstNum = 0
    secondNum = 0
    resultNum = 0
    giho = 0
    
    def __init__(self, inText):
        
        self.tmpText = inText
        self.frmTf = inText
        
    def calcFunc(self, evt):
        print(evt.GetEventObject().GetId())
        
        cmd = evt.GetEventObject().GetId()
        
        inData = evt.GetId()
        
        print(inData)
        
        
        if cmd in ['+','-','*','/']:
           self.fNum = int(self.frmTf.GetValue())
           self.giho = cmd
           self.frmTf.SetValue('')
        elif cmd == '=':
           self.sNum = int(self.frmTf.GetValue())
        
        
            
        giho = self.giho
        #wx.MessageBox(str(giho),str(giho),str(giho))
        if inData == 30005: # =
           # if giho == 3001:
            if giho == 30001:
                self.secondNum = int(self.tmpText.GetValue())
                self.resultNum = self.firstNum + self.secondNum
                result = self.resultNum  
           # self.firstNum = int(self.resultNum.GetValue())
                self.tmpText.SetValue(str(self.resultNum))
         
        elif inData == 30006: # clc
            self.firstNum = int(self.tmpText.GetValue())
            self.tmpText.SetValue('')    
            
        elif inData == 30001: # +
            #self.secondNum = int(self.tmpText.GetValue())
            self.resultNum = self.firstNum + self.secondNum
            #self.tmpText.SetValue(str(self.resultNum))
            self.tmpText.SetValue('') 
            self.giho = inData
            
        elif inData == 30002: # -
            #self.secondNum = int(self.tmpText.GetValue())
            self.resultNum = self.firstNum - self.secondNum
            self.tmpText.SetValue('') 
            #self.giho.SetValue('-')
            self.giho = inData
            
        elif inData == 30003: # *
            #self.secondNum = int(self.tmpText.GetValue())
            self.resultNum = self.firstNum * self.secondNum
            self.tmpText.SetValue('')   
            #self.giho.SetValue('*')  
            self.giho = inData  
            
        elif inData == 30004:  # /
            #self.secondNum = int(self.tmpText.GetValue())
            self.resultNum = self.firstNum / self.secondNum
            self.tmpText.SetValue('')  
            #self.giho.SetValue('/')
            self.giho = inData   
               
        else :
            tmpStr = self.tmpText.GetValue()
            self.tmpText.SetValue(tmpStr+str(inData))
    
    '''
    def evt11Func(self, ev):
        print(ev.GetEventObject.id)
        print(ev.GetEventObject.GetName())
    '''
class Gui11:
    text = None
    def makeGui(self):
        frm = wx.Frame(None, title='btn test')
        frm.SetSize(400,200)
        
        pan = wx.Panel(frm)
        
        text = wx.TextCtrl(pan)
        text.SetPosition((5,5))
        text.SetSize(360, 20)
        
        #btn = wx.Button(frm, label1='haha')
      #  btn.id = 'btn1'
        
        btn1 = wx.Button(pan, label='1', id=1, name='1')
        btn1.SetPosition((5,30))
        
        btn2 = wx.Button(pan, label='2', id=2, name='2')
        btn2.SetPosition((95,30))
        
        btn3 = wx.Button(pan, label='3', id=3, name='3')
        btn3.SetPosition((185,30))
        
        btna = wx.Button(pan, label='+', id=30001, name='+')
        btna.SetPosition((275,30))
        
        
        btn4 = wx.Button(pan, label='4', id=4, name='4')
        btn4.SetPosition((5,60))
        
        btn5 = wx.Button(pan, label='5', id=5, name='5')
        btn5.SetPosition((95,60))
        
        btn6 = wx.Button(pan, label='6', id=6, name='6')
        btn6.SetPosition((185,60))
        
        btnb = wx.Button(pan, label='-', id=30002, name='-')
        btnb.SetPosition((275,60))
        
        
        btn7 = wx.Button(pan, label='7', id=7, name='7')
        btn7.SetPosition((5,90))
        
        btn8 = wx.Button(pan, label='8', id=8, name='8')
        btn8.SetPosition((95,90))
        
        btn9 = wx.Button(pan, label='9', id=9, name='9')
        btn9.SetPosition((185,90))
        
        btnc = wx.Button(pan, label='*', id=30003, name='*')
        btnc.SetPosition((275,90))
        
        btnf = wx.Button(pan, label='clc', id=30006, name='clc')
        btnf.SetPosition((5,120))
        
        btn0 = wx.Button(pan, label='0', id=30000, name='0')
        btn0.SetPosition((95,120))
        
        btnd = wx.Button(pan, label='=', id=30005, name='=')
        btnd.SetPosition((185,120))
        
        btne = wx.Button(pan, label='/', id=30004, name='/')
        btne.SetPosition((275,120))
        
        evtObj = EvtHandler11(text)
        
        btn1.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn2.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn3.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn4.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn5.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn6.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn7.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn8.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn9.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btn0.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btna.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btnb.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btnc.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        btnd.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        
        btne.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        
        btnf.Bind(wx.EVT_LEFT_DOWN, evtObj.calcFunc)
        
        
        frm.Show(show=True)
        
        
if __name__ == '__main__':

    app = wx.App()
    gui = Gui11()
    gui.makeGui()
    app.MainLoop()
    