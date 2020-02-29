# -*- coding: utf-8 -*-

from myinit import init_path
init_path()

from UI.page import Page
from UI.constants import Width, Height
from UI.label  import Label
from UI.util_funcs import midRect
from UI.skin_manager import MySkinManager
from UI.keys_def import CurKeys

from utils.dbus_proxy.power import get_battery_percent


class BatteryPage(Page):

    _FootMsg = ["Nav","","Refresh","Back","Enter"]
    _Label = None

    def Init(self):
        self._CanvasHWND = self._Screen._CanvasHWND
        self._Width =  self._Screen._Width
        self._Height = self._Screen._Height

        self._Label = Label()
        self._Label.SetCanvasHWND(self._CanvasHWND)
        self._Label.Init('', MySkinManager.GiveFont('varela25'))

    def _update_percent(self):
        self._Label.SetText('%s %%' % get_battery_percent())
        rect = midRect(
            self._Width/2, self._Height/2,
            self._Label._Width, self._Label._Height,
            Width, Height)
        self._Label.NewCoord(rect.left, rect.top)

    def OnLoadCb(self):
        self._update_percent()

    def KeyDown(self, event):
        if event.key == CurKeys["Menu"] or event.key == CurKeys["B"]:
            self.ReturnToUpLevelPage()
            self._Screen.Draw()
            self._Screen.SwapAndShow()

        if event.key == CurKeys["Right"]:
            self._Screen.Draw()
            self._Screen.SwapAndShow()

        if event.key == CurKeys["Left"]:
            self._Screen.Draw()
            self._Screen.SwapAndShow()

        if event.key == CurKeys["X"]:
            self._update_percent()
            self._Screen.Draw()
            self._Screen.SwapAndShow()

    def Draw(self):
        self.ClearCanvas()
        self._Label.Draw()


# EOF
