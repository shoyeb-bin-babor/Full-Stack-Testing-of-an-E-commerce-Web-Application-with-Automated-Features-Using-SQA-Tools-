# API Testing Guide

## 1. Overview of API Testing
While Selenium automates the visual interface (DOM elements), Postman is utilized to validate the underlying backend APIs. The objective is to verify that the server responds correctly to valid data requests and securely rejects unauthorized or malformed requests.

## 2. Base Configuration
All API requests for this project are directed to the base URL:
`https://automationexercise.com`

---

## 3. Test Case Executions

### Test Case 1: Retrieve All Products (Positive Test)
**Objective:** Verify that the server successfully returns the complete product catalog.

1. **Client Setup:** Open Postman and create a new HTTP Request.
2. **Method:** `GET`
3. **Endpoint:** `https://automationexercise.com/api/productsList`
4. **Execution:** Send the request.
5. **Expected Result:** The server must return an HTTP Status of `200 OK`. The response body should contain a formatted JSON array of all available products.

---

### Test Case 2: Unauthorized Deletion (Negative Security Test)
**Objective:** Verify that the backend infrastructure blocks unauthorized HTTP methods.

1. **Client Setup:** Create a new HTTP Request.
2. **Method:** `DELETE`
3. **Endpoint:** `https://automationexercise.com/api/productsList`
4. **Execution:** Send the request.
5. **Expected Result:** The response body will contain JSON stating: `{"responseCode": 405, "message": "This request method is not supported."}`. This confirms the backend controllers are secure against bulk deletion attempts.

---

### Test Case 3: Invalid Authentication (Negative Logic Test)
**Objective:** Verify that the login API endpoint correctly rejects invalid credentials.

1. **Client Setup:** Create a new HTTP Request.
2. **Method:** `POST`
3. **Endpoint:** `https://automationexercise.com/api/verifyLogin`
4. **Payload Configuration:** Navigate to the **Body** tab, select **x-www-form-urlencoded**, and input the following Key-Value pairs:
   * **email**: `wrong@example.com`
   * **password**: `badpass`
5. **Execution:** Send the request.
6. **Expected Result:** The response body will return `{"responseCode": 404, "message": "User not found!"}`, confirming the authentication layer is functioning correctly.
