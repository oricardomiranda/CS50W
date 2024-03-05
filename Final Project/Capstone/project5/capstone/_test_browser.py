from selenium import webdriver

# Instantiate a Firefox webdriver
driver = webdriver.Firefox()

# Navigate to the specified URL
driver.get('http://localhost:8000')

# Check if "WhoAmI" is present in the page source
assert driver.page_source.find('WhoAmI')

# Close the browser
driver.quit()
