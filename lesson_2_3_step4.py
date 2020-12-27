from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    button = browser.find_element_by_css_selector(".btn.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input_value = browser.find_element_by_id("input_value")
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(calc(input_value.text))
    input_btn = browser.find_element_by_css_selector(".btn.btn")
    input_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

