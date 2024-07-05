from selenium import webdriver

# Specify the path to your geckodriver executable
driver_path = "C:/Users/slava/Desktop/list_of_prices/geckodriver.exe"

# Initialize the Firefox WebDriver
driver = webdriver.Firefox()

# ... your code ...

# Don't forget to quit the driver when you're done
driver.quit()