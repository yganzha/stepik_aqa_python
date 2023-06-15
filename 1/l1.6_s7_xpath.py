from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("miniME")

    browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()

