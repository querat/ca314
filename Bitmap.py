import wx

# Hack needed since wxPython does not propagate mouse click events correctly
class Bitmap(wx.StaticBitmap):

    def __init__(self, parent ,*args):
        wx.StaticBitmap.__init__(self, parent, *args)
        self.parent = parent
        self.Bind(wx.EVT_LEFT_DOWN, self.onBitmapClicked)


    def onBitmapClicked(self, evt):
        #self.parent.onBoardClicked(evt)
        wx.PostEvent(self.parent, evt)