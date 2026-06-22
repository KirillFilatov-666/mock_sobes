from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SecurePage(BasePage):
    FLASH = (By.ID, "flash")

    def flash_message(self):
        return self.text_of(self.FLASH)
