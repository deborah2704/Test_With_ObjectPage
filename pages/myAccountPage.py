from selenium.webdriver.common.by import By
from pages.mainPage import *
from pages.basicPage import BasicPage


class MyAccountPage(BasicPage):

    locator_dictionary = {"home": (By.CLASS_NAME, "icon-home"),
                          "info_account": (By.CLASS_NAME, "info-account")}

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_home_page(self):
        self._driver.find_element(*self.locator_dictionary["home"]).click()
        return MainPage(self._driver)

    def validation(self):
        return self._driver.find_element(*self.locator_dictionary["info_account"]).text

