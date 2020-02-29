# -*- coding: utf-8 -*-

from tools_page import ToolsPage

import myvars


def InitToolsPage(main_screen):
    myvars.ToolsPage = ToolsPage()
    myvars.ToolsPage._Screen = main_screen
    myvars.ToolsPage._Name = "MyTools"
    myvars.ToolsPage.Init()


# EOF
