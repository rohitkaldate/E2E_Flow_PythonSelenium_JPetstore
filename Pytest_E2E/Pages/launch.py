class Launch:
    def __init__(self, driver):
        self.driver = driver

    def launch(self):
        self.driver.get("https://petstore.octoperf.com/")
        print(self.driver.title)
        print(self.driver.current_url)
