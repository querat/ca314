import wx

class Display(wx.Frame):

    TITLE       = "Game of Go"
    HEIGHT      = 480
    WIDTH       = 768

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, Display.TITLE, size=(Display.WIDTH, Display.HEIGHT))
        self.Show()
# !class Display


if __name__ == "__main__":
    app = wx.App()
    display = Display()
    app.MainLoop()