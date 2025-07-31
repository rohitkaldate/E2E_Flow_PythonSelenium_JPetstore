import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://petstore.octoperf.com/")
print(driver.title)
print(driver.current_url)

driver.find_element(By.LINK_TEXT,"Enter the Store").click()
driver.find_element(By.LINK_TEXT,"Sign In").click()
driver.find_element(By.NAME,"username").send_keys("j2ee")
driver.find_element(By.NAME,"password").clear()
driver.find_element(By.NAME,"password").send_keys("j2ee")
driver.find_element(By.NAME,"signon").click()
time.sleep(5)
msg = driver.find_element(By.ID,"WelcomeContent").text
assert "Welcome" in msg

driver.find_element(By.XPATH,"//div[@id='QuickLinks']/a[1]").click()
test = driver.find_element(By.TAG_NAME,"h2").text
assert "Fish" in test
driver.find_element(By.LINK_TEXT,"FI-SW-01").click()
#Choose Product
driver.find_element(By.LINK_TEXT,"EST-1").click()

#Add to cart
driver.find_element(By.CSS_SELECTOR,".Button").click()
#CHeckout
driver.find_element(By.LINK_TEXT,"Proceed to Checkout").click()
#Continue
driver.find_element(By.XPATH,"//input[@value='Continue']").click()
#COnfirmation
driver.find_element(By.LINK_TEXT,"Confirm").click()
res =  driver.find_element(By.CSS_SELECTOR,"div ul[class='messages']").text
assert "Thank you" in res
#Logout
driver.find_element(By.LINK_TEXT,"Sign Out").click()


