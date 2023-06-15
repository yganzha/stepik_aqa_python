from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"


try:
    driver = webdriver.Chrome()
    driver.get(link)

    link = driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input1 = driver.find_element(By.XPATH, '/html/body/div/form/div[1]/input')
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.XPATH, '/html/body/div/form/div[2]/input')
    input2.send_keys("Petrko")
    input3 = driver.find_element(By.XPATH, '/html/body/div/form/div[3]/input')
    input3.send_keys("Uzhgorord")
    input4 = driver.find_element(By.XPATH, '/html/body/div/form/div[4]/input')
    input4.send_keys("UA")
    button = driver.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(18)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
