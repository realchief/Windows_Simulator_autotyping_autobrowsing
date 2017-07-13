from __future__ import print_function

from baseFunctions import *
from web import *
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, filename='auto-simulator.txt')


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
        # try:
        #     move_click_cursor(self.shell_trayWnd.Rectangle())
        #     children = dumpwindow(handle=search_window())['children']
        #     print('children: {}'.format(children))
        #
        #     All_Programs_handle = None
        #
        #     # In Start Menu
        #     for child in children:
        #         print(dumpwindow(handle=child))
        #         move_cursor(dumpwindow(handle=child)['rectangle'])
        #         # if dumpwindow(handle=child)['text'] == "All Programs":
        #         #     All_Programs_handle = child
        #
        #     # In "All programs", scroll action.
        #     if All_Programs_handle is not None:
        #         move_click_cursor(dumpwindow(handle=All_Programs_handle)['rectangle'])
        #         scroll_mouse(10, 50)
        #         scroll_mouse(10, -50)
        # except Exception as e:
        #     logging.info("Taskbar start_menu function => Got Error: {}".format(e))
        keyboard.hotkey('CTRL', 'ESC')

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

    def Running_Application(self):
        """
        Get Running Application
        :return: 
        """
        mstaskwwclass = self.shell_trayWnd.MSTaskSwWClass
        mstaskwwclass_wrap = mstaskwwclass.wrapper_object()

        move_cursor(mstaskwwclass.Rectangle())


taskbar = Taskbar()


class Office():
    def __init__(self):
        print("Starting Office")
        logging.info("Office init function => Starting Office Class....")
        self.zoomin_x = self.zoomin_y = self.zoomout_x = self.zoomout_y = None

    def start(self):
        taskbar.start_menu()
        time.sleep(3)

        keyboard.typewrite('wordpad')
        time.sleep(1)

        keyboard.hotkey('enter')
        time.sleep(3)

        keyboard.maximize()
        time.sleep(3)

        print(dumpwindow(handle=search_window()))
        for index,  child in enumerate(dumpwindow(handle=search_window())['children']):
            print(dumpwindow(handle=child))
            logging.info("Office start function => Information: {}".format(dumpwindow(handle=child)))
            if dumpwindow(handle=child)['classname'] == 'Static' and dumpwindow(handle=child)['text'] == '-':
                self.zoomout_x, self.zoomout_y = get_center_point(dumpwindow(handle=child)['rectangle'])

            elif dumpwindow(handle=child)['classname'] == 'Static' and dumpwindow(handle=child)['text'] == '+':
                self.zoomin_x, self.zoomin_y = get_center_point(dumpwindow(handle=child)['rectangle'])

            # if index % 3 == 0:
            move_cursor(dumpwindow(handle=child)['rectangle'])
            time.sleep(1)

        time.sleep(3)
        # keyboard.hotkey('enter')

    def write_letters(self):
        """
        Randowm write the letters in wordpad.
        :return: 
        """
        print('write letters')
        logging.info("Office Write_letters function => write letters.\n")
        time.sleep(5)
        scrapy_content_newsurl()
        time.sleep(3)
        scroll_mouse(4, sensivity=250)
        time.sleep(1)
        scroll_mouse(4, sensivity=-220)

        time.sleep(3)
        self.modify_properties()
        time.sleep(3)

        scroll_mouse(4, sensivity=250)
        time.sleep(1)
        scroll_mouse(4, sensivity=-220)

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
            if dumpwindow(handle=child)['text'] == 'Rich Text Format (RTF)':
                move_click_cursor(dumpwindow(handle=child)['rectangle'])
                time.sleep(1)
                keyboard.keydown('down')
                keyboard.hotkey('enter')

            if dumpwindow(handle=child)['classname'] == 'Edit':
                filename_editbox_rectangle = dumpwindow(handle=child)['rectangle']

            if dumpwindow(handle=child)['text'] == '&Save':
                SaveButton = dumpwindow(handle=child)['rectangle']
                break

        #  write the file name to save.
        filename = 'test-' + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
        move_click_cursor(filename_editbox_rectangle, number=2)
        time.sleep(1)
        keyboard.typewrite(filename)
        time.sleep(.5)
        move_click_cursor(SaveButton)

    def change_font_size(self, flag, iteration=1):
        """
        :return: 
        """
        for i in range(iteration):
            if flag:
                # increase font size
                keyboard.hotkey('Ctrl', 'Shift', '>')
            else:
                # decrease font size
                keyboard.hotkey('Ctrl', 'Shift', '<')

            time.sleep(1)

    def change_bold(self, iteration=1):
        """
        change bold
        :return: 
        """
        for i in range(iteration):
            keyboard.hotkey('CTRL', 'B')

    def change_font_style(self):
        """
        Change font style.
        :return: 
        """

    def modify_properties(self):
        """
        Manipulate some font size, font style, bold, italic, etc.
        :return: 
        """
        keyboard.hotkey('CTRL', 'A')
        time.sleep(2)

        # change font size.
        self.change_font_size(flag=1, iteration=random.choice([1,2,3]))
        time.sleep(3)

        # change font bold
        self.change_bold(iteration=random.choice([1,2,3,4]))
        time.sleep(3)

office = Office()

if __name__ == '__main__':
    time.sleep(3)
    office.start()
    # office.write_letters()
    # office.write_letters()
    # office.close_save_office()