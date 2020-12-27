from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_id("input_value")

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(calc(x_element.text))

    checkbox_robot = browser.find_element_by_id("robotCheckbox")
    checkbox_robot.click()

    radio_robot = browser.find_element_by_id("robotsRule")
    radio_robot.click()

    submit_btn = browser.find_element_by_css_selector(".btn")
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()