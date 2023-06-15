from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)


try:
    n1 = int(browser.find_element(By.ID, 'num1').text)
    n2 = int(browser.find_element(By.ID, 'num2').text)
    r = str(n1 + n2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(r)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
