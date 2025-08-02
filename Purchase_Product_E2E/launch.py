class LaunchPage:
    def __init__(self, driver):
        self.driver = driver

    def launch_webpage(self):
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.saucedemo.com/")
        print(self.driver.title)
        print(self.driver.current_url)
