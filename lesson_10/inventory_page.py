import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InventoryPage:
    """
    Страница товаров магазина Saucedemo
    Добавление товаров в корзину
    """

    ITEMS = {
        "backpack": "add-to-cart-sauce-labs-backpack",
        "t-shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
        "onesie": "add-to-cart-sauce-labs-onesie",
    }

    def __init__(self, driver):
        """
        Конструктор страницы товаров.
        :param driver: WebDriver (Chrome, Edge, Firefox)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить товар в корзину")
    def add_item(self, item_name):
        """
        Найти товар по id и добавить его в корзину.
        :param item_name: Ключ из словаря ITEMS
        ("backpack", "t-shirt", "onesie")
        """
        self.wait.until(
            EC.element_to_be_clickable((By.ID, self.ITEMS[item_name]))
        ).click()

    @allure.step("Добавить все товары в корзину")
    def add_all_items(self):
        """Добавляет каждый товар из списка в корзину по id"""
        for item in self.ITEMS:
            print(item)
            self.add_item(item)

    @allure.step("Перейти на страницу корзины нажав на значок корзины ")
    def go_to_cart(self):
        """
        После нажатия на значок корзины
        открылась страница корзины с добавленными товарами
        """
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link"
        ).click()

    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self):
        """
        Вернуть количество товаров в корзине.
        :return: Строка с числом товаров (например, "3")
        """
        return self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_badge"
        ).text
