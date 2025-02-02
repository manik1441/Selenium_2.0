from selenium import webdriver

class WebDriverFactory:


    def get_webdriver(self, request):
        browser = request.config.getoption("browser")
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            # options.add_argument("--incognito")
            options.add_experimental_option('detach', True)
            driver = webdriver.Chrome(options=options)
        elif browser == 'edge':
            driver = webdriver.Edge()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        else:
            raise Exception(f'Browser {browser} is not supported.')
        driver.maximize_window()
        return driver