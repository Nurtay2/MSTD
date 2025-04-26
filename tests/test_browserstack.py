from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def run_test(browser_name, test_name):
    bstack_options = {
        "os": "MacOS",
        "osVersion": "10",
        "sessionName": test_name,
        "buildName": "Test HW2",
        "userName": "nurtay_8bv3fB",
        "accessKey": "cL1KC79st7omn3NyQPU9"
    }

    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
    elif browser_name.lower() == "safari":
        options = webdriver.SafariOptions()
        bstack_options["os"] = "OS X"
        bstack_options["osVersion"] = "Monterey"
    else:
        raise Exception("Browser not supported")

    options.set_capability("browserVersion", "latest")
    options.set_capability("bstack:options", bstack_options)

    driver = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    try:
        if test_name == "Test 1":
            driver.get("https://example.com")
            heading = driver.find_element(By.TAG_NAME, "h1")
            assert heading.is_displayed()

        elif test_name == "Test 2":
            driver.get("https://example.com")
            paragraph = driver.find_element(By.TAG_NAME, "p")
            assert "illustrative" in paragraph.text.lower()

        # Вывод ссылки в конце теста
        print(f"Test completed. Final URL: {driver.current_url}")

    finally:
        driver.quit()


browsers = ["Chrome", "Firefox", "Safari"]
tests = ["Test 1", "Test 2"]

for browser in browsers:
    for test in tests:
        print(f"Running {test} on {browser}...")
        run_test(browser, test)
