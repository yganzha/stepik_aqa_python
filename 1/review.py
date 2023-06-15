from selenium import webdriver
import time
from selenium.webdriver.common.by import By

links = ["http://suninjuly.github.io/registration1.html",
        "http://suninjuly.github.io/registration2.html"]

for link in links:
    try:
        print('Start test for: ', link)

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        first_name.send_keys('Hello')

        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        last_name.send_keys('My')

        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        email.send_keys('World')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

    finally:
        print('End test for: ', link)
        browser.quit()