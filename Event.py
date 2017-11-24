import wx
import wx.lib.newevent

EvtPlayerPlay  , EVT_PLAYER_PLAY    = wx.lib.newevent.NewEvent()
EvtPlayerPass  , EVT_PLAYER_PASS    = wx.lib.newevent.NewEvent()
EvtPlayerGiveUp, EVT_PLAYER_GIVEUP  = wx.lib.newevent.NewEvent()