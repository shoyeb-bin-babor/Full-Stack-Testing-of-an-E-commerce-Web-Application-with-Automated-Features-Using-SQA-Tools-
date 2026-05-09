from selenium.webdriver.common.by import By

class LoginPage:
    # ---------------------------------------------------------
    # 1. LOCATORS (Where are the elements on the screen?)
    # AutomationExercise is great because they use 'data-qa' tags!
    # ---------------------------------------------------------
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    
    # We will look for this text to confirm a successful login
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(), 'Logged in as')]")

    # ---------------------------------------------------------
    # 2. INITIALIZATION (Hooking up the browser)
    # ---------------------------------------------------------
    def __init__(self, driver):
        self.driver = driver

    # ---------------------------------------------------------
    # 3. ACTIONS (What can a user do on this page?)
    # ---------------------------------------------------------
    def navigate(self):
        self.driver.get("https://automationexercise.com/login")

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        # This will return True if the "Logged in as" text is found on the screen
        elements = self.driver.find_elements(*self.LOGGED_IN_TEXT)
        return len(elements) > 0
