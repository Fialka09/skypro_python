import pytest
from string_utils import StringUtils

utils = StringUtils()


#                Тесты для capitalize

@pytest.mark.positive
def test_capitalize_russian():
    """Позитивный: русский текст — первая буква становится заглавной"""
    assert utils.capitalize("вперед") == "Вперед"


@pytest.mark.positive
def test_capitalize_english():
    """Позитивный: английский текст — первая буква заглавная"""
    assert utils.capitalize("go") == "Go"


@pytest.mark.positive
def test_capitalize_already_capital():
    """Позитивный: первая буква уже заглавная"""
    assert utils.capitalize("Great") == "Great"


@pytest.mark.positive
def test_capitalize_all_upper():
    """Позитивный: все буквы заглавные — остальные становятся строчными"""
    assert utils.capitalize("SKYPRO") == "Skypro"


@pytest.mark.negative
def test_capitalize_empty():
    """Негативный: пустая строка"""
    assert utils.capitalize("") == ""


@pytest.mark.negative
def test_capitalize_digits():
    """Негативный: строка из цифр"""
    assert utils.capitalize("5865") == "5865"


@pytest.mark.negative
def test_capitalize_symbols():
    """Негативный: строка из спецсимволов"""
    assert utils.capitalize("?*%") == "?*%"


@pytest.mark.negative
def test_capitalize_none():
    """Негативный: None вызывает ошибку"""
    with pytest.raises(AttributeError):
        utils.capitalize(None)  # type: ignore

#                  Тесты для trim


@pytest.mark.positive
def test_trim_one_space():
    """Позитивный: один пробел в начале удаляется"""
    assert utils.trim(" пробел") == "пробел"


@pytest.mark.positive
def test_trim_many_spaces():
    """Позитивный: много пробелов в начале - все удаляются"""
    assert utils.trim("              Много пробелов") == "Много пробелов"


@pytest.mark.positive
def test_trim_no_spaces():
    """Позитивный: нет пробелов в начале - строка не меняется"""
    assert utils.trim("без пробелов") == "без пробелов"


@pytest.mark.negative
def test_trim_empty():
    """Негатиывный: ввод пустой строки - пустая строка"""
    assert utils.trim("") == ""


@pytest.mark.negative
def test_trim_only_spaces():
    """Негативный: строка из пробелов - пустая строка"""
    assert utils.trim("      ") == ("")


#             Тесты для contains

@pytest.mark.positive
def test_contains_found_lowercase():
    """Позитивный: строчная буква найдена — возвращает True"""
    assert utils.contains("практика", "а")


@pytest.mark.positive
def test_contains_found_uppercase():
    """Позитивный: заглавная буква найдена — возвращает True"""
    assert utils.contains("Level", "L")


@pytest.mark.positive
def test_contains_found_digit():
    """Позитивный: цифра найдена - возвращает True"""
    assert utils.contains("9 марта", "9")


@pytest.mark.positive
def test_contains_found_substring():
    """Позитивный: подстрока найдена — возвращает True
    (баг: метод ищет подстроку, а не символ)"""
    assert utils.contains("SkyPro", "Pro")


@pytest.mark.negative
def test_contains_empty():
    """Негативный: пустая строка — возвращает False"""
    assert not utils.contains("", "а")


@pytest.mark.negative
def test_contains_case_sensitive():
    """Негативный: заглавная буква не найдена в строчной — возвращает False"""
    assert not utils.contains("Проверим регистр", "Р")


@pytest.mark.negative
def test_contains_none():
    """Негативный: None вызывает ошибку AttributeError"""
    with pytest.raises(AttributeError):
        utils.contains(None, "p")  # type: ignore

#        Тесты для delete_symbol


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("спорт", "п", "сорт"),
    (
        "Декоратор - инструмент для модификации",
        "-",
        "Декоратор  инструмент для модификации"
    ),
    ("Маркер — это функция", " ", "Маркер—этофункция"),
    ("Собственные маркировки", "в", "Собстенные маркироки"),
])
def test_delete_symbol_positive(string, symbol, expected):
    """Позитивные: символ удаляется из строки"""
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Модульное тестирование", "a", "Модульное тестирование"),
    ("2525 Библиотека", "Бил", "2525 Библиотека"),
])
def test_delete_symbol_negative(string, symbol, expected):
    """Негативные: символ не найден — строка не меняется"""
    assert utils.delete_symbol(string, symbol) == expected
