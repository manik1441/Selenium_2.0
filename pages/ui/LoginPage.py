from config import config
from locators.LoginLocator import LoginLocators
from pages.ui.BasePage import BasePage

class Login(BasePage):

    def navigate_to_login_page(self):
        self.navigate(config.ENVIRONMENT.get('url'))
        self.log("Navigated to URL.")

    def enter_username(self, value):
        self.send_keys(LoginLocators.USERNAME, value)
        self.log(f"Provided Username - {value}")

    def enter_password(self, value):
        self.send_keys(LoginLocators.PASSWORD, value)
        self.log(f"Provided Password")

    def click_login(self):
        self.click(LoginLocators.LOGIN)
        self.log('Clicked on Login button.')

    def validate_login(self):
        res = self.is_visible(LoginLocators.DASHBOARD,5)
        if res: self.log("Login successful.")
        return res