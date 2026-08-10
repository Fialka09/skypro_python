import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckoutPage:
    """
    Страница оформления заказа.
    Ввод данных пользователя (Имя, Фамилия, Индекс)
    """

    USER_INFO = {
        "first-name": "Елена",
        "last-name": "Сурина",
        "postal-code": "141191",
    }

    def __init__(self, driver):
        """
        Конструктор страницы оформления заказов.
        :param driver: WebDriver (Chrome, Edge, Firefox)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить поля данными пользователя")
    def fill_form(self):
        """Заполнить поля данными пользователя из USER_INFO."""
        for field_id, value in self.USER_INFO.items():
            field = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, f"#{field_id}")
                )
            )
            field.clear()
            field.send_keys(value)

    @allure.step("Нажать на кнопку 'Continue'")
    def continue_order(self):
        """Кнопка 'Continue' нажата и URL поменялся на "checkout-step-two" """
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue"))
        ).click()
        self.wait.until(EC.url_contains("checkout-step-two"))

    @allure.step("Получить итоговую стоимость корзины")
    def get_total(self):
        """Вернуть итоговую стоимость корзины.
        :return: Строка с итоговой стоимостью (например, "$58.29")
        """
        return self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label"
        ).text
