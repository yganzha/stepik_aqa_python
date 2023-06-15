from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    x = "YanaG"
    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys(x)
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys(x)
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys(x)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    time.sleep(1)
    button.click()


finally:
    time.sleep(10)
    browser.quit()
