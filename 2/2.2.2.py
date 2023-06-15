from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    # print(x)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.find_element(By.ID, 'robotsRule').click()
    button.click()


finally:
    time.sleep(10)
    browser.quit()
