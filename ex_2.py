from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Set up the WebDriver (for Chrome in this case)
driver = webdriver.Chrome() # You can use webdriver.Firefox() for Firefox
# Open the Google homepage
driver.get("https://www.google.com")
# Find the search input element using its name attribute
search_box = driver.find_element("name", "q")
# Type a search query
search_box.send_keys("bapatla engineering college")
# Simulate hitting the Enter key
search_box.send_keys(Keys.RETURN)
# Pause to see the results
time.sleep(10)
# Capture the titles of search results
results = driver.find_elements("tag name", "h3") # Grab headers from search results
for idx, result in enumerate(results):
 print(f"Result {idx + 1}: {result.text}")
# Close the browser
driver.quit()