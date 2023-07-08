import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(3)
    btn_text = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text
    assert btn_text != None, "страница товара на сайте НЕ содержит кнопку добавления в корзину"
