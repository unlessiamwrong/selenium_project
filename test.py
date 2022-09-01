from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    browser = webdriver.Chrome()
    browser.get(link)
    element = browser.find_element(By.CSS_SELECTOR, ".breadcrumb .active")
    name = element.text
    print(name)

finally:
    time.sleep(10)
    browser.quit()
