import logging
import pytest
from playwright.sync_api import sync_playwright

from pages import mainPage

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


@pytest.fixture
def open_website():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://automationpractice.com/index.php")
        yield mainPage.Main_page(page)
        page.close()


def test_mail_is_empty(open_website):
    log.info("test mail is empty")
    main_page = open_website
    authntication_page = main_page.sing_in()
    authntication_page.login(" ", "deborah shoushana")
    alert = authntication_page.error()
    assert "the address mail is most to be complete !!" in alert


def test_password_is_empty(open_website):
    log.info("test password is empty")
    main_page = open_website
    authntication_page = main_page.Sing_in()
    authntication_page.login("deborah270401@gmail.com", "  ")
    alert = authntication_page.rror()
    assert "the password of address mail is most to be complete !!" in alert


def test_validation_of_mail(open_website):
    log.info("test validation of mail")
    main_page = open_website
    authntication_page = main_page.sing_in()
    authntication_page.login("blabla@gmail.com", "deborah shoushana")
    alert = authntication_page.error()
    assert "the address mail is not true !!" in alert


def test_validation_of_password(open_website):
    log.info("test validation of password")
    main_page = open_website
    authntication_page = main_page.sing_in()
    authntication_page.login("deborah270401@gmail.com", "blabla")
    alert = authntication_page.error()
    assert "the password of address mail is not true !!" in alert


def test_buy_dress_completion_order(open_website):
    main_page = open_website
    authntication_page = main_page.sing_in()
    myAccount_page = authntication_page.login("deborah270401@gmail.com", "deborah shoushana")
    main_page = myAccount_page.go_to_home_page()
    search_page = main_page.search_summer("summer")
    item_page = search_page.choosing_the_cheapest_product()
    complete_of_order = item_page.completion_of_order()
    complete = complete_of_order.locator(".cheque-indent").locator(".dark")
    assert "The order was successfully placed." in complete.inner_html()
