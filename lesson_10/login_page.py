import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    """
    Страница входа в магазин Saucedemo.
    Открывает страницу и выполняет авторизацию.
    """

    URL = "https://www.saucedemo.com/"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    def __init__(self, driver):
        """
        Конструктор страницы входа.
        :param driver: WebDriver (Chrome, Edge, Firefox)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу входа")
    def open(self):
        """Открыть страницу магазина Saucedemo."""
        self.driver.get(self.URL)

    @allure.step(
        f"Ввод логина {USERNAME} и пароля {PASSWORD}, нажать на кнопку 'Login'"
    )
    def login(self):
        """Очистить поля, ввести логин и пароль, нажать на кнопку 'Login'"""
        user_name = self.wait.until(
            EC.presence_of_element_located((By.NAME, "user-name"))
        )
        user_name.clear()
        user_name.send_keys(self.USERNAME)

        password = self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password.clear()
        password.send_keys(self.PASSWORD)

        self.wait.until(
            EC.element_to_be_clickable((By.NAME, "login-button"))
        ).click()
        self.wait.until(EC.url_contains("inventory"))
