from selenium.webdriver.common.by import By

class LoginLocators():
    USERNAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOGIN = (By.XPATH, '//button[@type="submit"]')