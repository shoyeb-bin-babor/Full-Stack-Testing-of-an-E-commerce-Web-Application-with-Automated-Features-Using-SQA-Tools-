from pages.contact_page import ContactPage

def test_support_ticket(driver):
    """
    Test Case 7: Verify user can interact with the Customer Support chat/form interface.
    """
    print("\nStarting Test: Submit Customer Support Ticket")
    
    contact_page = ContactPage(driver)
    
    # 1. Go to the Contact Us page
    contact_page.navigate()
    
    # 2. Fill out and submit the support form
    contact_page.submit_support_ticket(
        name="Student Tester",
        email="student@university.edu",
        subject="Testing Support Flow",
        message="This is an automated test for my SQA university project verifying the interactive support feature."
    )
    
    # 3. Verify the success message appeared
    assert contact_page.is_ticket_successful() == True, "Bug: Support ticket failed to submit!"
    
    print("\nTest Passed: Support ticket submitted and Javascript alert handled successfully!")
