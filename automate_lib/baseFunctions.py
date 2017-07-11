from __future__ import print_function

import pyautogui
import random
from pywinauto.application import Application
from pywinauto import handleprops, findwindows
import pywinauto
import time

screenWidth, screenHeight = pyautogui.size()
print('Width: {}, Height: {}'.format(screenWidth, screenHeight))

stop_timea = 0.1
stop_timeb = 2
app = Application()


def get_pos():
    """
    get current position of mouse
    :return: (x, y)
    """
    return pyautogui.position()


def get_win_size():
    """
    get current size of window
    :return: screenWidth, screenHeight
    """
    return pyautogui.size()


def get_center_point(client_rect):
    """
    get center point coordinate 
    :param left: 
    :param top: 
    :param right: 
    :param bottom: 
    :return: 
    """

    return client_rect.left + 10, client_rect.top + 10


def move_cursor_browser(coor_x, coor_y):
    """
    Move mouse to given coordinate.
    :param coor_x: 
    :param coor_y: 
    :return: 
    """

    if coor_x == 0 and coor_y == 0:
        return
    action_time = random.uniform(0.1, 0.7)
    pyautogui.moveTo(coor_x, coor_y, action_time)


def move_cursor(rectangle):
    """
    Move mouse to given coordinate.
    :param coor_x: 
    :param coor_y: 
    :return: 
    """
    coor_x, coor_y = get_center_point(rectangle)
    if coor_x == 0 and coor_y == 0:
        return
    action_time = random.uniform(0.1, 0.7)
    pyautogui.moveTo(coor_x, coor_y, action_time)


def move_click_cursor(rectangle, number=1):
    """
    Move mouse to given coordinate.
    :param coor_x: 
    :param coor_y: 
    :return: 
    """
    coor_x, coor_y = get_center_point(rectangle)
    if coor_x == 0 and coor_y == 0:
        return

    action_time = random.uniform(0.1, 0.7)
    pyautogui.moveTo(coor_x, coor_y, action_time)
    time.sleep(1)
    pyautogui.click(button='left', clicks=number)


def move_click_browser(coor_x, coor_y):
    """
    Move mouse to given coordinate.
    :param coor_x: 
    :param coor_y: 
    :return: 
    """

    action_time = random.uniform(0.1, 0.7)
    pyautogui.moveTo(coor_x, coor_y, action_time)
    time.sleep(1)
    pyautogui.click(button='left')


def click_mouse(type, coor_x=None, coor_y=None):
    """
    Click mouse event with left, right.
    :param type: 
    :param coor_x: 
    :param coor_y: 
    :return: 
    """

    if coor_y == coor_x == None:
        time.sleep(random.uniform(stop_timea, stop_timeb))
        pyautogui.click(button=type)
    else:
        time.sleep(random.uniform(stop_timea, stop_timeb))
        pyautogui.click(x=coor_x, y=coor_y, button=type)


def scroll_mouse(count, sensivity=200, pause=None):
    """
    if coor_x and coor_y is None, then scroll current position of cursor.
    :param amount_to_scroll: 
    :param coor_x: 
    :param coor_y: 
    :return: 
    """
    for i in range(count):
        try:
            # time.sleep(random.uniform(stop_timea, stop_timeb))
            print("scrolling")
            pyautogui.scroll(sensivity, pause=0.5)
            # time.sleep(1)

        except Exception as e:
            print("Scroll mouse Error: {}".format(e))


def random_move_cursor(num=10):
    """
    Random moving mouse cursor.
    :param num: 
    :return: 
    """
    count = 0
    while count < num:
        x = random.uniform(0, screenWidth)
        y = random.uniform(0, screenHeight)
        print(x, y)

        move_cursor(x, y)
        count += 1
        time.sleep(.5)


def search_window():
    """
    Find elements based on criteria passed in and return list of their handles
    :return: 
    """
    try:
        found_window = findwindows.find_window(active_only=True, enabled_only=True, visible_only=True)
        print('found_window: {}'.format(found_window))
        return found_window
    except pywinauto.findwindows.ElementAmbiguousError:
        print('There was more then one element that matched')
    except pywinauto.findwindows.ElementNotFoundError:
        print('No element could be found')
    except pywinauto.findwindows.WindowAmbiguousError:
        print('There was more then one window that matched')
    except pywinauto.findwindows.WindowNotFoundError:
        print('No window could be found')

    return []


def dumpwindow(handle):
    """
    Return detail information about the handle on windows.
    :param handle: 
    :return: 
    """
    return handleprops.dumpwindow(handle)


def HWND_client_rect(HWND):
    """
    Get Area Rectangle for Client.
    :param app: 
    :return: 
    """
    return HWND.client_area_rect()


def type_of_object(obj):
    """
    Return type of object
    :param obj: 
    :return: 
    """

    obj_type = type(obj)
    print(obj_type.__name__)
    return obj_type.__name__


def classnames_unique(list):
    """
    Return classnames
    :param list: 
    :return: 
    """
    classnames = {v['class_name']: v for v in list}.values()
    print(classnames)
    return classnames


def identifiers_unique(list):
    """
    Return unique identifiers
    :param list: 
    :return: 
    """
    identifiers = {v['hash_rect']: v for v in list}.values()
    print(identifiers)
    print(len(identifiers))
    return identifiers


def is_valid(rect):
    """
    Check valid rect    
    :param rect: 
    :return: 
    """
    if rect.left == 0 and rect.top == 0 and rect.right == 0 and rect.bottom == 0:
        return False
    return True


def sys_info():
    print('OS x64 is: {}'.format(pywinauto.sysinfo.is_x64_OS()))
    print("python x64 is: {}".format(pywinauto.sysinfo.is_x64_Python()))
    print("OS Arch: {}".format(pywinauto.sysinfo.os_arch()))
    print("Python : {} bit".format(pywinauto.sysinfo.python_bitness()))


if __name__ == '__main__':
    scroll_mouse(count=1)
