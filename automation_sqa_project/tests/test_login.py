from pages.login_page import LoginPage

def test_invalid_login(driver):
    """
    Test Case 1: Verify that a user cannot log in with incorrect credentials.
    """
    print("\nStarting Test: Invalid Login")
    
    # 1. Load the Page Object
    login_page = LoginPage(driver)
    
    # 2. Navigate to the website
    login_page.navigate()
    
    # 3. Perform actions (Type wrong email and password)
    login_page.enter_email("wrong_email_for_sqa@example.com")
    login_page.enter_password("wrong_password123")
    
    # 4. Click the login button
    login_page.click_login()
    
    # 5. Assertion (The "Check" phase)
    # We expect is_logged_in to be False since we used wrong credentials!
    assert login_page.is_logged_in() == False, "Bug: User was able to log in with invalid credentials!"
    
    print("\nTest Passed: The system successfully blocked the invalid login!")
