from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Đường dẫn tới ChromeDriver
driver_path = r"C:\Users\tranm\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Tạo đối tượng Service
service = Service(driver_path)

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=service)

try:
    # Mở trang web
    driver.get("https://demo.guru99.com/test/login.html")
    driver.maximize_window()

    # Test case 1: Đăng nhập thành công
    email = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "passwd")
    email.send_keys("test@example.com")
    password.send_keys("123456")
    driver.find_element(By.ID, "SubmitLogin").click()
    time.sleep(2)

    if "Successfully logged in" in driver.page_source:
        print("Test case 1: Đăng nhập thành công - Passed")
    else:
        print("Test case 1: Đăng nhập thành công - Failed")

    # Quay lại trang đăng nhập
    driver.back()

    # Test case 2: Đăng nhập thất bại
    email = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "passwd")
    email.clear()
    password.clear()
    email.send_keys("wrong@example.com")
    password.send_keys("wrongpassword")
    driver.find_element(By.ID, "SubmitLogin").click()
    time.sleep(2)

    if "Invalid email or password" in driver.page_source:
        print("Test case 2: Đăng nhập thất bại - Passed")
    else:
        print("Test case 2: Đăng nhập thất bại - Failed")

    # Quay lại trang đăng nhập
    driver.back()

    # Test case 3: Để trống trường
    email = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "passwd")
    email.clear()
    password.clear()
    driver.find_element(By.ID, "SubmitLogin").click()
    time.sleep(2)

    if "Email and password required" in driver.page_source:
        print("Test case 3: Để trống trường - Passed")
    else:
        print("Test case 3: Để trống trường - Failed")

finally:
    # Đóng trình duyệt
    driver.quit()
