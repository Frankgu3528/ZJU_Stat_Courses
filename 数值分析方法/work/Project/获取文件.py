import os 
import wx 

class MyPanel(wx.Panel): 

    def __init__(self, parent): 
     wx.Panel.__init__(self, parent) 

     self.my_text = wx.TextCtrl(self, style=wx.TE_MULTILINE) 
     btn = wx.Button(self, label='Open Text File') 
     btn.Bind(wx.EVT_BUTTON, self.onOpen) 

     sizer = wx.BoxSizer(wx.VERTICAL) 
     sizer.Add(self.my_text, 1, wx.ALL|wx.EXPAND) 
     sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5) 

     self.SetSizer(sizer) 

    def onOpen(self, event): 
     wildcard = "TXT files (*.txt)|*.txt" 
     dialog = wx.FileDialog(self, "Open Text Files", wildcard=wildcard, 
           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) 

     if dialog.ShowModal() == wx.ID_CANCEL: 
      return 

     path = dialog.GetPath() 

     if os.path.exists(path): 
      with open(path) as fobj: 
       for line in fobj: 
        self.my_text.WriteText(line) 


class MyFrame(wx.Frame): 

    def __init__(self): 
     wx.Frame.__init__(self, None, title='Text File Reader') 

     panel = MyPanel(self) 

     self.Show() 

if __name__ == '__main__': 
    app = wx.App(False) 
    frame = MyFrame() 
    app.MainLoop() 