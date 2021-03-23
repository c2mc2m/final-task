from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        mail = self.get_element(*LoginPageLocators.REGISTER_EMAIL)
        mail.send_keys(email)
        pass1 = self.get_element(*LoginPageLocators.REGISTER_PASSWORD1)
        pass1.send_keys(password)
        pass2 = self.get_element(*LoginPageLocators.REGISTER_PASSWORD2)
        pass2.send_keys(password)
        submit_registration = self.get_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit_registration.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "There is no login form on this page"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_required_url("login"), "The current url is not login url"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "There is no registration form on this page"    
