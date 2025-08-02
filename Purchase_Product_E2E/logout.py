from selenium.webdriver.common.by import By


class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.click_sidebar_button = (By.XPATH, "//button[@id='react-burger-menu-btn']")
        self.click_logout = (By.LINK_TEXT, "Logout")

    def click_sidebar(self):
        self.driver.find_element(*self.click_sidebar_button).click()

    def logout_application(self):
        self.driver.find_element(*self.click_logout).click()