

import wx


class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
        
    def InitUI(self):   
            
        pnl = wx.Panel(self)

        self.rb1 = wx.RadioButton(pnl, label='Value A', pos=(10, 10), 
            style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(pnl, label='Value B', pos=(10, 30))
        self.rb3 = wx.RadioButton(pnl, label='Value C', pos=(10, 50))
        
        self.rb1.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.rb2.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.rb3.Bind(wx.EVT_RADIOBUTTON, self.SetVal)

        # self.sb = self.CreateStatusBar(3)
        
        # self.sb.SetStatusText("True", 0)
        # self.sb.SetStatusText("False", 1)
        # self.sb.SetStatusText("False", 2)   

        self.SetSize((600, 510))
        self.SetTitle('wx.RadioButton')
        self.Centre()
        self.Show(True)     


        btn = wx.Button(pnl, label='Ok', pos=(90, 185), size=(60, -1))

        btn.Bind(wx.EVT_BUTTON, self.OnClose)

    def SetVal(self, e):
        
        state1 = str(self.rb1.GetValue())
        state2 = str(self.rb2.GetValue())
        state3 = str(self.rb3.GetValue())

        # self.sb.SetStatusText(state1, 0)
        # self.sb.SetStatusText(state2, 1)
        # self.sb.SetStatusText(state3, 2)            
    def OnClose(self, e):
        
        self.Close(True)    
                 
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == '__main__':
    main()   