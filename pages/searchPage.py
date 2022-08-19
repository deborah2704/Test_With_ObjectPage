import time
from pages.basicPage import BasicPage
from pages.itemPage import ItemPage


class SearchPage(BasicPage):

    locator_dictionary = {
        "product_container": ".product-container",
        "product_name": ".product-name",
        "right_block": ".right-block",
        "content_price": ".content_price",
        "price": ".price",
        "add_to_cart": ".button.ajax_add_to_cart_button.btn.btn-default"
    }

    def __init__(self, page):
        super().__init__(page)

    def choosing_the_cheapest_product(self):
        product_containers = self._page.query_selector_all(self.locator_dictionary["product_container"])
        mini_price = 123
        mini_product_container = product_containers
        for product_container in product_containers:
            right_block = product_container.query_selector(self.locator_dictionary["right_block"])
            content_price = right_block.query_selector(self.locator_dictionary["content_price"])
            price = content_price.query_selector(self.locator_dictionary["price"]).text_content()
            price_num = float(price.replace("$", ""))
            if mini_price > price_num:
                mini_price = price_num
                mini_product_container = product_container
        right_block = mini_product_container.query_selector(self.locator_dictionary["right_block"])
        right_block.query_selector(self.locator_dictionary["product_name"]).click()
        return ItemPage(self._page)
