import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_phone_links():
    """Lấy danh sách links điện thoại từ danh sách ul class 'listproduct'"""
    # Cấu hình các tùy chọn của Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Không hiển thị giao diện trình duyệt
    chrome_options.add_argument('--no-sandbox')  # Bỏ sandboxing
    chrome_options.add_argument('--disable-dev-shm-usage')  # Tắt sử dụng shared memory

    # Tự động tải và sử dụng ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Truy cập trang web
    url = "https://www.thegioididong.com/dtdd#c=42&o=13&pi=6"
    driver.get(url)

    # Chờ cho trang web load xong
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".listproduct .item"))
    )

    # Lấy mã HTML sau khi trang đã được tải xong
    html = driver.page_source

    # Dùng BeautifulSoup để xử lý HTML
    soup = BeautifulSoup(html, "html.parser")

    # Lấy thông tin sản phẩm
    phones = soup.select(".listproduct .item")
    phone_links = []

    for phone in phones:
        link_tag = phone.select_one("a")
        if link_tag:
            link = f"https://www.thegioididong.com{link_tag['href']}"
            name = link_tag.get('data-name', '').strip()
            
            if link and name:
                clean_name = name.replace('Điện thoại', '').strip()
                phone_links.append({'link': link, 'name': clean_name})

    # Đóng trình duyệt sau khi hoàn tất
    driver.quit()
    
    return phone_links

def save_phone_links(phone_links, data_dir='data'):
    """Lưu danh sách links vào file JSON"""
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(data_dir, f"phone_links_{timestamp}.json")
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(phone_links, f, ensure_ascii=False, indent=2)
    
    print(f"\nĐã lưu danh sách links vào file {filename}")
    return filename

def load_phone_links(filename=None, data_dir='data'):
    """Đọc danh sách links từ file JSON"""
    import os
    import json

    if filename is None:
        # Nếu không có filename, lấy file mới nhất
        if not os.path.exists(data_dir):
            print(f"Không tìm thấy thư mục {data_dir} chứa danh sách links!")
            return None
            
        files = [f for f in os.listdir(data_dir) if f.startswith('phone_links_')]
        if not files:
            print("Không tìm thấy file chứa danh sách links!")
            return None
            
        filename = os.path.join(data_dir, sorted(files)[-1])  # Lấy file mới nhất
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            phone_links = json.load(f)
        print(f"\nĐã tải danh sách links từ file {filename}")
        return phone_links
    except Exception as e:
        print(f"Lỗi khi đọc file {filename}: {str(e)}")
        return None


if __name__ == "__main__":
    phone_links = get_phone_links()
    if phone_links:
        save_phone_links(phone_links)
