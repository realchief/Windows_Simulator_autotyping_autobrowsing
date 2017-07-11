from __future__ import print_function
from automate_lib.baseFunctions import *
from automate_lib.keyboard import *
from automate_lib.web import *
from automate_lib.Taskbar import *
from automate_lib.Browser import *

"""
Main Simulate Entry File
"""


def senario_1():
    """
    - start office first and write something and save as docx file.
    - Open browser and read inbox, compose email.
    :return: 
    """
    office.start()
    office.write_letters()
    office.close_save_office()
    browser.start()
    browser.login()
    browser.read_inbox()
    browser.compose_mail()
    browser.logout()


def senario_2():
    """
    Start browser first and login with username and password, read trash, inbox, and compose email
    :return: 
    """
    browser.start()
    browser.login()
    browser.read_archive()
    browser.read_trash()
    browser.compose_mail()
    browser.logout()
    office.start()
    office.write_letters()
    office.close_save_office()

if __name__ == '__main__':
    senario_list = [senario_1, senario_2]
    random.choice(senario_list)()