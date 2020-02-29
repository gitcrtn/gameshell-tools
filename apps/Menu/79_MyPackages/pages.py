# -*- coding: utf-8 -*-

from sample_page import SamplePage

import myvars


def InitSamplePage(main_screen):
    myvars.SamplePage = SamplePage()
    myvars.SamplePage._Screen = main_screen
    myvars.SamplePage._Name = "Sample"
    myvars.SamplePage.Init()


# EOF
