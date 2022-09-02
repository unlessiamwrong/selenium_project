from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_no_items_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.ITEMS), \
            "Cart items are presented, but should not be"

    def should_be_empty_message_in_cart(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE), \
            'Empty cart message is not presented'
