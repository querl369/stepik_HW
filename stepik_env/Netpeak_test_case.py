'''1. Перейти по ссылке на главную страницу сайта Netpeak. (https://netpeak.ua/)
2. Перейдите на страницу "Работа в Netpeak",
нажав на кнопку "Карьера"
3. Перейти на страницу заполнения анкеты,
нажав кнопку - "Я хочу работать в Netpeak"
4. Загрузить файл с недопустимым форматом в блоке "Резюме",
например png, и проверить что на странице появилось сообщение,
о том что формат изображения неверный.
5. Заполнить случайными данными блок "3. Личные данные"
6. Нажать на кнопку отправить резюме
7. Проверить что сообщение на текущей странице  -
"Все поля являются обязательными для заполнения" -
подсветилось красным цветом
8. Нажать на логотип для перехода на главную страницу
и убедиться что открылась нужная страница.'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color

#Browser opening and main page load
driver = webdriver.Chrome()
driver.get('https://netpeak.ua/')
driver.implicitly_wait(1)
driver.maximize_window()
#going to career
career = driver.find_element_by_css_selector('#main-menu > ul > li.blog > a')
career.click()
driver.implicitly_wait(3)

#next to button "Я хочу работать в Netpeak"
want_btn = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[5]/div/a')
want_btn.click()

#uploading file, checking if error message appears
upload_file = driver.find_element_by_css_selector('body > input[type=file]')
upload_file.send_keys('/home/teamqa/Downloads/MzY0Nzg2OA.jpeg')
error_message = driver.find_element_by_css_selector('#up_file_name > label')
wait = WebDriverWait(driver, 3)
try:
    wait_for_err = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, error_message.text)))
except TimeoutException:
    pass

assert error_message.text == 'Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf).'

#"3. Личные данные" filling
name_field = driver.find_element_by_css_selector('#inputName')
name_field.send_keys('Testin')

surname_field = driver.find_element_by_css_selector('#inputLastname')
surname_field.send_keys('Man')

email_field = driver.find_element_by_css_selector('#inputEmail')
email_field.send_keys('123@123.com')

year_birth = driver.find_element_by_css_selector('#user-main-info > div:nth-child(11) > div:nth-child(3) > select')
year_birth.click()
year_birth.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)

month_birth = driver.find_element_by_css_selector('#user-main-info > div:nth-child(11) > div:nth-child(4) > select')
month_birth.click()
month_birth.send_keys(Keys.ARROW_DOWN + Keys.ENTER)

day_birth = driver.find_element_by_css_selector('#user-main-info > div:nth-child(11) > div.form-group.birthday-form.has-error > select')
day_birth.click()
day_birth.send_keys(Keys.ARROW_DOWN + Keys.ENTER )

phone_field = driver.find_element_by_css_selector('#inputPhone')
phone_field.send_keys('+380111111111')

#submiting form
submit_btn = driver.find_element_by_css_selector('#submit')
submit_btn.click()

#checking error message is red
red_color = Color.from_string('red')
all_field_color = Color.from_string(driver.find_element_by_xpath('/html/body/div[2]/div/p').value_of_css_property('color'))
assert all_field_color == red_color

#going to main page making sure it is main
main_page = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[1]/div[1]/a/img')
main_page.click()
driver.implicitly_wait(5)
main_page_sure = driver.find_element_by_xpath('//*[@id="subheader"]/div/div[1]/div[1]/div/div[1]/h1')
assert main_page_sure.text == 'Агентство интернет-маркетинга №1*'

driver.quit()
