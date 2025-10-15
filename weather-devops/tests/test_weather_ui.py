from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open the web app
driver.get("http://localhost:5000")
time.sleep(2)

# Find the input and submit form
search_box = driver.find_element(By.NAME, "city")
search_box.send_keys("London")
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_btn.click()
time.sleep(3)

# Check if temperature text appears
assert "Temperature" in driver.page_source
print("✅ Weather Data Displayed Successfully!")

driver.quit()
