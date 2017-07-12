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
    try:
        office.start()
        office.write_letters()
        office.close_save_office()
    except Exception as e:
        print('Exception: {}'.format(e))
    try:
        browser.start()
        browser.login()
        browser.read_inbox()
        browser.compose_mail()
        browser.logout()
    except Exception as e:
        print(' Browser Exception: {}'.format(e))


def senario_2():
    """
    Start browser first and login with username and password, read trash, inbox, and compose email
    :return: 
    """
    try:
        browser.start()
        browser.login()
        browser.read_archive()
        browser.read_trash()
        browser.compose_mail()
        browser.logout()
        browser.google_entry()
    except Exception as e:
        print('Exception: {}'.format(e))

    try:
        office.start()
        office.write_letters()
        office.close_save_office()
    except Exception as e:
        print("Exception: {}".format(e))


def senario_3():
    """
    simulate with only browser
    :return: 
    """
    try:
        browser.start()
        browser.login()
        browser.read_archive()
        browser.read_trash()
        browser.compose_mail()
        browser.logout()
        browser.google_entry()
    except Exception as e:
        print('Exception: {}'.format(e))


def senario_4():
    """
    simulate with only office.
    :return: 
    """
    try:
        office.start()
        office.write_letters()
        office.close_save_office()
    except Exception as e:
        print("Exception: {}".format(e))


if __name__ == '__main__':
    # time.sleep(3)
    print(dumpwindow(handle=search_window())['classname'])
    if dumpwindow(handle=search_window())['classname'] == 'ConsoleWindowClass':
        app.connect(handle=search_window())
        consolewindowclass = app.ConsoleWindowClass
        consolewindowclass.Minimize()

    senario_list = [senario_1, senario_2, senario_3, senario_4]
    random.choice(senario_list)()