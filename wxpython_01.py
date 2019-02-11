import wx

class my_frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300, 200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

app = wx.App(False)
frame = my_frame(None, "Small_edior")
app.MainLoop()