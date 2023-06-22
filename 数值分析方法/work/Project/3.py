# -*- coding: utf-8 -*-
"""
http://blog.csdn.net/chenghit
"""
import wx
class MainWindow(wx.Frame):
    """We simply derive a new class of Frame."""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (200, 100))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.Show(True)

app = wx.App(False)
frame = MainWindow(None, 'Small editor')
app.MainLoop()