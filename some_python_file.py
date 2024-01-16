from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os


def test():
    try: 
        link = "http://suninjuly.github.io/file_input.html"
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'file.txt')

        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.NAME, "firstname")
        first_name.send_keys('Alexey')

        last_name = browser.find_element(By.NAME, "lastname")
        last_name.send_keys('Solovev')

        email = browser.find_element(By.NAME, "email")
        email.send_keys('alexsololol@gmail.com')

        input_file_button = browser.find_element(By.ID, 'file')
        input_file_button.send_keys(file_path)

        button = browser.find_element(By.CSS_SELECTOR, 'button')
        button.click()

    finally:
        time.sleep(10)
        browser.quit()


def negative_test():
    try: 
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
        first_name.send_keys('Alexey')

        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
        last_name.send_keys('Solovev')

        email = browser.find_element(By.CSS_SELECTOR, ".third_class input.third")
        email.send_keys('mailexample@mail.ru')

        button = browser.find_element(By.XPATH, '//*[@type="submit"]')
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(10)
        browser.quit()

test()
