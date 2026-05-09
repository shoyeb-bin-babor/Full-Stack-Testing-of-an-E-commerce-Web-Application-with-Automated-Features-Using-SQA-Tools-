from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    # 1. LOCATORS
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".product-image-wrapper")
    SEARCHED_PRODUCTS_TITLE = (By.XPATH, "//h2[contains(text(), 'Searched Products')]")
    
    # --- NEW LOCATORS FOR CART MODULE ---
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".features_items .add-to-cart")
    VIEW_CART_LINK = (By.XPATH, "//u[contains(text(), 'View Cart')]")

    def __init__(self, driver):
        self.driver = driver

    # 2. ACTIONS
    def navigate(self):
        self.driver.get("https://automationexercise.com/products")

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_CARDS))

    def search_for(self, product_name):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(product_name)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def is_search_results_visible(self):
        elements = self.driver.find_elements(*self.SEARCHED_PRODUCTS_TITLE)
        return len(elements) > 0

    # --- NEW ACTION FOR CART MODULE ---
    def add_first_item_to_cart_and_view(self):
        """Clicks add to cart, waits for the popup, and clicks View Cart."""
        # Find all "Add to Cart" buttons
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        
        # PRO TIP: We use a JavaScript click here to bypass the fact that the 
        # button is technically hidden behind a "hover" animation!
        self.driver.execute_script("arguments[0].click();", buttons[0])
        
        # PRO TIP: Explicit Wait
        # We wait up to 5 seconds for the success popup to appear before clicking it
        wait = WebDriverWait(self.driver, 5)
        view_cart_btn = wait.until(EC.element_to_be_clickable(self.VIEW_CART_LINK))
        view_cart_btn.click()
