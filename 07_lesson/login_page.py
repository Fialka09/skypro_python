from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self):
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
