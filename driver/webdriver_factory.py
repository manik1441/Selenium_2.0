from selenium import webdriver

class WebDriverFactory():
    def __init__(self):
        self.browser ='chrome'

    def get_webdriver(self):
        if self.browser == 'chrome':
            options = webdriver.ChromeOptions()
            # options.add_argument("--incognito")
            driver = webdriver. Chrome (options=options)
        elif self.browser == 'ie':
            driver = webdriver.Firefox()
        else:
            raise Exception(f'Browser {self.browser} is not supported.')
        driver.maximize_window()
        return driver