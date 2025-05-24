from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

class LoginPage():
    txt_username_id = "user-name"
    txt_password_id = "password"
    btn_login_id = "login-button"
    txt_error_xpath = "//h3[@data-test='error']"
    txt_error_css = "h3[data-test='error']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()

    def getErrorMessage(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txt_error_xpath))
        )
        return self.driver.find_element(By.XPATH, self.txt_error_xpath).text
    
    def getErrorMessageCSS(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.txt_error_css))
        )
        return self.driver.find_element(By.CSS_SELECTOR, self.txt_error_css).text