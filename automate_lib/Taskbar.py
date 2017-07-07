from __future__ import print_function

from baseFunctions import *
from web import *


class Taskbar():

    def __init__(self):
        app = Application().Connect(title=u'', class_name='Shell_TrayWnd')
        self.shell_trayWnd = app.Shell_TrayWnd

    def hidden_icons(self):
        hidden = self.shell_trayWnd[u'4']

        # Get location of hidden Icons.
        move_click_cursor(hidden.Rectangle())

        children = dumpwindow(handle=search_window())['children']

        # In pop up window of NotifyArea.
        for child in children:
            if dumpwindow(handle=child)['classname'] == 'SysLink':
                # click "customize Link
                move_click_cursor(dumpwindow(handle=child)['rectangle'])
                time.sleep(3)
                # open pop up window
                for item in dumpwindow(handle=search_window())['children']:
                    print(dumpwindow(handle=item))
                    move_cursor(dumpwindow(handle=item)['rectangle'])
                    # scroll bar
                    if dumpwindow(handle=item)["classname"] == 'ScrollBar':
                        move_click_cursor(dumpwindow(handle=item)['rectangle'], number=3)

                    elif dumpwindow(handle=item)["classname"] == "CtrlNotifySink":
                        move_click_cursor(dumpwindow(handle=item)['rectangle'])
                        time.sleep(1)
                        # item option list
                        for child in dumpwindow(handle=search_window())['children']:
                            move_cursor(dumpwindow(handle=item)['rectangle'])

                    # Ok Button
                    elif dumpwindow(handle=item)["text"] == "OK":
                        OK_Button_POS = dumpwindow(handle=item)['rectangle']

                    # Cancel Button
                    elif dumpwindow(handle=item)["text"] == "Cancel":
                        Cancel_Button_POS = dumpwindow(handle=item)['rectangle']

            elif dumpwindow(handle=child)['classname'] == 'ToolbarWindow32':
                # click "NotifyArea"
                pass

            # move_click_cursor(OK_Button_POS)

    def start_menu(self):

        move_click_cursor(self.shell_trayWnd.Rectangle())
        children = dumpwindow(handle=search_window())['children']
        print('children: {}'.format(children))

        All_Programs_handle = None

        # In Start Menu
        for child in children:
            print(dumpwindow(handle=child))
            move_cursor(dumpwindow(handle=child)['rectangle'])
            if dumpwindow(handle=child)['text'] == "All Programs":
                All_Programs_handle = child

        # In "All programs", scroll aciton.
        if All_Programs_handle is not None:
            move_click_cursor(dumpwindow(handle=All_Programs_handle)['rectangle'])
            scroll_mouse(10, 50)
            scroll_mouse(10, -50)

    def clock_time(self):
        """
        start clock time on the taskbar.
        :return: 
        """
        print(self.shell_trayWnd)
        trayClock = self.shell_trayWnd[u'TrayClockWClass']
        move_click_cursor(trayClock.Rectangle())
        time.sleep(1)
        # open time window.
        for child in dumpwindow(handle=search_window())['children']:
            print(dumpwindow(handle=child))
            move_cursor(dumpwindow(handle=child)['rectangle'])
        move_click_cursor(trayClock.Rectangle())


taskbar = Taskbar()


class Office():

    def __init__(self):
        taskbar.start_menu()
        time.sleep(3)

        keyboard.typewrite('wordpad')
        time.sleep(1)

        keyboard.hotkey('enter')
        time.sleep(3)

        print(dumpwindow(handle=search_window()))
        for child in dumpwindow(handle=search_window())['children']:
            print(dumpwindow(handle=child))
            move_cursor(dumpwindow(handle=child)['rectangle'])

        time.sleep(3)
        keyboard.hotkey('enter')

    def write_letters(self):
        """
        Randowm write the letters in wordpad.
        :return: 
        """
        scrapy_content_newsurl()

    def close_save_office(self):
        """
        Save the office word
        :return: 
        """

        keyboard.close()
        time.sleep(2)
        keyboard.hotkey('enter')
        time.sleep(2)
        for child in dumpwindow(handle=search_window())['children']:
            print(dumpwindow(handle=child))

            if dumpwindow(handle=child)['text'] == '&Save':
                SaveButton = dumpwindow(handle=child)['rectangle']
                break
        #  write the file name to save.
        keyboard.typewrite('test')
        move_click_cursor(SaveButton)


if __name__ == '__main__':
    word = Office()
    word.close_save_office()