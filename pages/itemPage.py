import time
from pages.basicPage import BasicPage


class ItemPage(BasicPage):
    locator_dictionary = {
        "Sub": "text='Add to cart'",
        "button1_proceed_to_checkout": "text='Proceed to checkout'",
        "button2_proceed_to_checkout": "#center_column >> text='Proceed to checkout'",
        "process_address": "button >> text='Proceed to checkout'",
        "checkbox": "input#cgv",
        "process_carrier": "button >> text='Proceed to checkout'",
        "bankwire": "text='Pay by bank wire'",
        "button_medium": "button >> text='I confirm my order'"
    }

    def __init__(self, page):
        super().__init__(page)

    def completion_of_order(self):
        self._page.locator(self.locator_dictionary["Sub"]).click()
        self._page.locator(self.locator_dictionary["button1_proceed_to_checkout"]).click()
        self._page.locator(self.locator_dictionary["button2_proceed_to_checkout"]).click()
        self._page.locator(self.locator_dictionary["process_address"]).click()
        self._page.locator(self.locator_dictionary["checkbox"]).click()
        self._page.locator(self.locator_dictionary["process_carrier"]).click()
        self._page.locator(self.locator_dictionary["bankwire"]).click()
        self._page.locator(self.locator_dictionary["button-medium"]).click()
        return self._page
