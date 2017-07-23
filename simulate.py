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
        time.sleep(5)
        browser.start()
        browser.popular_sites()
        browser.login()
        browser.read_inbox()
        browser.read_sent()
        browser.compose_mail()
        browser.logout()
        browser.close_borwser()

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
        browser.read_inbox()
        browser.read_sent()
        browser.read_archive()
        browser.read_trash()
        browser.compose_mail()
        browser.logout()
        # browser.google_entry()
        browser.popular_sites()
        browser.close_borwser()
        time.sleep(5)
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
        # browser.google_entry()
        browser.read_inbox()
        browser.read_sent()
        browser.read_archive()
        browser.read_trash()
        browser.compose_mail()
        browser.logout()
        browser.popular_sites()
        browser.close_borwser()
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

    senario_count = 0
    taskbar.hidden_icons()
    taskbar.clock_time()
    for item in range(random.choice([3, 4, 5])):
        # senario_list = [senario_1, senario_2, senario_3, senario_4]
        # random.choice(senario_list)()
        if senario_count == 0:
            senario_2()
        elif senario_count == 1:
            senario_1()
        else:
            senario_4()
        senario_count += 1