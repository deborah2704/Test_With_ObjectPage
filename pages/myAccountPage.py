from pages.basicPage import BasicPage
from pages.mainPage import Main_page


class MyAccountPage(BasicPage):

    locator_dictionary = {"home": ".icon-home",
                          "info_account": ".info-account"}

    def __init__(self, page):
        super().__init__(page)

    def go_to_home_page(self):
        self._page.locator(self.locator_dictionary["home"]).click()
        return Main_page(self._page)

    def validation(self):
        return self._page.locator(self.locator_dictionary["info_account"]).inner_html()
