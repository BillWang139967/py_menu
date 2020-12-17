#!/usr/bin/python
# coding=utf8
"""
# Author: meetbill
# Created Time : 2017-03-16 21:36:04

# File Name: three_page.py
# Description:

"""
import os
import sys
root_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.insert(0, os.path.join(root_path, 'w_lib'))
from pysnack.snack_lib import Mask
from pysnack.snack_lib import conformwindows
from pysnack.snack_lib import Snack_output
import logging


def three1_1funtion(screen, *args, **kargs):
    window_name = "name" in kargs.keys() and kargs["name"] or "test_windows1_1"
    m = Mask(screen, window_name, 35)
    m.text("label_test0", "ceshi_text")
    m.entry("label_test1", "entry_test1", "0")
    m.entry("label_test2", "entry_test2", "0")
    m.entry("label_test3", "entry_test3", "127.0.0.1")
    m.checks("复选框", "checks_list", [
        ('checks_name1', 'checks1', 0),
        ('checks_name2', 'checks2', 0),
        ('checks_name3', 'checks3', 0),
        ('checks_name4', 'checks4', 1),
        ('checks_name5', 'checks5', 0),
        ('checks_name6', 'checks6', 0),
        ('checks_name7', 'checks7', 0),
    ],
        height=5
    )
    m.radios("单选框", "radios", [
        ('radios_name1', 'radios1', 0),
        ('radios_name2', 'radios2', 1),
        ('radios_name3', 'radios3', 0)])

    m.buttons(yes="Sava&Quit", no="Quit")
    (cmd, results) = m.run(43, 3)

    logging.info(str(cmd) + " " + str(results))
    if cmd == "yes":
        rx = conformwindows(screen, "确认操作")
        if rx[0] == "yes" or rx[1] == "F12":
            """exe"""
            return
        else:
            logging.info("cancel this operation")
            return
    else:
        return


def three1_2funtion(screen, *args, **kargs):
    m = Snack_output(screen, "test_windows1_2", 35)
    m.text("ceshijjjjjjjjjjjxdffffffffffffffff")
    m.text("xxxfffxxxxxxxxxxxxxx")
    m.text("xxxxxxxxxxxxxxxxx")
    m.text("xxxxxxxxxxxxxxxxx")
    m.text("xxxxxxxxxxxxxxxxx")
    m.run(43, 3)


if __name__ == "__main__":
    from snack import *
    try:
        screen = SnackScreen()
        screen.setColor("ROOT", "white", "blue")
        screen.setColor("ENTRY", "white", "blue")
        screen.setColor("LABEL", "black", "white")
        screen.setColor("HELPLINE", "white", "blue")
        screen.setColor("TEXTBOX", "black", "yellow")
        three1_2funtion(screen)
    except Exception as e:
        print e
    finally:
        screen.finish()
