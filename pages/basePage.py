import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass():

    def __init__(self):
        self.driver = pytest.driver
        self.timeout = 20

    def wait_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator))
    
    def navigate(self, url):
        self.driver.get(url)

    def send_keys(self, locator, text):
       element =  self.wait_element(locator)
       element.clear()
       element.send_keys(text)

    def click(self, locator):
        element = self.wait_element(locator)
        element.click()