from playwright.sync_api import Page


class BasicPage(object):
    def __init__(self, page: Page):
        self._page = page
