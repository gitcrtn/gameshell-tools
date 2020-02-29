# -*- coding: utf-8 -*-

from myinit import init_path
init_path()

from assets.list_page import ListPage

import myvars


class ToolsPage(ListPage):

    MyPages = [
        ["Battery", "Battery"],
    ]

    basepath = myvars.basepath


# EOF
