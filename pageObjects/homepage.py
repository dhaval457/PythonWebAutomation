from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class homePage:

    img_logo_xpath = "//div[@class='app_logo']"
    btn_menu_xpath = "//button[normalize-space()='Open Menu']"
    bth_logout_xpath = "//a[@id='logout_sidebar_link']"
    password_alert_button_xpath = "//button[text()='OK']"


    def __init__(self,driver):
        self.driver = driver
    
    def closePasswordAlertIfPresent(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.password_alert_button_xpath)))
            ok_button.click()
            print("Password alert closed.")
        except:
            print("No password alert found.")
    
    def getLogo(self):
        webdriver_wait = WebDriverWait(self.driver, 10)
        webdriver_wait.until(
            EC.presence_of_element_located((By.XPATH, self.img_logo_xpath))
        )
        return self.driver.find_element(By.XPATH, self.img_logo_xpath)
    
    def clickMenu(self):
        self.driver.find_element(By.XPATH, self.btn_menu_xpath).click()

    def clickLogout(self):
        webdriver_wait = WebDriverWait(self.driver, 10)
        webdriver_wait.until(
            EC.element_to_be_clickable((By.XPATH, self.bth_logout_xpath))
        )
        self.driver.find_element(By.XPATH, self.bth_logout_xpath).click()        