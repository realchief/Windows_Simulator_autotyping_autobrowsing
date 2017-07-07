from baseFunctions import *
from keyboard import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Browse():
    def __init__(self):
        time.sleep(3)

        self.driver = webdriver.Ie("IEDriverServer.exe")

        time.sleep(2)
        keyboard.maximize()
        time.sleep(2)
        for child in dumpwindow(handle=search_window())['children']:
            print(dumpwindow(handle=child))
            if dumpwindow(handle=child)['classname'] == 'Frame Tab':
                self.browser_x, self.browser_y = get_center_point(dumpwindow(handle=child)['rectangle'])
                move_click_cursor(dumpwindow(handle=child)['rectangle'])
                break

        time.sleep(2)

    def browsing(self, url):
        print(dumpwindow(handle=search_window()))
        for child in dumpwindow(handle=search_window())['children']:
            print(dumpwindow(handle=child))
            if dumpwindow(handle=child)['text'] == 'Address Bar':
                move_click_cursor(dumpwindow(handle=child)['rectangle'])
                keyboard.typewrite(url)
                keyboard.hotkey('enter')

    def login(self):
        self.driver.get(URL['E-mail'])
        WebDriverWait(self.driver, 10)
        time.sleep(5)

        username_form = self.driver.find_element_by_id('username')
        location = username_form.location
        move_click_browser(self.browser_x + location['x'], self.browser_y + location['y'])
        time.sleep(1)
        e_mail_name = random.choice(EMAIL.keys())
        keyboard.typemail(e_mail_name)
        keyboard.hotkey('TAB')

        password_form = self.driver.find_element_by_id('password')
        move_click_browser(self.browser_x + password_form.location['x'], self.browser_y + password_form.location['y'])
        time.sleep(1)
        keyboard.typemail(EMAIL[e_mail_name])

        submit_button = self.driver.find_element_by_id('login_btn')
        location = submit_button.location
        move_click_browser(self.browser_x + location['x'], self.browser_y + location['y'])
        WebDriverWait(self.driver, 20)

    def read_inbox(self):
        time.sleep(5)
        inbox = self.driver.find_element_by_css_selector('subject-text ellipsis')
        inbox_location = inbox.location
        move_click_browser(self.browser_x + inbox_location['x'], self.browser_y + inbox_location['y'])

    def google(self):
        self.browsing('https://google.com')
        time.sleep(3)
        search_box = self.driver.find_element_by_name('q')
        move_click_browser(self.browser_x + search_box.location['x'], self.browser_y + search_box.location['y'])

    def close_borwser(self):
        self.driver.quit()


if __name__ == '__main__':

    browser = Browse()
    browser.google()
    # browser.login()
    # browser.read_inbox()