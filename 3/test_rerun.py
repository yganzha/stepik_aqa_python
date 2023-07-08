import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(5)
    btn_text = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text
    assert btn_text != None, "страница товара на сайте НЕ содержит кнопку добавления в корзину"
