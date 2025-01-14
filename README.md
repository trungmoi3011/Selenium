# Selenium Login Test Automation

This project demonstrates an automated test script for validating the login functionality of a sample website (`https://demo.guru99.com/test/login.html`) using Selenium WebDriver in Python. The test script includes multiple test cases to verify different login scenarios.

## Features
- Automated testing of login functionality.
- Validates success, failure, and blank field scenarios.
- Implements best practices for Selenium automation, including reusable functions and dynamic waits.
- Easy-to-read logging for test results.

## Prerequisites
1. Python 3.8 or later installed.
2. Google Chrome browser installed.
3. Required Python packages:
   - `selenium`
   - `webdriver-manager`

You can install the necessary packages using:
```bash
pip install selenium webdriver-manager
```

## Project Structure
```
.
├── main.py       # Main script file
├── README.md     # Project documentation
```

## Setup Instructions
1. Clone this repository or copy the script into your local machine.
2. Ensure all prerequisites are installed.
3. Execute the script using the following command:
   ```bash
   python main.py
   ```

## Test Scenarios
The script covers the following test cases:

1. **Successful Login**:
   - Input: Valid email and password (`test@example.com`, `123456`).
   - Expected Result: "Successfully logged in" message appears.

2. **Failed Login**:
   - Input: Invalid email and password (`wrong@example.com`, `wrongpassword`).
   - Expected Result: "Invalid email or password" message appears.

3. **Blank Fields**:
   - Input: No email and password provided.
   - Expected Result: "Email and password required" message appears.

## Code Highlights
### Reusable Function for Login
The script includes a reusable function to simplify login steps:
```python
def login(driver, email_text, password_text):
    email = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "passwd")
    email.clear()
    password.clear()
    email.send_keys(email_text)
    password.send_keys(password_text)
    driver.find_element(By.ID, "SubmitLogin").click()
```

### Dynamic Waits
The script replaces static waits (`time.sleep()`) with dynamic waits for better performance:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "SubmitLogin"))
)
```

### Logging
The script uses Python's built-in `logging` module for enhanced result tracking:
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Test case passed")
```

## Future Improvements
- Integrate with a testing framework like `pytest` or `unittest`.
- Generate detailed HTML reports using libraries such as `Allure` or `HTMLTestRunner`.
- Expand test cases for edge cases and boundary value testing.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

Happy Testing! 🚀
