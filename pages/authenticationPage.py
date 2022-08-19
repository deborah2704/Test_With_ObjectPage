import time
from playwright.async_api import Page
from pages.basicPage import BasicPage
from pages.myAccountPage import MyAccountPage


class AuthnticationPage(BasicPage):
    locator_dictionary = {"mail": "input#email",
                          "passwd": "input#passwd",
                          "icon_lock": "#SubmitLogin",
                          "alert": ".alert",
                          "forget_passwd": 'text=Forgot your password?',
                          "page_sub": ".page-subheading"
                          }

    def __init__(self, page: Page):
        super().__init__(page)

    def login(self, mail, passwd):
        self._page.locator(self.locator_dictionary["mail"]).fill(mail)
        self._page.locator(self.locator_dictionary["passwd"]).fill(passwd)
        self._page.locator(self.locator_dictionary["icon_lock"]).click()
        return MyAccountPage(self._page)

    def error(self):
        text = self._page.locator(self.locator_dictionary["alert"]).all_text_contents()
        return text[0]

    def forget_the_passwd(self):
        self._page.locator(self.locator_dictionary["forget_passwd"]).click()
        return self._page.title()
