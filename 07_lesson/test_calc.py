import pytest
from calc_page import CalcPage


@pytest.mark.chrome
def test_calc_page(chrome_driver):
    calc_page = CalcPage(chrome_driver)
    calc_page.open()
    calc_page.delay()
    calc_page.calculate()
    result = calc_page.get_result()
    assert result == "15"
