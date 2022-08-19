from selenium.webdriver.common.by import By
from pages.basicPage import BasicPage
from pages.itemPage import ItemPage


class SearchPage (BasicPage):

    def __init__(self, driver):
        super().__init__(driver)

    locator_dictionary = {
        "product_container": (By.CLASS_NAME, "product-container"),
        "product_name": (By.CLASS_NAME, "product-name"),
        "right_block": (By.CLASS_NAME, "right-block"),
        "content_price": (By.CLASS_NAME, "content_price"),
        "price": (By.CLASS_NAME, "price"),
        "add_to_cart": (By.CLASS_NAME, "button.ajax_add_to_cart_button.btn.btn-default")
    }

    def choosing_the_cheapest_product(self):
        product_containers = self._driver.find_elements(*self.locator_dictionary["product_container"])
        mini_price = 123
        mini_product_container = product_containers
        for product_container in product_containers:
            right_block = product_container.find_element(*self.locator_dictionary["right_block"])
            content_price = right_block.find_element(*self.locator_dictionary["content_price"])
            price = content_price.find_element(*self.locator_dictionary["price"]).text
            num_of_price = float(price[1:len(price)])
            if mini_price > num_of_price:
                mini_price = num_of_price
                mini_product_container = product_container
        right_block = mini_product_container.find_element(*self.locator_dictionary["right_block"])
        right_block.find_element(*self.locator_dictionary["product_name"]).click()
        return ItemPage(self._driver)
