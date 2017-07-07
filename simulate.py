from __future__ import print_function
from automate_lib.baseFunctions import *
from automate_lib.keyboard import *
from automate_lib.web import *

"""
Main Simulate Entry File

TODO: Integrating browser and windows app library.
"""


def start_menu():
    """
    Start Menu
    :return: 
    """
    app = Application().Connect(title=u'', class_name='Shell_TrayWnd')
    shelltraywnd = app.Shell_TrayWnd

    x, y = get_center_point(shelltraywnd.Rectangle())
    move_cursor(x, y)
    start = shelltraywnd.Start
    start.Click()


def office():
    """
    Word processing
    :return: 
    """
    handle = search_window()
    app = Application().Connect(handle=handle)
    opusapp = app.OpusApps
    nuiscrollbar = opusapp.Horizontalword
    x, y = get_center_point(nuiscrollbar.Rectangle())
    print(nuiscrollbar.Rectangle())
    move_click_cursor(x, y, 3)


def Desktop():
    """
    Desktop Processing    
    :return: 
    """
    app = Application().Connect(title=u'Program Manager', class_name='Progman')
    print(app)

if __name__ == '__main__':

    Desktop()