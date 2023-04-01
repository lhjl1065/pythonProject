# /usr/bin/env python
# coding: utf-8
import sys
from time import sleep

import pyautogui as pg
import pytweening


def my_click():
    l_pos, r_pos = pg.position()
    pg.dragTo(l_pos + 1, r_pos + 1, duration=0.5, button='left')
    sleep(0.1)


def main():
    # get current position
    print
    'Place your mouse in the starting position within then seconds.'
    sleep(10)

    try:
        my_click()
        times = 1
        while 1:
            my_click()
            my_click()
            sleep(2.5)
            my_click()
            print
            "click %03d" % times
            times += 1
    except pg.FailSafeException as e:
        print
        "Error: %s" % e
        print
        "Over"
    except Exception as e:
        print
        "Error: %s" % e
        print
        "Over"


if __name__ == "__main__":
    main()