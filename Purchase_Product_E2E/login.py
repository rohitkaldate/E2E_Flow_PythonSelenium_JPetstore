from selenium.webdriver.common.by import By


class LoginApp:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.XPATH, "//input[@id='user-name']")
        self.password_add = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//input[@id='login-button']")
        self.title_text = (By.XPATH, "//div[contains(text(),'Swag Labs')]")

    def login_page(self,user,password):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password_add).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        print(self.driver.find_element(*self.title_text).text)