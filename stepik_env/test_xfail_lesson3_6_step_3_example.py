import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.xfail()
@pytest.mark.parametrize('url_identifier', ['236898', '236899', '236903', '236904', '236905'])
def test_alien_message_gathering(browser, url_identifier):
    link = f'https://stepik.org/lesson/{url_identifier}/step/1'
    browser.get(link)
    login_btn = browser.find_element(By.CSS_SELECTOR, '.navbar__auth_login')
    login_btn.click()
    login_field = browser.find_element(By.CSS_SELECTOR, '[name="login"]')
    login_field.send_keys('yemets3@gmail.com')
    passwrd_field = browser.find_element(By.ID, 'id_login_password')
    passwrd_field.send_keys('01920392')
    submit_btn = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn')
    submit_btn.click()
    time.sleep(2)
    answer_field = browser.find_element(By.CSS_SELECTOR, '.textarea.string-quiz__textarea')
    answer_field.send_keys(f'{math.log(int(time.time()))}')
    sumbit_btn = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    sumbit_btn.click()
    if browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint'):
        check_text = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
        print(check_text)
        assert check_text == 'Correct!', 'Wrong word!'
    else:
        pass

