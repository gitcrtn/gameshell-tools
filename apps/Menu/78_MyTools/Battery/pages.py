# -*- coding: utf-8 -*-

from battery_page import BatteryPage

import myvars


def InitBatteryPage(main_screen):
    myvars.BatteryPage = BatteryPage()
    myvars.BatteryPage._Screen = main_screen
    myvars.BatteryPage._Name = "Battery"
    myvars.BatteryPage.Init()


# EOF
