from selenium import webdriver

""" check if driver executable 
use: sudo chmod +x {driver_name}
move/copy: sudo cp/mv {driver_name} /usr/local/bin """
browser = webdriver.Firefox() #browser should start if driver added to the /usr/local/bin directory

browser.get('https://stepik.org/lesson/25969/step/8')