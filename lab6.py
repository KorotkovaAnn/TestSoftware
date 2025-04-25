import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_web():
    """Тестирование заказа на сайте saucedemo.com"""
    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").send_keys("standard_user")
    browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input").send_keys("secret_sauce")
    browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input").click()
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]/a/div").click()
    browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/button").click()
    time.sleep(1)

    browser.get("https://www.saucedemo.com/cart.html")
    browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[2]").click()
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input").send_keys("Anna")
    browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Korotkova")
    browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input").send_keys("727272")
    browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/input").click()
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]").click()
    time.sleep(1)

    text_element = browser.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]").text
    assert "Thank you for your order!" in text_element, "Текст об успешном заказе не найден на странице"
    print("Тест входа пройден успешно")

    browser.quit()