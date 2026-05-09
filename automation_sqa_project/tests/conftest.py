import pytest
import time
from selenium import webdriver

# A "fixture" is a setup function that runs before our tests.
@pytest.fixture(scope="function")
def driver():
    print("\n[Setup] Opening Google Chrome...")
    
    # 1. Initialize the browser
    # (Selenium Manager handles the chromedriver.exe for us!)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    
    # 2. Make it full screen and set a wait time
    driver.maximize_window()
    driver.implicitly_wait(10) # Tell Selenium to wait up to 10 seconds for elements to load
    
    # 3. Give the browser to our test case
    yield driver
    
    # 4. Close the browser after the test finishes
    print("\n[Teardown] Pausing for 10 seconds for video recording...")
    time.sleep(10)
    print("\n[Teardown] Closing Google Chrome...")
    driver.quit()
