from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_anonymous_checkout_blocked(driver):
    """
    Test Case 5: Verify that an unregistered user cannot check out and is prompted to login.
    """
    print("\nStarting Test: Anonymous Checkout Blocked")
    
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    
    # 1. Go to products and add an item
    products_page.navigate()
    products_page.add_first_item_to_cart_and_view()
    
    # 2. Click on 'Proceed to Checkout'
    cart_page.click_proceed_to_checkout()
    
    # 3. Verify the system blocks them and asks them to login
    assert cart_page.is_login_prompt_visible() == True, "Bug: Anonymous user was allowed to checkout!"
    
    print("\nTest Passed: System successfully blocked checkout and prompted the user to login/register!")
