import pytest
import allure

from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage
from cart_page import CartPage


@allure.feature("Магазин")
@allure.story("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Покупка трёх товаров в магазине Saucedemo")
@allure.description("Тест проверяет полный цикл покупки")
@pytest.mark.firefox
def test_shop(firefox_driver):
    login_page = LoginPage(firefox_driver)
    with allure.step("Открыть страницу входа"):
        login_page.open()
    with allure.step("Ввод логина и пароля, нажать на кнопку 'Login'"):
        login_page.login()

    inventory_page = InventoryPage(firefox_driver)
    with allure.step("Добавить товары в корзину"):
        inventory_page.add_all_items()

    assert (
        inventory_page.get_cart_count() == "3"
    ), "В корзине должно быть 3 товара!"

    with allure.step("Перейти в корзину"):
        inventory_page.go_to_cart()

    cart_page = CartPage(firefox_driver)
    with allure.step("Нажать на кнопку 'Checkout'"):
        cart_page.checkout()

    checkout_page = CheckoutPage(firefox_driver)
    with allure.step("Заполнить поля данными пользователя"):
        checkout_page.fill_form()

    with allure.step("Нажать на кнопку 'Continue'"):
        checkout_page.continue_order()
    with allure.step("Получить итоговую стоимость корзины"):
        total = checkout_page.get_total()
    assert "Total: $58.29" in total, f"Неверная сумма: {total}"
