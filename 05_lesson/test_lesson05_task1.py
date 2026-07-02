from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def test_navigation():
    driver = webdriver.Chrome()

    for _ in range(3):
        try:
            driver.get("https://httpbin.org/")
            driver.find_element(By.PARTIAL_LINK_TEXT, "HTML").click()
            assert "/forms/post" in driver.current_url

            driver.back()
            assert "httpbin.org" in driver.current_url
            assert "/forms/post" not in driver.current_url
            break
        except NoSuchElementException:
            sleep(2)

    driver.quit()
