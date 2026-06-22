from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.secure_page import SecurePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def open(self):
        super().open(self.URL)
        return self

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)
        return SecurePage(self.driver)

    def error_message(self):
        return self.text_of(self.FLASH)
