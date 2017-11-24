import wx.lib.newevent

# Custom events used by the project
EvtPlayerPlay       , EVT_PLAYER_PLAY           = wx.lib.newevent.NewEvent()
EvtPlayerPass       , EVT_PLAYER_PASS           = wx.lib.newevent.NewEvent()
EvtPlayerGiveUp     , EVT_PLAYER_GIVEUP         = wx.lib.newevent.NewEvent()
EvtNewGameRequested , EVT_NEW_GAME_REQUESTED    = wx.lib.newevent.NewEvent()