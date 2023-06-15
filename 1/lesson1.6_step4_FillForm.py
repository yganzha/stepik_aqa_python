from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element(By.XPATH, '/html/body/div/form/div[1]/input')
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.XPATH, '/html/body/div/form/div[2]/input')
    input2.send_keys("Petrko")
    input3 = driver.find_element(By.XPATH, '/html/body/div/form/div[3]/input')
    input3.send_keys("AAAAAAAAAAAAAAAA")
    input4 = driver.find_element(By.XPATH, '/html/body/div/form/div[4]/input')
    input4.send_keys("UA")
    button = driver.find_element(By.XPATH, '/html/body/div/form/div[6]/button[3]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
