from selenium import webdriver
from selenium.webdriver.common.by import By

# URL of the webpage to scrape
url = 'https://example.com'

# Path to the WebDriver executable (e.g., ChromeDriver)
driver_path = '/path/to/chromedriver'

# Create a new instance of the web browser
driver = webdriver.Chrome(executable_path=driver_path)

# Open the webpage
driver.get(url)

# Extract data (e.g., titles of articles)
titles = driver.find_elements(By.CSS_SELECTOR, 'h2.title')

# Print the extracted titles
for title in titles:
    print(title.text)

# Close the web browser
driver.quit()
