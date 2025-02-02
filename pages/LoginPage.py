from config.config import URL
from locators.LoginLocator import LoginLocators
from pages.BasePage import BasePage


class Login(BasePage):

    def navigate_to_login_page(self):
        self.navigate(URL().url())
        self.logger.info("Navigated to URL.")
        self.log("Navigated to URL.")

    def enter_username(self, value):
        self.send_keys(LoginLocators.USERNAME, value)

    def enter_password(self, value):
        self.send_keys(LoginLocators.PASSWORD, value)

    def click_login(self):
        self.click(LoginLocators.LOGIN)