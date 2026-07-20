import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def press(driver, key):
    """Нажимает кнопку на калькуляторе по тексту."""
    driver.find_element(By.XPATH, f'//span[text()="{key}"]').click()


@pytest.mark.chrome
# тест для браузера Chrome
def test_calc(chrome_driver):
    wait = WebDriverWait(chrome_driver, 51)
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    chrome_driver.get(url)

    delay = chrome_driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")

    press(chrome_driver, "7")
    press(chrome_driver, "+")
    press(chrome_driver, "8")
    press(chrome_driver, "=")

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
        )
    )
    result = chrome_driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15", f"Ожидалось 15, получено {result}"
