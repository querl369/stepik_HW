from selenium import webdriver
import unittest
import time

class TestRegistration(unittest.TestCase):
    def test_first(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector(".first_block .first")
        first_name.send_keys("some text")

        last_name = browser.find_element_by_css_selector(".first_block .second")
        last_name.send_keys("some_text2")

        email_field = browser.find_element_by_css_selector(".first_block .third")
        email_field.send_keys("some_email.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "The text dont equal")

        time.sleep(10)

        browser.quit()
    def test_second(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector(".first_block .first")
        first_name.send_keys("some text")

        last_name = browser.find_element_by_css_selector(".first_block .second")
        last_name.send_keys("some_text2")

        email_field = browser.find_element_by_css_selector(".first_block .third")
        email_field.send_keys("some_email.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "The text dont equal")

        time.sleep(10)

        browser.quit()

if __name__ == "__main__":
    unittest.main()