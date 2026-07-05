from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_form_interaction():
    driver = webdriver.Chrome()
    for _ in range(3):
        try:
            driver.get("https://httpbin.org/forms/post")
            sleep(5)
            input_customer_name = driver.find_element(By.NAME, "custname")
            input_customer_name.send_keys("Елена")
            submit_button = driver.find_element(
                By.XPATH, '//button[text()="Submit order"]'
            )
            submit_button.click()
            sleep(2)
            print("Текущий URL:", driver.current_url)
            assert "/post" in driver.current_url
            break
        except NoSuchElementException:
            sleep(2)

    driver.quit()
