import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/")
print(driver.title)
print(driver.current_url)

#Login Details
# driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
# driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
# driver.find_element(By.XPATH,"//input[@id='login-button']").click()
# print(driver.find_element(By.XPATH,"//div[contains(text(),'Swag Labs')]").text)

##Get the multiple products and add to cart
# products = driver.find_elements(By.XPATH,"//div/div[@class='inventory_item']")
# print(len(products))
# for product in products:
#     item = product.find_element(By.XPATH,"//div/div[@class='inventory_item'][1]")
#     item.click()
#     print(item.text)
#     item.find_element(By.XPATH, "//div/div[2]/button[@id='add-to-cart']").click()
#
#     break
# driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()

#Go to cart
# driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
# print(driver.find_element(By.XPATH,"//div[@class='cart_item']").text)

# driver.find_element(By.ID,"checkout").click()

# print(driver.find_element(By.XPATH,"//span[@class='title']").text)
# driver.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Rohit")
# driver.find_element(By.CSS_SELECTOR,"#last-name").send_keys("Kaldate")
# driver.find_element(By.CSS_SELECTOR,"#postal-code").send_keys("123456")

# driver.find_element(By.NAME,"continue").click()
# msg =  driver.find_element(By.XPATH,"//span[@class='title']").text
# assert "Checkout" in msg
# print(driver.find_element(By.XPATH,"//div[@id='checkout_summary_container']").text)
#
# driver.find_element(By.NAME,"finish").click()

# print(driver.find_element(By.TAG_NAME,"h2").text)
# driver.find_element(By.ID,"back-to-products").click()
# driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
driver.find_element(By.LINK_TEXT,"Logout").click()





# driver.find_element(By.XPATH,"//button[@id='add-to-cart']").click()

# print(driver.find_element(By.XPATH,"//div[@class='inventory_details_desc_container']/div[1]").text)
# driver.find_element(By.XPATH,"//button[@id='add-to-cart']").click()

driver.quit()









