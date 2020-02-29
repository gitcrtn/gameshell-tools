# -*- coding: utf-8 -*-

import pages
import myvars


def Init(main_screen):
    pages.InitSamplePage(main_screen)


def API(main_screen):
    if main_screen !=None:
        main_screen.PushCurPage()
        main_screen.SetCurPage(myvars.SamplePage)
        main_screen.Draw()
        main_screen.SwapAndShow()


# EOF
