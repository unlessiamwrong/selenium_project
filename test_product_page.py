import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.fixture
def book_coders_at_work_page_link():
    return "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.fixture
def book_coders_at_work_promo_page_link():
    return "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.fixture
def book_city_and_stars_page_link():
    return "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.xfail(reason="known bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, book_coders_at_work_page_link):
    link = book_coders_at_work_page_link
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, book_coders_at_work_page_link):
    link = book_coders_at_work_page_link
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="known bug")
def test_message_disappeared_after_adding_product_to_basket(browser, book_coders_at_work_page_link):
    link = book_coders_at_work_page_link
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser, book_city_and_stars_page_link):
    link = book_city_and_stars_page_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# --------------------------------need_review --------------------------------

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, book_city_and_stars_page_link):
    link = book_city_and_stars_page_link
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = ProductPage(browser, browser.current_url)
    login_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, book_city_and_stars_page_link):
    link = book_city_and_stars_page_link
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.should_be_no_items_in_basket()
    page.should_be_empty_message_in_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "fake_password"
        page.register_new_user(email, password)
        # page.should_be_authorized_user() -  not required in final tests

    def test_user_cant_see_success_message(self, browser, book_coders_at_work_page_link):
        link = book_coders_at_work_page_link
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, book_coders_at_work_promo_page_link):
        link = book_coders_at_work_promo_page_link
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        item_name = page.get_item_name()
        item_price = page.get_item_price()
        page.add_item_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_equal_names_and_prices(item_name, item_price)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, book_coders_at_work_promo_page_link):
    link = book_coders_at_work_promo_page_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    item_name = page.get_item_name()
    item_price = page.get_item_price()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_names_and_prices(item_name, item_price)
