from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    # ---------------------------------------------------------
    # 1. LOCATORS
    # ---------------------------------------------------------
    CART_ITEMS = (By.CSS_SELECTOR, "tr[id^='product-']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.check_out")
    CHECKOUT_MODAL_LOGIN_LINK = (By.XPATH, "//u[contains(text(), 'Register / Login')]")
    
    # NEW LOCATORS FOR REMOVE MODULE
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, ".cart_quantity_delete")
    EMPTY_CART_TEXT = (By.XPATH, "//b[contains(text(), 'Cart is empty!')]")

    # ---------------------------------------------------------
    # 2. INITIALIZATION
    # ---------------------------------------------------------
    def __init__(self, driver):
        self.driver = driver

    # ---------------------------------------------------------
    # 3. ACTIONS
    # ---------------------------------------------------------
    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def click_proceed_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def is_login_prompt_visible(self):
        wait = WebDriverWait(self.driver, 5)
        prompt = wait.until(EC.visibility_of_element_located(self.CHECKOUT_MODAL_LOGIN_LINK))
        return prompt.is_displayed()
        
    # NEW ACTIONS FOR REMOVE MODULE
    def remove_first_item(self):
        """Clicks the 'X' button to delete the item from the cart."""
        self.driver.find_element(*self.REMOVE_ITEM_BUTTON).click()

    def is_cart_empty(self):
        """Waits for the 'Cart is empty!' text to appear."""
        wait = WebDriverWait(self.driver, 5)
        try:
            empty_msg = wait.until(EC.visibility_of_element_located(self.EMPTY_CART_TEXT))
            return empty_msg.is_displayed()
        except:
            return False
