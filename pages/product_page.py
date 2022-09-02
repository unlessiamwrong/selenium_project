from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), 'Add to cart button is not presented'

    def get_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return item_name

    def get_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        return item_price

    def add_item_to_cart(self):
        add_item_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_item_button.click()

    def should_be_equal_names_and_prices(self, item_name, item_price):
        self.should_be_same_book_name(item_name)
        self.should_be_same_price(item_price)

    def should_be_same_book_name(self, item_name):
        book_name = item_name
        assert self.is_element_present(*ProductPageLocators.ADDING_INFO), 'Success message is not presented'
        info_book_name = self.browser.find_element(*ProductPageLocators.ADDING_INFO).text
        assert book_name == info_book_name, 'Books names are not the same'

    def should_be_same_price(self, item_price):
        book_price = item_price
        assert self.is_element_present(*ProductPageLocators.CART_VALUE_INFO), 'Cart value message is not presented'
        info_cart_value = self.browser.find_element(*ProductPageLocators.CART_VALUE_INFO).text
        assert book_price == info_cart_value, 'Prices are not the same'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but didn't"