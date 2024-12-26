# import time
# from selenium import  webdriver
# from selenium.webdriver.common.by import By

# opt = webdriver.ChromeOptions()
# opt.add_experimental_option('detach',True)
# driver = webdriver.Chrome(options=opt)

# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# driver.maximize_window()

# driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('Admin')
# driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin123')
# driver.find_element(By.XPATH, '//button[@type="submit"]').click()
import pytest
from pages.login import Login

@pytest.mark.parametrize('username, password', [('Admin', 'admin123')])
def test_login(username, password):
    login = Login()
    login.navigate_to_login_page()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()