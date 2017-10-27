'''
Created on 2017. 10. 25.

@author: hsw
checked
'''

import wx

class FrameChangeEvt:

    lfrm = None
    wfrm = None
    def __init__(self, inlfrm, inwfrm):
        self.lfrm = inlfrm
        self.wfrm = inwfrm
        
    def frameChgEvt(self, ev):
        cmd = ev.GetEventObject().GetName()
        if cmd == 'insert':
            self.lfrm.Show(False)
            self.lfrm.Show(True)
        elif cmd == 'list':
            self.wfrm.Show(False)
            self.lfrm.Show(True)  
            