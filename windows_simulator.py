from __future__ import print_function
from pyautogui import typewrite
from automate_lib.baseFunctions import *
from automate_lib.keyboard import *
from automate_lib.web import *
import threading

"""
Test File.
"""

app = Application()

current_windows = []


def action_write(text="testdialogwrapper\n"):
    scroll_mouse(count=random.choice(scroll_count))
    typewrite(text)


def parse_objects(objects):
    """
    Parse objects from Application
    :param objects: 
    :return: 
    """
    print("Length of objects: {}".format(len(objects)))

    for object in objects:
        try:
            if type_of_object(object) == "DialogWrapper":
                #
                # if not is_valid(object.ClientAreaRect()):
                #     continue
                if object.is_active():
                    print("object Area Rect: {}".format(object.rectangle()))
                    print("object has_keyboard_focus(): {}".format(object.is_active()))
                    # x, y = get_center_point(object.client_rect())
                    # typewrite('test')
                    x, y = get_center_point(object.client_rect())
                    move_cursor(x, y)
                    time.sleep(1)


            elif type_of_object(object) == "EditWrapper":
                print("object Area Rect: {}".format(object.client_rect()))
                print("object has_keyboard_focus(): {}".format(object.is_active()))
                # move_cursor(object.client_rect().right, object.client_rect().bottom)

            elif type_of_object(object) == "ToolTipsWrapper":
                print("object Area Rect: {}".format(object.client_rect()))
                print("object has_keyboard_focus(): {}".format(object.is_active()))

            elif type_of_object(object) == "HwndWrapper":
                print("object Area Rect: {}".format(object.client_rect()))
                print("object has_keyboard_focus(): {}".format(object.is_active()))

            elif type_of_object(object) == "TreeViewWrapper":
                print("object Area Rect: {}".format(object.client_rect()))
                print("object has_keyboard_focus(): {}".format(object.is_active()))
                # if object.has_keyboard_focus():

        except controls.hwndwrapper.ControlNotEnabled:
            print("Raised when a control is not enabled")

        except controls.hwndwrapper.ControlNotVisible:
            print("Raised when a control is not visible")


def parse_specification(specification):
    pass
    if specification.exists():
        print("Control exists")
        object = specification.wrapper_object()
        print("object Area Rect: {}".format(object.ClientAreaRect()))

        # object.print_control_identifiers()
        # object.minimize()
        # action_write()
    else:
        print("Window exists")
    print(specification.child_window(active_only=True, enabled_only=True, visible_only=True))
    specification.print_control_identifiers()


def parse_child_handle(handle):
    print("dump windows: {}".format(dumpwindow(handle)))
    handle_info = dumpwindow(handle=handle)
    children = handle_info["children"]
    # Connect to application and get objects from this application.

    for child in children:
        try:
            child_info = dumpwindow(child)
            print('child_info: {}'.format(child_info))
            if child_info["isvisible"]:
                x, y = get_center_point(child_info['rectangle'])
                move_cursor(x, y)

            if child_info["text"] == 'All Programs':  # if text is All Programs.
                all_programs_info = {'child_info': child_info,
                                     'handle': handle
                                     }
        except Exception as e:
            print('Exception: {}'.format(e))


def parse_handles(handle):
    """
    processing handles
    :param handle: 
    :return: 
    """
    # find current active application and find objects..
    print("dump windows: {}".format(dumpwindow(handle)))
    handle_info = dumpwindow(handle=handle)
    children = handle_info["children"]

    # Connect to application and get objects from this application.
    all_programs_info = None

    for child in children:
        try:
            child_info = dumpwindow(child)
            print('child_info: {}'.format(child_info))
            if child_info["isvisible"]:
                x, y = get_center_point(child_info['rectangle'])
                move_cursor(x, y)
                if len(child_info['children']) != 0:
                    parse_child_handle(child)

            if child_info["text"] == 'All Programs':  # if text is All Programs.
                all_programs_info = {'child_info': child_info,
                                     'handle': handle
                                     }

        except Exception as e:
            print('Exception: {}'.format(e))

    if all_programs_info:
        x, y = get_center_point(all_programs_info['child_info']['rectangle'])
        move_cursor(x, y)
        click_mouse('left')
        typewrite("word")
        time.sleep(3)
        hotkey('enter')


def open_office_word(handle):

    parse_handles(handle=handle)


def work_word():
    """
    Process something on Microsoft word.
    :return: 
    """
    time.sleep(3)
    handle = search_window()
    app.connect(handle=handle)
    time.sleep(3)
    hotkey('enter')

    content = scrapy_content_newsurl()
    print('content1: {}'.format(content))
    typewrite('this is testing to automate text\n')
    typewrite(content)
    # parse_handles( handle)


def start_browser():
    """
    Working with Browser
    :return: 
    """
    hotkey("CTRL", "SHIFT", "N")


def start_main():
    """
    main function entry, it is starting from clicking start menu.
    :return: 
    """

    hotkey('CTRL', 'ESC')  # start menu
    handle = search_window()
    app.connect(handle=handle)

    open_office_word(handle)
    work_word()
    # parse_objects(objects)
    # random_move_cursor(5)


if __name__ == '__main__':
    time.sleep(3)
    start_browser()
    # start_main()
    # move_cursor(576,127)
