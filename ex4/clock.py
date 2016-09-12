# -*- coding: utf-8 -*-
"""
A beep clock
-------------
: author: lihui
: website: withlihui.com
"""
import winsound
from time import sleep, localtime


def beep():
    if m == 59:
        winsound.Beep(1000, 500)  # one long beep
    elif m == 29:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep


if __name__ == "__main__":
    while True:
        now = localtime()
        m = now.tm_min
        s = now.tm_sec
        sleep(60 - s)  # refresh every minute.
        beep()
