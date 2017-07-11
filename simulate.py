from __future__ import print_function
from automate_lib.baseFunctions import *
from automate_lib.keyboard import *
from automate_lib.web import *
from automate_lib.Taskbar import *
from automate_lib.Browser import *

"""
Main Simulate Entry File
"""


if __name__ == '__main__':
    # office.write_letters()
    # office.close_save_office()
    browser = Browse()
    browser.start()
    browser.login()
    browser.read_inbox()