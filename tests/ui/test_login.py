import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver).open()
    secure = login.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in secure.flash_message()

@pytest.mark.parametrize("username, password, expected", [
    ("wrong", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "wrong", "Your password is invalid!"),
])
def test_invalid_login(driver, username, password, expected):
    login = LoginPage(driver).open()
    login.login(username, password)
    assert expected in login.error_message()