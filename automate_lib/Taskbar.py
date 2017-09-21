from __future__ import print_function

from baseFunctions import *
from web import *
from datetime import datetime
import logging


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
            try:
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

                        # Cancel Butriter.
                        elif dumpwindow(handle=item)["text"] == "Cancel":
                            Cancel_Button_POS = dumpwindow(handle=item)['rectangle']

                elif dumpwindow(handle=child)['classname'] == 'ToolbarWindow32':
                    # click "NotifyArea"
                    pass
                    # move_click_cursor(OK_Button_POS)
            except Exception as e:
                print('Exception: {}'.format(e))

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
        #     # In "All programs", scroll action. whi
        #     if All_Progra
        # ms_handle is not None:
        #         move_click_cursor(dumpwindow(handle=All_Programs_handle)['rectangle'])
        #         scroll_mouse(10, 50)
        #         scroll_mouse(10, -50)
        # except Exception as e:
        #     logging.info("Taskbar start_menu function => Got Error: {}".format(e))
        time.sleep(2)
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

    def switch_language(self):
        """
        Switch languages
        :return: 
        """
        lgbtn = self.shell_trayWnd[u'3']
        lgbtn_wrap = lgbtn.wrapper_object()

        move_click_cursor(lgbtn_wrap.Rectangle())
        time.sleep(2)
        move_click_cursor(lgbtn_wrap.Rectangle())

        keyboard.switch_lg()


taskbar = Taskbar()


class Office():
    def __init__(self):
        print("Starting Office")
        self.zoomin = self.zoomout = None
        self.font_style = self.font_size = None

    def start(self):
        taskbar.start_menu()
        time.sleep(3)

        keyboard.typewrite('wordpad')
        time.sleep(1)

        keyboard.hotkey('enter')
        time.sleep(3)

        # keyboard.maximize()
        # time.sleep(3)
        # keyboard.hotkey('enter')
        print(
            dumpwindow(handle=search_window()))
        for index, child in enumerate(dumpwindow(handle=search_window())['children']):
            child_dump = dumpwindow(handle=child)
            print(child_dump)

            if child_dump['classname'] == 'Button' and child_dump['text'] == '-':
                self.zoomout = child_dump['rectangle']

            elif child_dump['classname'] == 'Button' and child_dump['text'] == '+':
                self.zoomin = child_dump['rectangle']

            elif child_dump['classname'] == 'UIRibbonCommandBarDock' and child_dump['text'] == "UIRibbonDockTop":
                self.file_menu = child_dump['rectangle']

            elif child_dump['classname'] == 'RICHEDIT50W' and child_dump['text'] == '\r\n':
                self.doc_body = child_dump['rectangle']

            elif child_dump['classname'] == 'RICHEDIT50W' and str(child_dump['text']).isdigit():
                print('self.font_size ')
                self.font_size = child_dump['rectangle']

            elif child_dump['classname'] == 'RICHEDIT50W' and child_dump['text'] != '':
                print('self.font_style')
                self.font_style = child_dump['rectangle']

        self.obj_list = [self.file_menu, self.font_size, self.font_style, self.zoomin, self.zoomout]

    def change_font_size(self):
        """
        Change font size.
        :return: 
        """
        try:
            move_click_cursor(self.font_size)
            time.sleep(3)
            keyboard.hotkey('DOWN') 
            time.sleep(2)

            for i in range(random.randint(3, 10)):
                time.sleep(1)
                keyboard.hotkey('DOWN')

            keyboard.hotkey('ENTER')
        except Exception as e:
            print('Change_font_size function => Got Error: {}'.format(e))

    def change_font_sytle(self):
        """
        Change font style
        :return:
        """
        try:
            move_click_cursor(self.font_style)
            time.sleep(3)
            keyboard.hotkey('DOWN')
            time.sleep(2)
            keyboard.typewrite(str(random.randint(13, 25)))
            time.sleep(1)
            keyboard.hotkey('ENTER')

        except Exception as e:
            print('Change_font_style function => Got Error: {}'.format(e))

    def change_zoomin(self):
        """
        Change Zoom in.
        :return: 
        """
        for i in range(random.randint(2, 3)):
            time.sleep(1)
            move_click_cursor(self.zoomin)

    def change_zoomout(self):
        """
        Change Zoom out.
        :return: 
        """
        for i in range(random.randint(1, 2)):
            time.sleep(1)
            move_click_cursor(self.zoomout)

    def change_bold(self, iteration=1):
        """
        change bold
        :return: 
        """
        for i in range(iteration):
            keyboard.hotkey('CTRL', 'B')
            time.sleep(1)

    def write_letters(self):
        """
        Random write the letters in wordpad.
        :return: 
        """
        print('write letters')
        # self.modify_properties()
        time.sleep(3)
        scrapy_content_newsurl()
        time.sleep(3)
        scroll_mouse(4, sensivity=250)
        time.sleep(1)
        scroll_mouse(4, sensivity=-220)

        time.sleep(3)

        scroll_mouse(4, sensivity=250)
        time.sleep(1)
        scroll_mouse(4, sensivity=-220)
        time.sleep(3)

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
                time.sleep(1)
                keyboard.hotkey('enter')

            if dumpwindow(handle=child)['classname'] == 'Edit':
                filename_editbox_rectangle = dumpwindow(handle=child)['rectangle']

            if dumpwindow(handle=child)['text'] == '&Save':
                SaveButton = dumpwindow(handle=child)['rectangle']
                break

        # write the file name to save.
        filename = 'test-' + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
        move_click_cursor(filename_editbox_rectangle, number=2)
        time.sleep(1)
        keyboard.typewrite(filename)
        time.sleep(.5)
        move_click_cursor(SaveButton)

    def modify_properties(self):
        """
        Manipulate some font size, font style, bold, italic, etc.
        :return:
        """
        move_click_cursor(self.file_menu)
        time.sleep(2)
        move_click_cursor(self.file_menu)
        time.sleep(2)
        modify_function_list = [self.change_zoomin(), self.change_zoomout()]
        random.shuffle(modify_function_list)
        print(modify_function_list)

        for i in range(0, len(modify_function_list)):
            try:
                modify_function_list[i]()
            except Exception as e:
                print('Exception: {}'.format(e))
            time.sleep(1)
        move_click_cursor(self.doc_body)
        time.sleep(2)


office = Office()

if __name__ == '__main__':
    time.sleep(3)
    # taskbar.switch_language()
    i = 0
    while i < 5:
        office.start()
        office.write_letters()
        office.close_save_office()
        i += 1