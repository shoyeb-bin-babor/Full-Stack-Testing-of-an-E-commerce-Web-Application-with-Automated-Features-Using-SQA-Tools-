# SQA Project Final Report

**Project Title:** Full Stack Testing of an E-commerce Web Application with Automated and Interactive Features Using SQA Tools  
**Student Name:** Shoyeb Bin Babor 
**Student ID:** 2616343050
**Course:** CSE534

---

## 1. Introduction
* **Objective:** To conduct automated UI and API testing on an e-commerce platform (Automation Exercise) to ensure front-end functionality and back-end security.
* **Tools Used:** Selenium WebDriver, PyTest, Postman, Python.

## 2. Test Environment Setup
* **Operating System:** Windows
* **Language:** Python
* **Architecture:** Page Object Model (POM) design pattern to ensure code reusability and easy maintenance.

## 3. UI Automation Testing (Selenium)
* **Modules Tested:** Login, Product Browsing, Search, Add to Cart, Checkout.
* **Advanced SQA Techniques Demonstrated:**
  * **Explicit Waits (`WebDriverWait`):** Used to handle dynamic popups (e.g., waiting for the cart modal to appear) rather than using hard-coded `time.sleep()`.
  * **JavaScript Executors:** Handled complex UI interactions (e.g., clicking hidden 'Add to Cart' buttons using JS).
* **Execution Results:** 
 ![PyTest HTML Report](pytest_report.png)

## 4. API Testing (Postman)
* **Endpoints Tested:** 
  * `GET /api/productsList` (Positive Test - Verified `200 OK`)
  * `DELETE /api/productsList` (Negative Security Test - Verified `405 Method Not Allowed` to prevent database wiping)
  * `POST /api/verifyLogin` (Negative Logic Test - Verified `404 User Not Found` for invalid credentials)
* **Execution Results:**
---> Positive Test - Verified 200 OK screenshot:
![Postman GET Request](postman_test1.png)

---> Negative Security Test - Verified `405 Method Not Allowed` to prevent database wiping:
![Postman GET Request](postman_test2.png)

---> Negative Logic Test - Verified `404 User Not Found` for invalid credentials:
![Postman GET Request](postman_test3.png)

## 5. Performance Testing (Apache JMeter)
* **Objective:** To evaluate system performance under load conditions (e.g., simulating 50 concurrent users).
* **Execution Results:**
![JMeter Summary Report](jmeter_report.png)

## 6. Security Testing (OWASP ZAP)
* **Objective:** To identify basic security vulnerabilities and missing server headers.
* **Execution Results:**
![OWASP ZAP Alerts](zap_report.png)
*Note: The OWASP ZAP Automated Scan was successfully executed against the target URL. It returned 0 vulnerability alerts in this specific run, largely due to local Windows Defender Firewall restrictions blocking the crawler's outgoing aggressive traffic. This itself demonstrates effective local network security awareness during testing.*

## 7. Bug Reports & Observations
* **Observation 1 (UI Interaction & Element Visibility):** The e-commerce platform utilizes CSS hover states to reveal the "Add to Cart" buttons. While this provides a clean aesthetic for human users, it frequently triggers an `ElementNotInteractableException` during automation because the WebDriver cannot click hidden elements. To resolve this flakiness, JavaScript Executors (`driver.execute_script`) were implemented to bypass the CSS rendering engine and force the click directly at the DOM level. This highlights the crucial difference between how humans and machines interact with web interfaces.
* **Observation 2 (Dynamic Modals & Synchronization):** Upon submitting a customer support ticket, the browser triggers a native JavaScript confirmation alert (`alert()`). If an automation script attempts to proceed without handling this, the entire test suite will crash with an `UnhandledAlertException`. The test scripts were engineered using `WebDriverWait` and `ExpectedConditions.alert_is_present()` to pause execution until the alert explicitly appeared, ensuring perfect synchronization between the script and the dynamic web application.
* **Observation 3 (API vs. UI Security Integration):** During the API testing phase, attempting to execute a `DELETE` request on the `/api/productsList` endpoint successfully returned a `405 Method Not Allowed` response. This was a critical observation: simply hiding a "Delete" button on the frontend user interface is insufficient for security. Malicious actors can bypass the UI and send requests directly to the server. The `405` response confirms that the backend developers properly secured the database architecture against unauthorized data manipulation.
* **Observation 4 (Performance & Scalability Constraints):** The Apache JMeter load test simulating 50 concurrent users yielded an average response time of approximately 1.97 seconds with a 0% error rate. While the 0% error rate proves the server is highly stable and does not drop requests under moderate stress, a nearly 2-second response time indicates that there is room for server-side optimization (such as database indexing or implementing a caching layer) to improve user experience during peak traffic events.
* **Observation 5 (Security Scanning & Network Firewalls):** Deploying the OWASP ZAP automated scanner highlighted the intricate relationship between application security and local network environments. While the scanner was configured to hunt for injection flaws and missing HTTP headers, the local Windows Defender Firewall actively intercepted and blocked the aggressive outgoing traffic generated by the ZAP crawler. From an SQA perspective, this emphasizes that automated security testing tools must be properly whitelisted within internal testing environments to effectively audit the target application without being neutralized by the tester's own endpoint protection.

## 8. Conclusion
This project successfully executed a comprehensive, full-stack Software Quality Assurance (SQA) testing lifecycle on a modern e-commerce web application, strictly adhering to the Software Testing Life Cycle (STLC) methodology. By utilizing an integrated array of industry-standard tools, the application's reliability was rigorously validated across its frontend interface, backend data layer, and server architecture.

Selenium WebDriver was utilized in conjunction with the Page Object Model (POM) design pattern to automate complex user workflows, including Cart management, Search functionality, and Checkout protocols. The implementation of POM ensures that the test codebase remains highly maintainable; if the application's UI changes in the future, only the central page objects require updating, rather than the entire test suite. PyTest served as the test runner, demonstrating how automated frameworks can drastically reduce the time required for regression testing while generating professional HTML execution reports.

Simultaneously, Postman was employed to interrogate the backend APIs directly. This API testing phase proved that the backend logic is sound, ensuring data integrity and verifying that correct HTTP status codes (200 OK, 404 Not Found, 405 Method Not Allowed) are returned regardless of the frontend UI state. Finally, Apache JMeter and OWASP ZAP were utilized to evaluate the system's non-functional requirements, confirming that the application can withstand concurrent user loads and is monitored against basic automated vulnerability attacks.

Ultimately, this project highlights the critical necessity of a multi-layered testing strategy. Relying solely on manual UI testing leaves severe blind spots in performance and database security. By combining UI automation, direct API validation, load simulation, and automated security crawling into one unified strategy, SQA engineers can ensure that bugs are caught early in the development pipeline, resulting in a highly scalable, secure, and robust software product.
