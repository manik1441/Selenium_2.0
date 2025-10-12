from selenium import webdriver
class WebDriverFactory:


    def get_webdriver(self, request):
        browser = request.config.getoption("browser")
        headless = request.config.getoption("headless", default=False)
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            # options.add_argument("--incognito")
            if headless:
                options.add_argument('--headless=new')
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

    def get_webdriver_grid(self, browser):
        hub_url = "http://localhost:5555/wd/hub"
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_experimental_option('detach', True)
            driver = webdriver.Remote(command_executor=hub_url, options=options)
        elif browser == 'edge':
            options = webdriver.EdgeOptions()
            options.add_experimental_option('detach', True)
            driver = webdriver.Remote(command_executor=hub_url, options=options)
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            driver = webdriver.Remote(command_executor=hub_url, options=options)
        else:
            raise Exception(f'Browser {browser} is not supported.')
        driver.maximize_window()
        return driver
