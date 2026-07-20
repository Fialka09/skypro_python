import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.edge
def test_form(edge_driver):
    wait = WebDriverWait(edge_driver, 10)
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    edge_driver.get(url)
    # First name  Иван
    first_name = edge_driver.find_element(
        By.CSS_SELECTOR, '[name="first-name"]'
    )
    first_name.clear()
    first_name.send_keys("Иван")
    # Last name  Петров
    last_name = edge_driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
    last_name.clear()
    last_name.send_keys("Петров")
    # Address  Ленина, 55-3
    address = edge_driver.find_element(By.CSS_SELECTOR, '[name="address"]')
    address.clear()
    address.send_keys("Ленина, 55-3")
    # Email  test@skypro.com
    email = edge_driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
    email.clear()
    email.send_keys("test@skypro.com")
    # Phone number  +7985899998787
    phone = edge_driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
    phone.clear()
    phone.send_keys("+7985899998787")
    # Zip code  *оставить пустым '[name="zip-code"]'
    # City  Москва
    city = edge_driver.find_element(By.CSS_SELECTOR, '[name="city"]')
    city.clear()
    city.send_keys("Москва")
    # Country  Россия
    country = edge_driver.find_element(By.CSS_SELECTOR, '[name="country"]')
    country.clear()
    country.send_keys("Россия")
    # Job position  QA
    job = edge_driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
    job.clear()
    job.send_keys("QA")
    # Company  SkyPro
    company = edge_driver.find_element(By.CSS_SELECTOR, '[name="company"]')
    company.clear()
    company.send_keys("SkyPro")
    # кнопка Submit .btn-outline-primary
    submit = edge_driver.find_element(By.CSS_SELECTOR, ".btn-outline-primary")
    submit.click()
    # alert-danger = красный
    # alert-success = зеленый
    # Проверка: почтовый индекс - красный
    zip_selector = "#zip-code.alert-danger"
    zip_code_field = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, zip_selector))
    )
    assert zip_code_field.is_displayed(), "Zip code не отображается!"
    # Проверка: остальные поля - зелёные
    green_field_ids = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]
    for field_id in green_field_ids:
        element = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f"#{field_id}.alert-success")
            )
        )
        assert element.is_displayed(), f"Поле {field_id} не отображается!"
