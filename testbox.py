from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Mở trang web
driver.get("https://demoqa.com/text-box")

# Tìm và nhập dữ liệu vào trường "Full Name"
full_name = driver.find_element(By.XPATH, "//input[@id='userName']")
full_name.send_keys("MinhLezMinhLez")

# Tìm và nhập dữ liệu vào trường "Email"
email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email.send_keys("minhleminhle@example.com")

# Tìm và nhập dữ liệu vào trường "Current Address"
current_address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
current_address.send_keys("33 XVNTXVNT")

# Tìm và nhập dữ liệu vào trường "Permanent Address"
permanent_address = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
permanent_address.send_keys("HihiHihi")

# Nhấn nút "Submit"
submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_button.click()

# Chờ vài giây để quan sát kết quả
time.sleep(5)

# Đóng trình duyệt
driver.quit()