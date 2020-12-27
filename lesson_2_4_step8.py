from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price_wait = WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_btn = browser.find_element(By.ID, "book")
    book_btn.click()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input_value = browser.find_element(By.ID, "input_value")
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(calc(input_value.text))
    input_btn = browser.find_element(By.ID, "solve")
    input_btn.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[-1])

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(15)
    browser.quit()

# не забываем оставить пустую строку в конце файла

