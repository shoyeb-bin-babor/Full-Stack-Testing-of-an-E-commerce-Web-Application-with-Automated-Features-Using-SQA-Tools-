from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_to_cart(driver):
    """
    Test Case 4: Verify that a user can successfully add a product to the cart.
    """
    print("\nStarting Test: Add to Cart")
    
    # 1. Load the Page Objects
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    
    # 2. Go to the products page
    products_page.navigate()
    
    # 3. Add the first item to the cart
    products_page.add_first_item_to_cart_and_view()
    
    # 4. Verify item is in the cart
    items_in_cart = cart_page.get_cart_item_count()
    assert items_in_cart > 0, "Bug: The cart is empty after adding a product!"
    
    print(f"\nTest Passed: Successfully found {items_in_cart} item(s) in the cart!")
