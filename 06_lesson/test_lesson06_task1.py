from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(
            "https://the-internet.herokuapp.com/dynamic_loading/2"
        )
        button_start = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[id='start'] button")
            )
        )
        button_start.click()
        text_h_w = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#finish h4')
            )
        )
        assert text_h_w.is_displayed()
        assert text_h_w.text == "Hello World!"
        driver.save_screenshot("screenshots/full_screen.png")
    finally:
        driver.quit()
