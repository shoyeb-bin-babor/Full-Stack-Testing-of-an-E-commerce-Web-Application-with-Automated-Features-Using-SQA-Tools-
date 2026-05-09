from pages.products_page import ProductsPage

def test_browse_products(driver):
    """
    Test Case 2: Verify that products are visible when visiting the Products page.
    """
    print("\nStarting Test: Browse Products")
    
    products_page = ProductsPage(driver)
    products_page.navigate()
    
    # We should see more than 0 products on the screen!
    count = products_page.get_product_count()
    assert count > 0, "Bug: No products were found on the products page!"
    
    print(f"\nTest Passed: Successfully loaded {count} products on the page.")

def test_search_product(driver):
    """
    Test Case 3: Verify that searching for 'Shirt' works and displays results.
    """
    print("\nStarting Test: Search for 'Shirt'")
    
    products_page = ProductsPage(driver)
    products_page.navigate()
    
    # 1. Perform the search
    products_page.search_for("Shirt")
    
    # 2. Verify the "Searched Products" title appears
    assert products_page.is_search_results_visible() == True, "Bug: Search results title did not appear!"
    
    # 3. Verify we actually got some item cards back in the results
    count = products_page.get_product_count()
    assert count > 0, "Bug: Search worked, but 0 shirts were found!"
    
    print(f"\nTest Passed: Successfully found {count} shirt(s)!")
