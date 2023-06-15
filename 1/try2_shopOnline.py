from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    # подготовка для теста
    # открываем страницу первого товара
    # данный сайт не существует, этот код приведен только для примера
    browser.get("https://fake-shop.com/book1.html")

    # добавляем товар в корзину
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()

    # открываем страницу второго товара
    browser.get("https://fake-shop.com/book2.html")

    # добавляем товар в корзину
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()

    # тестовый сценарий
    # открываем корзину
    browser.get("https://fake-shop.com/basket.html")

    # ищем все добавленные товары
    goods = browser.find_elements(By.CSS_SELECTOR, ".good")

    # проверяем, что количество товаров равно 2
    assert len(goods) == 2

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(18)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла