from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = 'nurtay_8bv3fB'
ACCESS_KEY = 'cL1KC79st7omn3NyQPU9'
URL = f'https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'

# Create a Firefox Options object
options = Options()
options.set_capability('browserstack.debug', True)
options.set_capability('name', 'Test Wikipedia Search')
options.set_capability('build', 'Homework Build')
options.set_capability('browser', 'Firefox')
options.set_capability('browser_version', 'latest')
options.set_capability('os', 'Windows')
options.set_capability('os_version', '10')

# Start the remote WebDriver
driver = webdriver.Remote(
    command_executor=URL,
    options=options  # Use 'options' here instead of 'capabilities'
)

# Perform the search on Wikipedia
driver.get("https://www.wikipedia.org")
search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Selenium (software)")
search_box.send_keys(Keys.RETURN)

# Better wait
WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))
assert "Selenium" in driver.title

# Quit the driver
driver.quit()
