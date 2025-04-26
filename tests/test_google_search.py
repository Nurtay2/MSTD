from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = 'bsuser_dBuWYw'
ACCESS_KEY = '4UxP2jSKExcCDQmrN4zW'
URL = f'https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'

options = webdriver.ChromeOptions()
options.set_capability('browserstack.user', USERNAME)
options.set_capability('browserstack.key', ACCESS_KEY)
options.set_capability('os', 'OS X')
options.set_capability('os_version', 'Sonoma')
options.set_capability('browser', 'Safari')
options.set_capability('browser_version', 'latest')
options.set_capability('name', 'Test Google Search')
options.set_capability('build', 'Homework Build')

driver = webdriver.Remote(
    command_executor=URL,
    options=options
)

try:
    driver.get("https://www.google.com")

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("BrowserStack")
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
    )
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert any("BrowserStack" in r.text for r in results), "BrowserStack not found in results"

    print("Test passed successfully!")

finally:
    driver.quit()
