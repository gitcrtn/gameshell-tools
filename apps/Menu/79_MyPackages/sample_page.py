# -*- coding: utf-8 -*-

import pygame

from UI.page import Page
from UI.keys_def import CurKeys


class SamplePage(Page):

    _FootMsg = ["Nav","","","Back","Enter"]

    def Init(self):
        self._CanvasHWND = self._Screen._CanvasHWND
        self._Width =  self._Screen._Width
        self._Height = self._Screen._Height

    def OnLoadCb(self):
        pass

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

    def Draw(self):
        self.ClearCanvas()


# EOF
