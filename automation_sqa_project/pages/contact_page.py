from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage:
    # ---------------------------------------------------------
    # 1. LOCATORS
    # ---------------------------------------------------------
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='email']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "input[data-qa='subject']")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "textarea[data-qa='message']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    SUCCESS_MSG = (By.XPATH, "//div[contains(text(), 'Success! Your details have been submitted successfully.')]")

    # ---------------------------------------------------------
    # 2. INITIALIZATION
    # ---------------------------------------------------------
    def __init__(self, driver):
        self.driver = driver

    # ---------------------------------------------------------
    # 3. ACTIONS
    # ---------------------------------------------------------
    def navigate(self):
        self.driver.get("https://automationexercise.com/contact_us")

    def submit_support_ticket(self, name, email, subject, message):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.SUBJECT_INPUT).send_keys(subject)
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(message)
        
        # Click the submit button
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        
        # PRO TIP: Handling JavaScript Browser Alerts
        # The site throws a standard "Are you sure?" browser popup. We must accept it!
        wait = WebDriverWait(self.driver, 5)
        alert = wait.until(EC.alert_is_present())
        alert.accept()

    def is_ticket_successful(self):
        """Checks if the green success message is displayed."""
        wait = WebDriverWait(self.driver, 5)
        success = wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG))
        return success.is_displayed()
