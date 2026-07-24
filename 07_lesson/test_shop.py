import pytest

from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage
from cart_page import CartPage


@pytest.mark.firefox
def test_shop(firefox_driver):
    login_page = LoginPage(firefox_driver)
    login_page.open()
    login_page.login()

    inventory_page = InventoryPage(firefox_driver)
    inventory_page.add_all_items()

    assert (
        inventory_page.get_cart_count() == "3"
    ), "В корзине должно быть 3 товара!"

    inventory_page.go_to_cart()

    cart_page = CartPage(firefox_driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(firefox_driver)
    checkout_page.fill_form()
    checkout_page.continue_order()

    total = checkout_page.get_total()
    assert "Total: $58.29" in total, f"Неверная сумма: {total}"
