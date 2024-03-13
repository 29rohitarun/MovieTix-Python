from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                      options=options)

driver.get("https://www.fandango.com/")

# Wait for the user to click on a specific link or button that leads to the desired webpage
# For example, you can wait for the user to click on a movie link
wait = WebDriverWait(driver, 10)
movie_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="movie_link"]')))
movie_link.click()

# Once the user is on the specific webpage, wait for it to fully render
# (Assuming the webpage has a specific element you can wait for)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="desired_element"]')))

links = driver.find_elements(By.XPATH, '//button[text()="]')

'''
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome driver
driver = webdriver.Chrome()
driver.get('https://www.fandango.com/')

# Simulate user interactions to navigate to the checkout page
# Example: Click on a movie, select tickets, proceed to checkout, etc.

# Once you reach the checkout page, wait for it to fully render
# (Assuming the checkout page has a specific element you can wait for)
wait = WebDriverWait(driver, 10)
checkout_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_button"]')))

# Get the page source after JavaScript execution
page_source = driver.page_source

# Close the driver
driver.quit()

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

print("printing")
print(soup)

'''