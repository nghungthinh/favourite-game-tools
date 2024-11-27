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

def generate_usernames(base_username, count=None, mode="auto", manual_usernames=None):
    if mode == "auto":
        if count is None:
            raise ValueError("Count must be provided in 'auto' mode.")
        return [f"{base_username}{i}" for i in range(1, count + 1)]
    elif mode == "manual":
        if not manual_usernames:
            raise ValueError("Manual usernames must be provided in 'manual' mode.")
        return manual_usernames
    else:
        raise ValueError("Invalid mode. Use 'auto' or 'manual'.")

def register_worker(usernames, password, phone, count):
    global shared_variable

    for username in usernames:
        with mutex:
            shared_variable += 1

        driver = WebDriver()
        max_retries = 3
        attempt = 0
        while attempt < max_retries:
            try:
                # Register account
                driver.register_account(username, password, phone)

                if driver.checkIsExist(username):
                    status = "Account is exist"
                else:
                    status = driver.getUsernameAfterRegister(username)

                print(f"Account: {username}, Result: {status}")
                append_to_csv("output.csv", [username, password, password, phone, status])
                break  # Exit loop if successful
            except Exception as e:
                attempt += 1
                if attempt >= max_retries:
                    print(f"Account: {username}, Error after {attempt} retries: {str(e)}")
                    append_to_csv("output.csv", [username, password, password, phone, "Failed"])
            finally:
                driver.quit()
