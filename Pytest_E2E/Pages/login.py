from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.enter_store = (By.LINK_TEXT, "Enter the Store")
        self.signin = (By.LINK_TEXT, "Sign In")
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.click_login = (By.NAME, "signon")
        self.txt = (By.ID, "WelcomeContent")

    def login_details(self,username,password):
        self.driver.find_element(*self.enter_store).click()
        self.driver.find_element(*self.signin).click()
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.click_login).click()
        msg = self.driver.find_element(*self.txt).text
        assert "Welcome" in msg

