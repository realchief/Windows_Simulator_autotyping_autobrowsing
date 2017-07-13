from baseFunctions import *
from keyboard import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import logging

logging.basicConfig(level=logging.INFO, filename='auto-simulator.txt')


class Browse():
    def __init__(self):
        self.RANDOM_BROWSE_COUNT = 0
        self.browser_x = 0
        self.browser_y = 0

    def start(self):
        time.sleep(3)
        try:
            self.driver = webdriver.Ie(os.path.abspath("IEDriverServer.exe"))
        except Exception as e:
            self.driver = webdriver.Ie("C:/workspace_1/automate_lib/IEDriverServer.exe")

        time.sleep(2)
        keyboard.maximize()
        time.sleep(2)
        try:
            for child in dumpwindow(handle=search_window())['children']:
                print("Browser Start function => Dumpwindow: {}\n".format(dumpwindow(handle=child)))
                logging.info("Browser Start function => Dumpwindow: {}\n".format(dumpwindow(handle=child)))

                if dumpwindow(handle=child)['classname'] == 'Frame Tab':
                    self.browser_x, self.browser_y = get_center_point(dumpwindow(handle=child)['rectangle'])
                    move_click_cursor(dumpwindow(handle=child)['rectangle'])

                elif dumpwindow(handle=child)['classname'] == 'ToolbarWindow32' and dumpwindow(handle=child)[
                    'text'] == '':
                    self.backward_x, self.backward_y = get_center_point(dumpwindow(handle=child)['rectangle'])

            time.sleep(2)
        except Exception as e:
            print("Browser Start function => Got Error: {}\n".format(e))
            logging.info("Browser Start function => Got Error: {}\n".format(e))

    def browsing(self, url):
        """
        Type URL in address bar.
        :param url: 
        :return: 
        """
        for child in dumpwindow(handle=search_window())['children']:
            print("Browser browsing Function => dumpwindows: {}\n".format(dumpwindow(handle=child)))
            logging.info("Browser browsing Function => dumpwindows: {}\n".format(dumpwindow(handle=child)))

            if dumpwindow(handle=child)['text'] == 'Address Bar':
                move_click_cursor(dumpwindow(handle=child)['rectangle'])
                keyboard.typewrite(url)
                keyboard.hotkey('enter')
                break

    def login(self):

        try:
            self.driver.get(URL['E-mail'])
            WebDriverWait(self.driver, 10)
            inbox_table = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "username")))
            time.sleep(5)

            # Type username in form field.
            username_form = self.driver.find_element_by_id('username')
            location = username_form.location
            move_click_browser(self.browser_x + location['x'], self.browser_y + location['y'])
            time.sleep(1)
            self.e_mail_name = random.choice(EMAIL.keys())
            keyboard.typemail(self.e_mail_name)
            keyboard.hotkey('TAB')

            # Type password in form field.
            password_form = self.driver.find_element_by_id('password')
            move_click_browser(self.browser_x + password_form.location['x'],
                               self.browser_y + password_form.location['y'])
            time.sleep(1)
            keyboard.typemail(EMAIL[self.e_mail_name])

            # Submit login button
            submit_button = self.driver.find_element_by_id('login_btn')
            location = submit_button.location
            move_click_browser(self.browser_x + location['x'], self.browser_y + location['y'])
            time.sleep(5)

            # Wait for loading next page.
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//section[@id='pm_sidebar']")))

        except Exception as e:
            print("Browser Login function => Got Error: {}".format(e))
            logging.info("Browser Login function => Got Error: {}\n".format(e))
            self.close_borwser()

    def read_conversation_items(self):

        try:
            inbox_table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='conversation-list-columns']")))

            inbox_lists = inbox_table.find_elements_by_class_name('conversation-meta')
            for inbox_item in inbox_lists:
                move_click_browser(self.browser_x + inbox_item.location['x'], self.browser_y + inbox_item.location['y'])
                time.sleep(3)

        except Exception as e:
            print("Browser read_conversation_items => Got Error: {}".format(e))
            logging.info("Browser read_conversation_items => Got Error: {}\n".format(e))

    def read_inbox(self):

        try:
            inbox = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='inbox']")
            inbox_location = inbox.location
            print('Inbox location: {}'.format(inbox_location))
            logging.info('Browser read_inbox function => Inbox location: {}\n'.format(inbox_location))

            move_click_browser(self.browser_x + inbox_location['x'], self.browser_y + inbox_location['y'])
            self.read_conversation_items()
        except Exception as e:
            print("Browser read_inbox got error: {}".format(e))
            logging.info("Browser read_inbox => Got error: {}\n".format(e))

    def read_drafts(self):

        try:
            drafts = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='drafts']")
            drafts_location = drafts.location
            print('Browser read_drafts function => drafts location: {}'.format(drafts_location))
            logging.info('Browser read_drafts function => drafts location: {}\n'.format(drafts_location))

            move_click_browser(self.browser_x + drafts_location['x'], self.browser_y + drafts_location['y'])

            self.read_conversation_items()
        except Exception as e:
            print('Browser read_drafts function got Error: {}'.format(e))
            logging.info('Browser read_drafts function => Got Error: {}\n'.format(e))

    def read_sent(self):
        try:
            sent = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='sent']")
            sent_location = sent.location
            print('Browser read_sent Function => sent location: {}'.format(sent_location))
            logging.info('Browser read_sent Function => sent location: {}\n'.format(sent_location))

            move_click_browser(self.browser_x + sent_location['x'], self.browser_y + sent_location['y'])
            self.read_conversation_items()
        except Exception as e:
            print('Browser read_sent Function => Got Error: {}'.format(e))
            logging.info('Browser read_sent Function => Got Error: {}\n'.format(e))

    def read_starred(self):
        try:
            starred = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='starred']")
            starred_location = starred.location
            print('Browser read_starred function => starred location: {}'.format(starred_location))
            logging.info('Browser read_starred function => starred location: {}'.format(starred_location))

            move_click_browser(self.browser_x + starred_location['x'], self.browser_y + starred_location['y'])
            self.read_conversation_items()
        except Exception as e:
            print('Browser read_starred function => Got Error: {}'.format(e))
            logging.info('Browser read_starred function => Got Error: {}'.format(e))

    def read_archive(self):
        try:
            archive = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='archive']")
            archive_location = archive.location
            print('archive location: {}'.format(archive_location))
            logging.info('Browser read_archive function => archive location: {}'.format(archive_location))

            move_click_browser(self.browser_x + archive_location['x'], self.browser_y + archive_location['y'])
            self.read_conversation_items()
        except Exception as e:
            print('Browser read_archive function => Got Error: {}'.format(e))
            logging.info('Browser read_archive function => Got Error: {}'.format(e))

    def read_spam(self):
        try:
            spam = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='spam']")
            spam_location = spam.location
            print('Browser read_spam function => spam location: {}'.format(spam_location))
            logging.info('Browser read_spam function => spam location: {}'.format(spam_location))

            move_click_browser(self.browser_x + spam_location['x'], self.browser_y + spam_location['y'])
            self.read_conversation_items()
        except Exception as e:
            print('Browser read_spam function => Got Error: {}'.format(e))
            logging.info('Browser read_spam function => Got Error: {}'.format(e))

    def read_trash(self):
        try:
            trash = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='trash']")
            trash_location = trash.location
            print('Browser read_trash function => Trash location: {}'.format(trash_location))
            logging.info('Browser read_trash function => Trash location: {}'.format(trash_location))

            move_click_browser(self.browser_x + trash_location['x'], self.browser_y + trash_location['y'])
            self.read_conversation_items()
        except Exception as e:
            print('Browser read_trash function => Got Error: {}'.format(e))
            logging.info('Browser read_trash function => Got Error: {}'.format(e))
            # self.close_borwser()

    def compose_mail(self):
        try:
            compose = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//button")
            compose_location = compose.location
            move_click_browser(self.browser_x + compose_location['x'], self.browser_y + compose_location['y'])

            tomail_form = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//form[@id='pm_composer']//input[@name='autocomplete']")))
            move_click_browser(self.browser_x + tomail_form.location['x'], self.browser_y + tomail_form.location['y'])
            time.sleep(3)

            sent_mail = [item for item in EMAIL.keys() if item != self.e_mail_name]
            keyboard.typemail(sent_mail[0])
            time.sleep(3)

            keyboard.hotkey('TAB')
            title_form = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//form[@id='pm_composer']//input[@title='Subject']")))
            move_click_browser(self.browser_x + title_form.location['x'], self.browser_y + title_form.location['y'])
            time.sleep(3)
            keyboard.typemail('From ' + self.e_mail_name)

            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//form[@id='pm_composer']//iframe[@class='squireIframe']")))
            move_click_browser(self.browser_x + iframe.location['x'], self.browser_y + iframe.location['y'])
            time.sleep(3)
            keyboard.typemail('test')
            time.sleep(5)

            send_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//form[@id='pm_composer']//button[@data-message='message']")))
            move_click_browser(self.browser_x + send_button.location['x'], self.browser_y + send_button.location['y'])
            time.sleep(5)

        except Exception as e:
            logging.info('Browser compose_mail function => Got Error: {}'.format(e))
            self.close_borwser()

    def close_borwser(self):
        self.driver.quit()

    def logout(self):
        try:
            user_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='body']//li[@class='navigationUser']")))

            move_click_browser(self.browser_x + user_button.location['x'], self.browser_y + user_button.location['y'])

            time.sleep(3)
            logout_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='body']//li[@class='navigationUser']//a[@ui-sref='login']")))

            move_click_browser(self.browser_x + logout_button.location['x'],
                               self.browser_y + logout_button.location['y'])

        except Exception as e:
            logging.info('Browser logout Function => Got Error: {}'.format(e))

    def google_button(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[@id='_fZl']")))
            move_click_browser(self.browser_x + button.location['x'], self.browser_y + button.location['y'])

        except Exception as e:
            logging.info('Browser Google Button => Got Error: {}'.format(e))

    def google_entry(self):
        try:
            if self.RANDOM_BROWSE_COUNT == 0:
                self.browsing('https://google.com')
                time.sleep(3)
            search_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.NAME, "q")))

            move_click_browser(self.browser_x + search_box.location['x'], self.browser_y + search_box.location['y'],
                               number=2)
            time.sleep(.5)
            move_click_browser(self.browser_x + search_box.location['x'], self.browser_y + search_box.location['y'],
                               number=2)
            time.sleep(3)
            keyboard.hotkey('CTRL', 'A')
            time.sleep(2)
            keyboard.typewrite(random.choice(Random_Keyword))
            self.google_button()
            self.search_google()
        except Exception as e:
            logging.info('Browser Google Entry Function => Got Error: {}'.format(e))

    def search_google(self):
        try:
            item_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='rso']")))
            items = self.driver.find_elements_by_xpath("//div[@id='rso']//div[@class='g']")
            print('items: {}'.format(items))
            logging.info('Browser search google Function => Items: {}'.format(items))

            for index, item in enumerate(items):
                print(index, item)
                if index == 5:
                    break
                if index % 2 == 0:
                    scroll_mouse(count=1, sensivity=-150)
                if index == 0:
                    first_element = (self.browser_x + item.location['x'], self.browser_y + item.location['y'])
                move_cursor_browser(self.browser_x + item.location['x'], self.browser_y + item.location['y'])
                time.sleep(1)

            scroll_mouse(count=5, sensivity=200)
            move_click_browser(first_element[0], first_element[1])
            time.sleep(8)
            scroll_mouse(count=3, sensivity=-150, pause=3)
            time.sleep(3)
            scroll_mouse(count=4, sensivity=200, pause=3)
            # Count < 5
            if self.RANDOM_BROWSE_COUNT <= 5:
                self.random_browsing()
        except Exception as e:
            logging.info('Browser search google Function => Got Errors: {}'.format(e))

    def random_browsing(self):
        """
        Iterate google entry function.
        :return: 
        """
        self.RANDOM_BROWSE_COUNT += 1
        keyboard.backward()
        time.sleep(1)
        # move_click_browser(self.backward_x, self.backward_y)
        time.sleep(1)
        self.google_entry()

    def popular_sites(self, repeat=10):
        """
        Visit popular sites
        :return: 
        """
        urls = parse_csv()

        for i in range(repeat):
            try:
                self.browsing(random.choice(urls))
                time.sleep(5)
                body_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body")))

                move_cursor_browser(self.browser_x + body_element.location['x'] + 300,
                                    self.browser_y + body_element.location['y'] + 50)
                time.sleep(3)
                scroll_mouse(5, sensivity=random.choice([-200, -300]))
                time.sleep(random.choice([2, 4, 6, 8]))
                scroll_mouse(4, sensivity=random.choice([180, 200, 250]))
                time.sleep(random.choice([2, 4, 6, 8]))

            except Exception as e:
                print('Browser popular sites Function => Got Error: {}'.format(e))
                continue

browser = Browse()

if __name__ == '__main__':
    browser = Browse()
    browser.start()
    browser.login()
    browser.read_inbox()
    browser.read_drafts()
    browser.read_sent()
    browser.compose_mail()
    browser.logout()
    browser.google_entry()
    browser.popular_sites()
