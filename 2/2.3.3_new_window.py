from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    button = browser.find_element(By.CSS_SELECTOR, ".btn").click()
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()


finally:
    time.sleep(10)
    browser.quit()

