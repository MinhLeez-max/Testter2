from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

try:
    # Bước 1: Mở trang "Books"
    driver.get("https://demoqa.com/books")

    # Bước 2: Xác minh danh sách sách hiển thị
    books_table = driver.find_element(By.ID, "app")
    assert books_table.is_displayed(), "Danh sách sách không hiển thị!"

    # Bước 3: Kiểm tra xem cuốn sách "Git Pocket Guide" có xuất hiện không
    book_title = driver.find_element(By.XPATH, "//a[text()='Git Pocket Guide']")
    assert book_title.is_displayed(), "Sách 'Git Pocket Guide' không xuất hiện trong danh sách!"

    print("Kiểm thử thành công: Danh sách sách hiển thị và chứa 'Git Pocket Guide'.")

finally:
    # Chờ vài giây để quan sát (nếu cần)
    time.sleep(5)

    # Đóng trình duyệt
    driver.quit()
