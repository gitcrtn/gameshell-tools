# -*- coding: utf-8 -*-

import sys

def init_path():
    mylib = '/home/cpi/mylib'
    if mylib not in sys.path:
        sys.path.append(mylib)


# EOF
