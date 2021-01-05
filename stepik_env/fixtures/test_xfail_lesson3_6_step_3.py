import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
answer = math.log(int(time.time()))

@pytest.mark.parametrize('url_identifier', ['236895', '236896', '236897', '236898',
'236899', '236903', '236904', '236905'])
def test_alien_message_gathering(browser, url_identifier):
    link = f'https://stepik.org/lesson/{url_identifier}/step/1'
    browser.get(link)
    text_field = browser.find_element(By.CSS_SELECTOR, '.textarea.string-quiz__textarea')
    text_field.send_keys(f'{answer}')
    submit_btn = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    submit_btn.click()