from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_remove_from_cart(driver):
    """
    Test Case 6: Verify that a user can successfully remove an item from the cart.
    """
    print("\nStarting Test: Remove Item from Cart")
    
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    
    # 1. Add item to cart
    products_page.navigate()
    products_page.add_first_item_to_cart_and_view()
    
    # 2. Verify it was actually added
    assert cart_page.get_cart_item_count() > 0, "Bug: The cart didn't receive the item in the first place."
    
    # 3. Click the Remove button
    cart_page.remove_first_item()
    
    # 4. Verify the 'Cart is empty!' message appears
    assert cart_page.is_cart_empty() == True, "Bug: Item was not removed from the cart!"
    
    print("\nTest Passed: Successfully removed the item and verified the cart is empty!")
