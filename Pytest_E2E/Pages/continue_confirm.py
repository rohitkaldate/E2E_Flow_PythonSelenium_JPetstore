from selenium.webdriver.common.by import By


class Confirm:
    def __init__(self, driver):
        self.driver = driver
        self.continue_purchase = (By.XPATH,"//input[@value='Continue']")
        self.confirmation = (By.LINK_TEXT,"Confirm")
        self.ordered = (By.CSS_SELECTOR,"div ul[class='messages']")

    def order_product(self):
        self.driver.find_element(*self.continue_purchase).click()
        self.driver.find_element(*self.confirmation).click()
        res =  self.driver.find_element(*self.ordered).text
        assert "Thank you" in res
