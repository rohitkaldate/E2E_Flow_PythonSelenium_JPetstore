from selenium.webdriver.common.by import By


class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.logout_button =  (By.LINK_TEXT, "Sign Out")

    def logout_application(self):
        self.driver.find_element(*self.logout_button).click()