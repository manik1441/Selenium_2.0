from config.config import URL
from locators.login import LoginLocators
from pages.basePage import BaseClass


class Login(BaseClass):

    def navigate_to_login_page(self):
        self.navigate(URL().url())

    def enter_username(self, value):
        self.send_keys(LoginLocators.USERNAME, value)

    def enter_password(self, value):
        self.send_keys(LoginLocators.PASSWORD, value)

    def click_login(self):
        self.click(LoginLocators.LOGIN)