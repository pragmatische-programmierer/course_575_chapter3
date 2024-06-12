import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestProductPage:
    def test_guest_should_see_add_button(self, browser):
        browser.get(link)
        button = browser.find_element(By.CSS_SELECTOR, "form#add_to_basket_form button[type='submit']")
        assert button.is_enabled(), \
            f"Button \"Add to basket\" not exist at page: {link}"
