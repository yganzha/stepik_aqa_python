import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_auth(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        last_name = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        email = browser.find_element(By.CSS_SELECTOR, "input.third:required")

        first_name.send_keys("miniME")
        last_name.send_keys("miniME")
        email.send_keys("miniME")

        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Congratulations text is present")



    def test_not_auth(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        last_name = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        email = browser.find_element(By.CSS_SELECTOR, "input.third:required")

        first_name.send_keys("miniME")
        last_name.send_keys("miniME")
        email.send_keys("miniME")

        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertNotEqual("Congratulations! You have successfully registered!", welcome_text, "Congratulations text is NOT present")


if __name__ == "__main__":
    unittest.main()
