import pytest
from pages.ui.LoginPage import Login

@pytest.mark.parametrize('username, password', [ ('Admin', 'admin123'),
                                                ('Admin', 'admin1234'),
                                                ('Admin', 'admin1232')
                                                ])
def test_login(username, password):
    login = Login()
    login.navigate_to_login_page()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()
    assert login.validate_login()