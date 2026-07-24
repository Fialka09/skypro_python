from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckoutPage:
    USER_INFO = {
        "first-name": "Елена",
        "last-name": "Сурина",
        "postal-code": "141191",
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self):
        for field_id, value in self.USER_INFO.items():
            field = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, f"#{field_id}")
                )
            )
            field.clear()
            field.send_keys(value)

    def continue_order(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue"))
        ).click()
        self.wait.until(EC.url_contains("checkout-step-two"))

    def get_total(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label"
        ).text
