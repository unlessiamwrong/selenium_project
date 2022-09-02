import time

import pytest

from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail(reason='known bug')),
                                  8, 9])
def test_guest_can_add_product_to_cart(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    item_name = page.get_item_name()
    item_price = page.get_item_price()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_equal_names_and_prices(item_name, item_price)


@pytest.mark.xfail(reason="known bug")
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="known bug")
def test_message_disappeared_after_adding_product_to_cart(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = ProductPage(browser, browser.current_url)
    login_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    page = CartPage(browser, link)
    page.should_be_no_items_in_cart()
    page.should_be_empty_message_in_cart()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.browser = browser
        self.page = LoginPage(browser=browser, url=link)
        self.page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "fakepassword"
        self.page.register_new_user(email=email, password=password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        self.link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        self.link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer1"
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.should_be_add_to_cart_button()
        self.item_name = self.page.get_item_name()
        self.item_price = self.page.get_item_price()
        self.page.add_item_to_cart()
        self.page.solve_quiz_and_get_code()
        self.page.should_be_equal_names_and_prices(self.item_name, self.item_price)
