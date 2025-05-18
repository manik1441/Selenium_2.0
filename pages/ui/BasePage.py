import pytest, logging
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from config import config


class BasePage:

    def __init__(self):
        self.driver = pytest.driver
        self.timeout = config.TIMEOUT
        self.logger = logging.getLogger(self.__class__.__name__)

    def wait_element(self, locator,timeout=None):
        timeout = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    
    def navigate(self, url):
        self.driver.get(url)

    def send_keys(self, locator, text):
       element =  self.wait_element(locator)
       element.clear()
       element.send_keys(text)

    def click(self, locator):
        element = self.wait_element(locator)
        element.click()

    def get_text(self, locator):
        element = self.wait_element(locator)
        return element.text

    def is_visible(self, locator, timeout=None):
        try:
            return self.wait_element(locator,timeout).is_displayed()
        except Exception as e:
            self.log(f'Error in getting locator - {e}', 'error')
            return False

    def log(self, msg, level='info'):
        if level == 'error':
            self.logger.error(msg)
        elif level == 'warning':
            self.logger.warning(msg)
        else:
            self.logger.info(msg)