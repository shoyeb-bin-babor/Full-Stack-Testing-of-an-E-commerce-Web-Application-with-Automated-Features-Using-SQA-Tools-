# Full-Stack-Testing-of-an-E-commerce-Web-Application-with-Automated-Features-Using-SQA-Tools-

# 🚀 Full-Stack SQA Automation Framework

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)
![PyTest](https://img.shields.io/badge/PyTest-Testing-yellow.svg)
![Postman](https://img.shields.io/badge/Postman-API_Testing-orange.svg)
![JMeter](https://img.shields.io/badge/JMeter-Performance-red.svg)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-Security-blueviolet.svg)

## 📌 Project Overview
This project is a comprehensive **Software Quality Assurance (SQA)** automation framework built for the [Automation Exercise](https://automationexercise.com/) e-commerce web application. 

Instead of relying solely on manual testing, this project implements a multi-layered testing strategy covering:
1. **Frontend UI Automation** (Selenium WebDriver + PyTest)
2. **Backend API Validation** (Postman)
3. **Performance & Load Testing** (Apache JMeter)
4. **Security Vulnerability Scanning** (OWASP ZAP)

This project was developed as the final submission for the **Software Quality Assurance (CSE 534)** course at North South University.
---

## 🎯 What This System Does
This system acts as a fully automated QA engineer. It is programmed to:
1. Automatically launch a browser and navigate to the e-commerce platform.
2. Dynamically locate web elements (buttons, forms, modals) and interact with them like a real human user.
3. Verify that expected outcomes occur (e.g., cart quantities increase, invalid logins are rejected).
4. Send raw HTTP requests directly to the server to test backend database security.
5. Simulate heavy user traffic to test server stability and scan for security vulnerabilities.
6. Generate comprehensive execution reports and capture evidence automatically.

---

## 🔗 System Integration
This project integrates multiple tools to form a complete SQA pipeline:
* **Selenium + PyTest:** The Page Object Model (POM) architecture integrates directly with PyTest fixtures to ensure a clean browser state for every test, automatically generating an HTML execution report upon completion.
* **UI + API Layer:** While Selenium handles the frontend DOM interactions, Postman tests the underlying REST API, providing a true full-stack integration testing strategy.

---

## 📑 Full Reports & Evidence Files
To view the complete findings, methodologies, and visual evidence (screenshots of bugs, JMeter graphs, Postman responses, and PyTest HTML logs), please refer to the detailed academic reports located in the `reports/` directory:

* 📄 **[NSU Final Report](reports/NSU_Final_Report.md):** The comprehensive 24-section academic project report containing all findings, bug reports, and testing strategies.
* 📊 **PyTest HTML Report:** Located at `reports/pytest_report.html`, this auto-generated file provides timestamped execution evidence of all UI automation tests.
* 🖼️ **Visual Evidence:** All test execution screenshots and tool outputs (Postman, JMeter, ZAP) are embedded directly within the Final Report.

---
## 🏗️ Architecture & Design Patterns
The UI automation framework strictly follows the **Page Object Model (POM)** design pattern. 
* **Maintainability:** UI locators and interactions are separated from test logic.
* **Stability:** Implements `WebDriverWait` (Explicit Waits) to handle dynamic web elements and AJAX calls.
* **Advanced Interactions:** Utilizes JavaScript Executors to bypass complex CSS hover states and DOM-hidden elements.

---

## 🛠️ Technology Stack
* **Programming Language:** Python 3.13
* **UI Automation:** Selenium WebDriver
* **Test Runner & Reporting:** PyTest, pytest-html
* **API Testing:** Postman
* **Performance Testing:** Apache JMeter (50 Concurrent Users)
* **Security Testing:** OWASP ZAP (Automated Active Scan)

---

## 📂 Project Structure
```text
📦 automation_sqa_project
 ┣ 📂 pages                 # Page Object Model classes (Locators & Methods)
 ┃ ┣ 📜 cart_page.py
 ┃ ┣ 📜 contact_page.py
 ┃ ┣ 📜 login_page.py
 ┃ ┗ 📜 products_page.py
 ┣ 📂 tests                 # PyTest Execution Scripts
 ┃ ┣ 📜 conftest.py         # Global test fixtures & browser setup
 ┃ ┣ 📜 test_cart.py
 ┃ ┣ 📜 test_checkout.py
 ┃ ┣ 📜 test_contact_us.py
 ┃ ┣ 📜 test_login.py
 ┃ ┣ 📜 test_products.py
 ┃ ┗ 📜 test_remove_cart.py
 ┣ 📂 reports               # Execution Reports & Documentation
 ┃ ┣ 📜 NSU_Final_Report.md # Comprehensive Academic Report
 ┃ ┗ 📜 pytest_report.html  # Auto-generated HTML execution report
 ┣ 📜 API_Testing_Guide.md  # API execution documentation
 ┣ 📜 Performance_and_Security_Guide.md # JMeter & ZAP documentation
 ┣ 📜 requirements.txt      # Python dependencies
 ┗ 📜 README.md             # Project overview
```

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd automation_sqa_project
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ How to Run the UI Automation Tests

To execute the entire test suite and automatically generate an HTML report, run the following command in your terminal:

```bash
pytest tests/ -v --html=reports/pytest_report.html
```

* **Note:** The `conftest.py` is configured with a 10-second `time.sleep()` during the browser teardown phase to allow for visual confirmation and screen recording.

---

## 📊 Testing Highlights

### 1. API Testing (Postman)
Validated backend security by confirming the database rejects unauthorized `DELETE` requests (`405 Method Not Allowed`) and handles invalid authentication payloads (`404 User Not Found`).

### 2. Performance Testing (JMeter)
Simulated 50 concurrent virtual users accessing the platform simultaneously. Achieved a **0% Error Rate** with an average response time of 1.97s, proving high server stability under load.

### 3. Security Testing (OWASP ZAP)
Configured and executed an automated vulnerability spider/scan. Documented the impact of local Windows Defender Firewall active-interception on security auditing tools.

---

## 👨‍💻 Author
**Shoyeb Bin Babor**
* Software Quality Assurance (CSE 534)
* North South University
