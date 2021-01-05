from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR,".basket-mini .btn-group > a")

    @pytest.mark.sanity
    def test_sample_ui_test(self, browser):
        browser.get("https://meduza.io/")
        var = browser.find_element(By.CSS_SELECTOR,"a.Header-meduza")
        assert var.text in "Медуза. Перейти на главную страницу"
