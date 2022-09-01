from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login is not presented in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login Username field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login Password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login Submit button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register Email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD1), \
            "Register Password1 field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD2), \
            "Register Password2 field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUBMIT), "Register Submit button is not presented"