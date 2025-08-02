import pytest
from selenium.webdriver.common.by import By


class AddToCart:
    def __init__(self, driver):
        self.driver = driver
        self.add_product = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        self.gocart = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.cart_item = (By.XPATH, "//div[@class='cart_item']")

    def add_to_cart_and_go_to_cart(self):
        self.driver.find_element(*self.add_product).click()
        self.driver.find_element(*self.gocart).click()

    @pytest.mark.skip
    def cart_item(self):
        print(self.driver.find_element(*self.cart_item).text)

