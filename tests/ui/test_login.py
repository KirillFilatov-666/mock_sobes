import allure
import pytest
from pages.login_page import LoginPage


@allure.epic("Авторизация")
@allure.feature("Логин")
@allure.story("Успешный вход")
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_login(driver):
    with allure.step("Открыть страницу логина"):
        login = LoginPage(driver).open()
    with allure.step("Войти с валидными данными"):
        secure = login.login("tomsmith", "SuperSecretPassword!")
    with allure.step("Проверить сообщение об успехе"):
        assert "You logged into a secure area!" in secure.flash_message()


@allure.epic("Авторизация")
@allure.feature("Логин")
@allure.story("Невалидный вход")
@pytest.mark.parametrize("username, password, expected", [
    ("wrong", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "wrong", "Your password is invalid!"),
])
def test_invalid_login(driver, username, password, expected):
    login = LoginPage(driver).open()
    login.login(username, password)
    assert expected in login.error_message()