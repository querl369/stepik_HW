from selenium import webdriver
import time
import math

try:
    link = "https://suninjuly.github.io/execute_script.html"
    driver = webdriver.Chrome()
    driver.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_value = driver.find_element_by_id("input_value").text

    input_field = driver.find_element_by_id("answer")
    driver.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    input_field.send_keys(calc(int(x_value)))

    robot_checkbox = driver.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    robot_radio = driver.find_element_by_id("robotsRule")
    robot_radio.click()

    submit_btn = driver.find_element_by_css_selector(".btn")
    submit_btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()