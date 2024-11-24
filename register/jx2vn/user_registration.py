import csv
from threading import Lock
from web_driver import WebDriver

mutex = Lock()
shared_variable = 0

# Hàm tạo file CSV và ghi tiêu đề nếu file chưa tồn tại
def create_csv_file(file_name):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Password 1", "Password 2", "Phone", "Status"])  # Ghi tiêu đề

# Hàm ghi một dòng dữ liệu vào file CSV
def append_to_csv(file_name, row):
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def generate_usernames(base_username, count):
    return [f"{base_username}{i}" for i in range(count)]

def register_worker(base_username, password, phone, count):
    global shared_variable
    usernames = generate_usernames(base_username, count)

    for username in usernames:
        with mutex:  # Thread-safe shared resource update
            shared_variable += 1

        driver = WebDriver()
        try:
            # Register account
            driver.register_account(username, password, phone)

            if driver.checkIsExist(username):
                status = "Account is exist"
            else:
                status = driver.getUsernameAfterRegister(username)
            
            print(f"Account: {username}, Result: {status}")
            append_to_csv("output.csv", [username, password, password, phone, status])
        except Exception as e:
            # Xử lý lỗi trong quá trình đăng ký (timeout hoặc lỗi khác)
            print(f"Account: {username}, Error during registration: {str(e)}")
            append_to_csv("output.csv", [username, password, password, phone, "Failed"])
        finally:
            driver.quit()
