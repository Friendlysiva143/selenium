from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Initialize the WebDriver (Ensure 'chromedriver' is in your PATH)
driver = webdriver.Chrome()
try:
 # Open a website
 driver.get('https://www.python.org')
 # Find an element by its class name and print its text (Example: The main navigation bar)
 element = driver.find_element(By.CLASS_NAME, 'introduction')
 print('Text from the selected element:', element.text)
 # Interact with elements if needed (Example: Clicking a link)
 download_link = driver.find_element(By.LINK_TEXT, 'Downloads')
 download_link.click()
 # Wait for a few seconds to observe actions
 time.sleep(5)
finally:
 # Close the browser
 driver.quit()