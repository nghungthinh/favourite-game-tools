import threading
from user_registration import register_worker

if __name__ == "__main__":
    base_username = input("Username: ")
    password = input("Password: ")
    phone = input("Phone: ")
    account_count = int(input("Number of accounts to generate: "))

    threads = []
    for _ in range(1):  # Create 1 threads for demonstration
        t = threading.Thread(target=register_worker, args=(base_username, password, phone, account_count))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
