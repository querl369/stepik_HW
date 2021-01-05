from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    driver = webdriver.Chrome()
    driver.get(link)

    first_name = driver.find_element_by_css_selector("[name='firstname']")
    first_name.send_keys("some_text")

    last_name = driver.find_element_by_css_selector("[name='lastname']")
    last_name.send_keys("some_new_text")

    email = driver.find_element_by_css_selector("[name='email']")
    email.send_keys("some@mail.com")

    upload_btn = driver.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname("sample.txt"))
    file_path = os.path.join(current_dir, "sample.txt")
    upload_btn.send_keys(file_path)

    submit_btn = driver.find_element_by_css_selector(".btn")
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()