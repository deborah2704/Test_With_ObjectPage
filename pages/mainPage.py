import time
from playwright.sync_api import Page
from pages.basicPage import BasicPage
from pages.searchPage import SearchPage
from pages.authenticationPage import AuthnticationPage


class Main_page(BasicPage):
    locator_dictionary = {"sing_in": "a.login",
                          "search_query_top": '#search_query_top',
                          "submit_search": 'button.button-search'
                          }

    def __init__(self, page):
        super().__init__(page)

    def sing_in(self):
        self._page.locator(self.locator_dictionary["sing_in"]).click()
        return AuthnticationPage(self._page)

    def search_summer(self, search_text):
        self._page.locator(self.locator_dictionary["search_query_top"]).fill(search_text)
        self._page.locator(self.locator_dictionary["submit_search"]).click()
        return SearchPage(self._page)
