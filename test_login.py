from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()

# Open local HTML file
driver.get("file:///home/roronoa/Documents/selenium-login-test/login.html")

time.sleep(2)

# -------- TEST CASE 1: Valid Login --------
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.XPATH, "//button").click()

time.sleep(2)
print("Valid Login:", driver.find_element(By.ID, "message").text)

# -------- TEST CASE 2: Invalid Login --------
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()

driver.find_element(By.ID, "username").send_keys("user")
driver.find_element(By.ID, "password").send_keys("wrong")
driver.find_element(By.XPATH, "//button").click()

time.sleep(2)
print("Invalid Login:", driver.find_element(By.ID, "message").text)

# -------- TEST CASE 3: Empty Fields --------
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()

driver.find_element(By.XPATH, "//button").click()

time.sleep(2)
print("Empty Login:", driver.find_element(By.ID, "message").text)

driver.quit()
