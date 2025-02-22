from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

# Set up the webdriver (you'll need to specify the path to your chromedriver)
driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))

# Navigate to the login page
driver.get('https://portal.svkm.ac.in/usermgmt/login')

try:
    # Wait for the username field to be visible
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'userName'))
    )
    
    # Enter username
    username_field.send_keys('your username here') # Type your username here
    
    # Find and fill the password field
    password_field = driver.find_element(By.ID, 'userPwd')
    password_field.send_keys('your password here') # Type your password here
    
    # Find and click the login button
    login_button = driver.find_element(By.ID, 'userLogin')
    login_button.click()
    
    # Wait for successful login (e.g., by checking for an element on the next page)
    
    print("Login successful!")

    #This is a work around so that the chrome window doesn't close.
    input("Press Enter to close the browser.")
except Exception as e:
    print(f"An error occurred: {e}")

# Remove or comment out this line to keep the browser open
finally:
    driver.quit()
