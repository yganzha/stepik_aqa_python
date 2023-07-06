import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
#                                   "https://stepik.org/lesson/236896/step/1",
#                                   "https://stepik.org/lesson/236897/step/1",
#                                   "https://stepik.org/lesson/236898/step/1",
#                                   "https://stepik.org/lesson/236899/step/1",
#                                   "https://stepik.org/lesson/236903/step/1",
#                                   "https://stepik.org/lesson/236904/step/1",
#                                   "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser):
    answer = math.log(int(time.time()))
    print(answer)

    browser.implicitly_wait(15)
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    browser.find_element(By.ID, "ember33").click()

    browser.find_element(By.ID, 'id_login_email').send_keys("ganzhayai@ukr.net")
    browser.find_element(By.ID, 'id_login_password').send_keys("Love1234")
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(5)

    browser.find_element(By.CSS_SELECTOR, '[placeholder="Type your answer here..."]').send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    msg = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    time.sleep(15)

    assert "Correct!" == msg, print(msg)
