from baseFunctions import *
from keyboard import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os


class Browse():

    def __init__(self):
        pass

    def start(self):
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
        """
        Type URL in address bar.
        :param url: 
        :return: 
        """
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
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//section[@id='pm_sidebar']")))

    def read_conversation_items(self):
        inbox_table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='conversation-list-columns']")))

        inbox_lists = inbox_table.find_elements_by_class_name('conversation-meta')
        for inbox_item in inbox_lists:
            move_click_browser(self.browser_x + inbox_item.location['x'], self.browser_y + inbox_item.location['y'])
            time.sleep(3)

    def read_inbox(self):
        inbox = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='inbox']")
        inbox_location = inbox.location
        print('Inbox location: {}'.format(inbox_location))

        move_click_browser(self.browser_x + inbox_location['x'], self.browser_y + inbox_location['y'])
        self.read_conversation_items()

    def read_drafts(self):
        drafts = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='drafts']")
        drafts_location = drafts.location
        print('drafts location: {}'.format(drafts_location))

        move_click_browser(self.browser_x + drafts_location['x'], self.browser_y + drafts_location['y'])

        self.read_conversation_items()

    def read_sent(self):
        sent = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='sent']")
        sent_location = sent.location
        print('sent location: {}'.format(sent_location))

        move_click_browser(self.browser_x + sent_location['x'], self.browser_y + sent_location['y'])
        self.read_conversation_items()

    def read_starred(self):
        starred = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='starred']")
        starred_location = starred.location
        print('starred location: {}'.format(starred_location))

        move_click_browser(self.browser_x + starred_location['x'], self.browser_y + starred_location['y'])
        self.read_conversation_items()

    def read_archive(self):
        archive = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='archive']")
        archive_location = archive.location
        print('archive location: {}'.format(archive_location))

        move_click_browser(self.browser_x + archive_location['x'], self.browser_y + archive_location['y'])
        self.read_conversation_items()

    def read_spam(self):
        spam = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='spam']")
        spam_location = spam.location
        print('spam location: {}'.format(spam_location))

        move_click_browser(self.browser_x + spam_location['x'], self.browser_y + spam_location['y'])
        self.read_conversation_items()

    def read_trash(self):
        trash = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='trash']")
        trash_location = trash.location
        print('Trash location: {}'.format(trash_location))

        move_click_browser(self.browser_x + trash_location['x'], self.browser_y + trash_location['y'])
        self.read_conversation_items()

    def compose_mail(self):
        compose = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//button")
        compose_location = compose.location
        move_click_browser(self.browser_x + compose_location['x'], self.browser_y + compose_location['y'])

        tomail_form = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//form[@id='pm_composer']//input[@name='autocomplete']")))
        move_click_browser(self.browser_x + tomail_form.location['x'], self.browser_y + tomail_form.location['y'])
        time.sleep(3)

        keyboard.typemail('test@mail.com')
        time.sleep(1)

        title_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form[@id='pm_composer']//input[@title='Subject']")))
        move_click_browser(self.browser_x + title_form.location['x'], self.browser_y + title_form.location['y'])
        time.sleep(3)
        keyboard.typemail('From Test')

        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form[@id='pm_composer']//iframe[@class='squireIframe']")))
        move_click_browser(self.browser_x + iframe.location['x'], self.browser_y + iframe.location['y'])
        time.sleep(3)
        keyboard.typemail('test')

        send_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form[@id='pm_composer']//button[@data-message='message']")))
        move_click_browser(self.browser_x + send_button.location['x'], self.browser_y + send_button.location['y'])

    def close_borwser(self):
        self.driver.quit()

    def logout(self):
        user_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='body']//li[@class='navigationUser']")))

        move_click_browser(self.browser_x + user_button.location['x'], self.browser_y + user_button.location['y'])

        time.sleep(3)
        logout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='body']//li[@class='navigationUser']//a[@ui-sref='login']")))

        move_click_browser(self.browser_x + logout_button.location['x'], self.browser_y + logout_button.location['y'])

    def google_button(self):

        button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='_fZl']")))
        move_click_browser(self.browser_x + button.location['x'], self.browser_y + button.location['y'])

    def google_entry(self):
        self.browsing('https://google.com')
        time.sleep(3)
        search_box = self.driver.find_element_by_name('q')
        move_click_browser(self.browser_x + search_box.location['x'], self.browser_y + search_box.location['y'])
        time.sleep(3)
        keyboard.typewrite('title')
        self.google_button()
        self.search_google()

    def search_google(self):
        item_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='rso']")))
        items = self.driver.find_elements_by_xpath("//div[@id='rso']//div[@class='g']")

        for index, item in enumerate(items):
            print(index, item)
            if index % 2 == 0:
                scroll_mouse(count=2, sensivity=-200)
            move_cursor_browser(self.browser_x + item.location['x'], self.browser_y + item.location['y'])
            time.sleep(1)

browser = Browse()

if __name__ == '__main__':
    browser = Browse()
    browser.start()
    browser.google_entry()
    # browser.login()
    # browser.logout()
    # browser.compose_mail()
