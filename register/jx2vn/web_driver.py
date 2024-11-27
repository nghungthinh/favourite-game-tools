from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class WebDriver:
    def __init__(self):
        chrome_options = Options()
        # Uncomment the line below to run headless
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-images')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(options=chrome_options)

    def quit(self):
        self.driver.quit()

    def register_account(self, username, password, phone):
        self.driver.get("https://jx2vn.com/api/dang-ky")
        try:
            # Username
            username_field = WebDriverWait(self.driver, 20).until(
                                                    EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/div/div/form/div[1]/div[1]/input")))
            username_field.send_keys(username)

            # Password 1
            password_field = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/form/div[1]/div[2]/input"))
            password_field.send_keys(password)

            # Password 2
            confirm_password_field = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/form/div[2]/div[1]/input"))
            confirm_password_field.send_keys(password)

            # Phone
            phone_field = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/form/div[2]/div[2]/div/input"))
            phone_field.send_keys(phone)

            # Confirm
            confirm_button = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/form/div[2]/div[3]/button"))
            confirm_button.click()

            # # Check if account exists
            # check_message = WebDriverWait(self.driver, 10).until(
            #     lambda d: d.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]")).text
            # return check_message

        except Exception as e:
            self.driver.save_screenshot(f"error_{username}.png")  # Save screenshot for debugging
            raise e        
    def checkIsExist(self, username):
        # Login
        # pass
        
        # Check if account exists 
        checkStrExist = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]")).text
        checkStr = "Tài khoản [" + username + "] đã tồn tại!"
        
        if (checkStrExist == checkStr):
            print("Account is exist")
            return True

    def getUsernameAfterRegister(self, userName):
        try:
            # Get Username
            username_field = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(By.XPATH, "/html/body/header/nav/div[2]/div/div[2]/div/span"))
            username = username_field.text

            if username != userName:
                return "Failed"
            else:
                return "Success"
        except Exception as e:
            return f"Failed (Error: {str(e)})"