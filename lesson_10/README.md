# Документация проекта — тесты магазина Saucedemo

## Описание

Проект использует:
- **Python** — основной язык
- **Selenium** — управление браузером
- **Pytest** — запуск тестов
- **Allure** — отчёты о тестировании
- **Page Object** — паттерн организации кода

### Форматирование кода

- Код соответствует PEP 8 (проверяется `flake8` и `black --line-length 79`)
- Все методы классов содержат docstring с `:param` и `:return`
- Шаги размечены через `@allure.step` в классах Page Object
- Тесты содержат `@allure.title`, `@allure.description`, `@allure.feature`, `@allure.severity`

---

## Структура тестов магазина

- `login_page.py` — страница входа
- `inventory_page.py` — страница товаров
- `cart_page.py` — страница корзины
- `checkout_page.py` — страница оформления заказа
- `test_shop.py` — тест полного цикла покупки

## Запуск тестов

```bash
python -m pytest lesson_10/test_shop.py -v 
```

## Запуск с Allure-отчётом
```bash
python -m pytest lesson_10/ --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Что видно в отчёте
Название теста: «Покупка трёх товаров в магазине Saucedemo»

Шаги: открытие, логин, добавление товаров, корзина, оформление, проверка суммы

Параметры товаров: рюкзак, футболка, комбинезон

Итоговая стоимость: $58.29