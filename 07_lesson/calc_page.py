from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(self.URL)

    def delay(self):
        delay = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay.clear()
        delay.send_keys("45")

    def press(self, key):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f'//span[text()="{key}"]'))
        ).click()

    def calculate(self):
        for key in ["7", "+", "8", "="]:
            self.press(key)

    def get_result(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
