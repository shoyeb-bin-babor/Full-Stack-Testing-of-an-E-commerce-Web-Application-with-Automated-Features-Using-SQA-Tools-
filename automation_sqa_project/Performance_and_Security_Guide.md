# Performance and Security Testing Guide

This document outlines the methodology and instructions for executing the non-functional performance and security testing phases of this project.

## 1. Performance Testing (Apache JMeter)
Apache JMeter was selected as the industry standard tool for simulating concurrent user traffic to evaluate server scalability.

### Execution Instructions:
1. **Prerequisites:** Ensure Java is installed. Download Apache JMeter from `https://jmeter.apache.org/download_jmeter.cgi`.
2. **Launch:** Extract the archive, navigate to the `bin` directory, and execute `jmeter.bat`.
3. **Test Plan Configuration:**
   * Add a **Thread Group** to the Test Plan.
   * Configure the "Number of Threads (users)" to `50` to simulate concurrent load.
   * Add an **HTTP Request** sampler and set the Server Name to: `automationexercise.com`.
   * Add a **Summary Report** listener to capture metrics.
4. **Execution:** Run the test using the Start button.
5. **Results Analysis:** The Summary Report generates key metrics including Average Response Time and Error Rate, which are documented in the Final Report artifacts.

---

## 2. Security Testing (OWASP ZAP)
OWASP ZAP (Zed Attack Proxy) was utilized to perform automated vulnerability scanning, crawling the application to identify weaknesses such as missing headers or injection vulnerabilities.

### Execution Instructions:
1. **Prerequisites:** Install OWASP ZAP from `https://www.zaproxy.org/download/`.
2. **Launch:** Open the ZAP application and initiate a temporary session.
3. **Configuration:** Navigate to the Quick Start menu and select **Automated Scan**.
4. **Target Setup:** Enter the target URL: `https://automationexercise.com`.
5. **Execution:** Initiate the attack. ZAP will utilize its spider modules to crawl and actively scan the target.
6. **Results Analysis:** Upon completion, review the "Alerts" tab to identify any flagged vulnerabilities. Note: Local Windows Defender Firewall configurations may intentionally intercept and block the scanner's active payload delivery, resulting in 0 alerts in certain execution environments.
