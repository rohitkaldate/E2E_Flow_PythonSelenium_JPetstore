from selenium.webdriver.common.by import By


class Confirmation:
    def __init__(self, driver):
        self.driver = driver
        self.confirmation_title = (By.XPATH, "//span[@class='title']")
        self.fname = (By.CSS_SELECTOR, "#first-name")
        self.lname = (By.CSS_SELECTOR, "#last-name")
        self.post_code = (By.CSS_SELECTOR, "#postal-code")
        self.continue_button = (By.NAME, "continue")
        self.check_confirmation = (By.XPATH, "//span[@class='title']")
        self.summary =  (By.XPATH, "//div[@id='checkout_summary_container']")
        self.finish = (By.NAME, "finish")
        self.thanks_text = (By.TAG_NAME, "h2")
        self.back_to_products = (By.ID, "back-to-products")

    def confirm_purchase_product(self,first_name,last_name,postal_code):
        print(self.driver.find_element(*self.confirmation_title).text)
        self.driver.find_element(*self.fname).send_keys(first_name)
        self.driver.find_element(*self.lname).send_keys(last_name)
        self.driver.find_element(*self.post_code).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
        msg = self.driver.find_element(*self.check_confirmation).text
        assert "Checkout" in msg
        print(self.driver.find_element(*self.summary).text)
        self.driver.find_element(*self.finish).click()

    def go_back(self):
        print(self.driver.find_element(*self.thanks_text).text)
        self.driver.find_element(*self.back_to_products).click()