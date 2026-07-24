from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InventoryPage:
    ITEMS = {
        "backpack": "add-to-cart-sauce-labs-backpack",
        "t-shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
        "onesie": "add-to-cart-sauce-labs-onesie",
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item(self, item_name):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, self.ITEMS[item_name]))
        ).click()

    def add_all_items(self):
        for item in self.ITEMS:
            self.add_item(item)

    def go_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link"
        ).click()

    def get_cart_count(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_badge"
        ).text
