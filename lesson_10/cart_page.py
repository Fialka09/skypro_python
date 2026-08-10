import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage:
    """
    Страница корзины магазина Saucedemo.
    Оформление заказа
    """

    def __init__(self, driver):
        """
        Конструктор страницы корзины
        :param driver: WebDriver (Chrome, Edge, Firefox)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step(
        "Нажать на кнопку 'Checkout' и проверить, что URL страницы изменился"
    )
    def checkout(self):
        """После нажатия на кнопку 'Checkout' URL страницы поменялся"""
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
        ).click()
        self.wait.until(EC.url_contains("checkout-step-one"))
