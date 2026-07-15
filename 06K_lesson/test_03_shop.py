import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.firefox
def test_shop(firefox_driver):
    wait = WebDriverWait(firefox_driver, 10)
    url = "https://www.saucedemo.com/"
    firefox_driver.get(url)
    username = firefox_driver.find_element(By.NAME, "user-name")
    username.clear()
    username.send_keys("standard_user")
    password = firefox_driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys("secret_sauce")
    firefox_driver.find_element(By.NAME, "login-button").click()
    wait.until(
        EC.element_to_be_clickable(
            (By.NAME, "add-to-cart-sauce-labs-backpack")
        )
    ).click()
    wait.until(
        EC.element_to_be_clickable(
            (By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
        )
    ).click()
    wait.until(
        EC.element_to_be_clickable((By.NAME, "add-to-cart-sauce-labs-onesie"))
    ).click()
    cart_badge = firefox_driver.find_element(
        By.CSS_SELECTOR, ".shopping_cart_badge"
    )
    assert cart_badge.text == "3", f"В корзине {cart_badge.text}, ожидалось 3"
    firefox_driver.find_element(
        By.CSS_SELECTOR, ".shopping_cart_link"
    ).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))).click()
    first_name = firefox_driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.clear()
    first_name.send_keys("Елена")
    last_name = firefox_driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.clear()
    last_name.send_keys("Сурина")
    zip_code = firefox_driver.find_element(By.CSS_SELECTOR, "#postal-code")
    zip_code.clear()
    zip_code.send_keys("141191")
    firefox_driver.find_element(By.CSS_SELECTOR, "#continue").click()
    total = firefox_driver.find_element(
        By.CSS_SELECTOR, ".summary_total_label"
    ).text

    assert total == "Total: $58.29", f"Неверная сумма: {total}"
