# favourite-game-tools

# **Selenium Account Registration Tool for JX2VN**

This project automates the process of account registration using Selenium WebDriver.

---

### **Examples**

#### **1. Auto Mode**
Automatically generate usernames with a base name and count:
```bash
python main.py --mode=auto --base_username=username --count=15 --threads=3 --phone=012345678912 --password=123456
```
- This will create 15 usernames (`nghungthinh1` to `nghungthinh15`), divide them among 3 threads, and register accounts using the specified phone and password.

#### **2. Manual Mode**
Register specific usernames manually:
```bash
python main.py --mode=manual --manual_usernames user1 user2 user3 --threads=1 --phone=012345678912 --password=123456
```
- This will register the usernames `user1`, `user2`, and `user3` sequentially using 1 thread.

---

## **Features**
- Register accounts automatically or manually.
- Save results (username, password, phone, and status) in a CSV file.
- Multi-threaded support for faster registration.
- Handles errors and retries failed registrations.

---

## **Requirements**

### **System Requirements**
- Python 3.8 or later
- Google Chrome browser
- ChromeDriver (ensure the version matches your Chrome browser)

### **Python Packages**
Install the required Python libraries:
```bash
pip install selenium
