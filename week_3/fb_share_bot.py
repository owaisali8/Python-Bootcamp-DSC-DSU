from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
from time import sleep

driver = None


def driver_in():
    global driver
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_opt)
    driver.get("https://m.facebook.com/")
    return driver


def login():
    driver = driver_in()
    email = input('Enter your email: ')
    password = getpass.getpass()
    email_field = driver.find_element_by_id("m_login_email")
    password_field = driver.find_element_by_id('m_login_password')
    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)
    sleep(5)


def goto_post():
    post_link = input("Enter post link that you want to share: ")
    driver.get(post_link)


def share_post():
    share_btn = driver.find_element_by_css_selector('a._15kr._77li')
    share_btn.click()
    write_post = driver.find_element_by_id("share-with-message-button")
    write_post.click()
    text_post = input("What do you want to write on your post: ")
    driver.find_element_by_id("share_msg_input").send_keys(text_post)
    driver.find_element_by_id("share_submit").click()


def like_post():
    driver.find_element_by_css_selector('a._15ko._77li.touchable').click()


def main():
    login()
    goto_post()
    like_post()
    share_post()
    sleep(5)


if __name__ == "__main__":
    main()
