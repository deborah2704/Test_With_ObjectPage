from pages.authenticationPage import AuthenticationPage
from pages.searchPage import *


class MainPage(BasicPage):
    locator_dictionary = {"sing_in": (By.CLASS_NAME, "login"),
                          "search_query_top": (By.ID, "search_query_top"),
                          "submit_search": (By.NAME, "submit_search")
                          }

    def __init__(self, driver):
        super().__init__(driver)

    def sing_in(self):
        self._driver.find_element(*self.locator_dictionary["sing_in"]).click()
        return AuthenticationPage(self._driver)

    def search_summer(self, search_query_top):
        self._driver.find_element(*self.locator_dictionary["search_query_top"]).send_keys(search_query_top)
        self._driver.find_element(By.NAME, "submit_search").click()
        return SearchPage(self._driver)
