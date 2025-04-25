import pytest
from playwright.sync_api import sync_playwright


def test_purchase_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # 1. Авторизация
        page.goto("https://www.saucedemo.com/")
        page.fill('input[data-test="username"]', "standard_user")
        page.fill('input[data-test="password"]', "secret_sauce")
        page.click('input[data-test="login-button"]')

        # 2. Выбор товара
        page.click('a[id="item_4_title_link"]')  # Sauce Labs Backpack
        page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')

        # 3. Переход в корзину
        page.click('a[class="shopping_cart_link"]')
        assert page.locator('.inventory_item_name').inner_text() == "Sauce Labs Backpack"

        # 4. Оформление заказа
        page.click('button[data-test="checkout"]')
        page.fill('input[data-test="firstName"]', "John")
        page.fill('input[data-test="lastName"]', "Doe")
        page.fill('input[data-test="postalCode"]', "12345")
        page.click('input[data-test="continue"]')
        page.click('button[data-test="finish"]')

        # 5. Проверка успешной покупки
        assert page.locator('h2.complete-header').inner_text() == "Thank you for your order!"

        browser.close()