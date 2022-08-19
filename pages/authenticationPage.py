from selenium.webdriver.common.by import By
from pages.basicPage import BasicPage
from pages.myAccountPage import MyAccountPage


class AuthenticationPage(BasicPage):
    locator_dictionary = {"mail": (By.ID, "email"),
                          "passwd": (By.ID, "passwd"),
                          "icon_lock": (By.CLASS_NAME, "icon-lock"),
                          "alert": (By.CLASS_NAME, "alert"),
                          "forget_passwd": (By.XPATH, '//a[text()="Forgot your password?"]'),
                          "page_sub": (By.CLASS_NAME, "page-subheading")
                          }

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, mail: str, passwd: str):
        self._driver.find_element(*self.locator_dictionary["mail"]).send_keys(mail)
        self._driver.find_element(*self.locator_dictionary["passwd"]).send_keys(passwd)
        self._driver.find_element(By.CLASS_NAME, "icon_lock").click()
        return MyAccountPage(self._driver)

    def error(self):
        txt = self._driver.find_element(*self.locator_dictionary["alert"]).text
        return txt

    def forget_the_passwd(self):
        self._driver.find_element(*self.locator_dictionary["forget_passwd"]).click()
        message_forget_passwd = self._driver.find_element(*self.locator_dictionary["page_sub"]).text
        return message_forget_passwd
