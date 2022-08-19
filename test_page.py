import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from pages.mainPage import MainPage
from pages.basicPage import BasicPage

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrom_driver_path = "C:\selenium\chromedriver.exe"

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

my_address_mail = "deborah270401@gmail.com"
my_passwd = "deborah shoushana"
my_account = "deborah"


# start driver => mainPage
# mainPage click on singIn => authenticationPage
# authenticationPage.login ("user", "password") = myAccountPage
# myAccountPage.click home() = mainPage
# mainPage.search("summer") => searchPage


@pytest.fixture
def open_website():
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    # driver.get('https://www.google.com')
    driver.get('http://automationpractice.com/index.php')
    yield MainPage(driver)
    driver.quit()


def test_mail_is_empty(open_website):
    log.info("test mail is empty")
    main_page = open_website
    authentication_page = main_page.sing_in()
    authentication_page.login("", "deborah shoushana")
    alert = authentication_page.error()
    assert "the address mail is most to be complete !!" in alert


def test_password_is_empty(open_website):
    log.info("test password is empty")
    main_page = open_website
    authentication_page = main_page.sing_in()
    authentication_page.login("deborah270401@gmail.com", "")
    alert = authentication_page.error()
    assert "the password of address mail is most to be complete !!" in alert


def test_validation_of_mail(open_website):
    log.info("test validation of mail")
    main_page = open_website
    authentication_page = main_page.sing_in()
    authentication_page.login("blabla@gmail.com", "deborah shoushana")
    alert = authentication_page.error()
    assert "the address mail is not true !!" in alert


def test_validation_of_password(open_website):
    log.info("test validation of password")
    main_page = open_website
    authentication_page = main_page.sing_in()
    authentication_page.login("deborah270401@gmail.com", "blabla")
    alert = authentication_page.error()
    assert "the password of address mail is not true !!" in alert


def test_buy_dress_completion_order(open_website):
    log.info("test buy dress completion order")
    main_page = open_website
    authentication_page = main_page.sing_in()
    myAccount_page = authentication_page.login("deborah270401@gmail.com", "deborah shoushana")
    main_page = myAccount_page.go_to_home_page()
    search_page = main_page.search_summer("summer")
    item_page = search_page.choosing_the_cheapest_product()
    complete_of_order = item_page.completion_of_order()
    complete = complete_of_order.find_element(By.CLASS_NAME, "process_carrier").find_element(By.CLASS_NAME, "dark")
    assert "The order was successfully placed." in complete.text
