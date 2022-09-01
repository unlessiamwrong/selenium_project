from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail(reason='known bug')),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    current_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, current_link)
    page.open()
    page.should_be_add_to_cart_button()
    item_name = page.get_item_name()
    item_price = page.get_item_price()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_equal_names_and_prices(item_name, item_price)
