from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Khởi tạo WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Mở trang danh sách điện thoại
    driver.get("https://www.thegioididong.com/dtdd")
    time.sleep(3)  # Chờ trang tải

    # Lấy danh sách các sản phẩm
    products = driver.find_elements(By.XPATH, "//ul[@class='listproduct']/li")

    # Tạo danh sách để lưu dữ liệu
    data = []

    for product in products:
        try:
            # Lấy tên sản phẩm
            name = product.find_element(By.XPATH, ".//h3").text

            # Lấy giá sản phẩm
            price = product.find_element(By.XPATH, ".//strong").text

            # Lấy URL hình ảnh sản phẩm
            image = product.find_element(By.XPATH, ".//img").get_attribute("src")

            # Lưu dữ liệu vào danh sách
            data.append({"name": name, "price": price, "image": image})
        except Exception as e:
            print(f"❌ Lỗi khi lấy dữ liệu sản phẩm: {e}")

    # Lưu dữ liệu vào file CSV
    with open("products.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "image"])
        writer.writeheader()
        writer.writerows(data)

    print("✅ Dữ liệu đã được lưu vào file 'products.csv'!")

finally:
    # Đóng trình duyệt
    driver.quit()