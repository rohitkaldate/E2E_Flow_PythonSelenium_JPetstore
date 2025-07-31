from selenium.webdriver.common.by import By


class Product:
    def __init__(self,driver):
        self.driver = driver
        self.select_product = (By.XPATH, "//div[@id='QuickLinks']/a[1]")
        self.assertion = (By.TAG_NAME, "h2")
        self.choose_item = (By.LINK_TEXT, "FI-SW-01")
        self.choose_subitem = (By.LINK_TEXT, "EST-1")
        self.add_cart = (By.CSS_SELECTOR, ".Button")
        self.checkout = (By.LINK_TEXT, "Proceed to Checkout")


    def choose_product(self):
        self.driver.find_element(*self.select_product).click()
        test = self.driver.find_element(*self.assertion).text
        assert "Fish" in test
        self.driver.find_element(*self.choose_item).click()

    def add_to_cart_and_checkout(self):
        self.driver.find_element(*self.choose_subitem).click()
        self.driver.find_element(*self.add_cart).click()
        self.driver.find_element(*self.checkout).click()





