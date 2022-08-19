import time
from selenium.webdriver.common.by import By
from pages.basicPage import BasicPage


class ItemPage(BasicPage):

    locator_dictionary = {
        "Sub": (By.ID, "add_to_cart"),
        "button1_proceed_to_checkout": (By.CSS_SELECTOR, "a.button-medium"),
        "button2_proceed_to_checkout": (By.CSS_SELECTOR, 'a[href="http://automationpractice.com/index.php?controller=order&step=1"]'),
        "name_process_address": (By.CSS_SELECTOR, '[name=processAddress]'),
        "checkbox": (By.CSS_SELECTOR, '[type=checkbox]'),
        "process_carrier": (By.CSS_SELECTOR, '[name=processCarrier]'),
        "bankwire": (By.CLASS_NAME, "bankwire"),
        "button_medium": (By.CSS_SELECTOR, "button.button-medium")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def completion_of_order(self):
        self._driver.find_element(*self.locator_dictionary["Sub"])[0].click()
        self._driver.find_element(*self.locator_dictionary["button1_proceed_to_checkout"]).click()
        self._driver.find_element(*self.locator_dictionary["button2_proceed_to_checkout"]).click()
        self._driver.find_element(*self.locator_dictionary["name_process_address"]).click()
        self._driver.find_element(*self.locator_dictionary["checkbox"]).click()
        self._driver.find_element(*self.locator_dictionary["process_carrier"]).click()
        self._driver.find_element(*self.locator_dictionary["bankwire"]).click()
        self._driver.find_element(*self.locator_dictionary["button_medium"]).click()
        time.sleep(3)
        return self._driver
