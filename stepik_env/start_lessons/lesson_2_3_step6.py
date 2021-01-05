from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    button = browser.find_element_by_css_selector(".trollface.btn")
    button.click()

    new_window = browser.window_handles[1]

    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    input_value = browser.find_element_by_id("input_value")
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(calc(input_value.text))
    input_btn = browser.find_element_by_css_selector(".btn.btn")
    input_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

