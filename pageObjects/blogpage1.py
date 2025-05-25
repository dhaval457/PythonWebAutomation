from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

class BlogPage1():
    radio_btnmale_xpath = "//input[@id='male']"
    radio_btnfemale_xpath = "//input[@id='female']"
    checkbox_sunday_xpath = "//input[@id='sunday']"
    checkbox_monday_xpath = "//input[@id='monday']"


    def __init__(self, driver):
        self.driver = driver

    def clickRadioBtnMale(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.radio_btnmale_xpath))
        )
        self.driver.find_element(By.XPATH, self.radio_btnmale_xpath).click()

    def clickRadioBtnFemale(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.radio_btnfemale_xpath))
        )
        self.driver.find_element(By.XPATH, self.radio_btnfemale_xpath).click()
    
    def isRadioBtnMaleSelected(self):
        return self.driver.find_element(By.XPATH, self.radio_btnmale_xpath).is_selected()
    
    def isRadioBtnFemaleSelected(self):
        return self.driver.find_element(By.XPATH, self.radio_btnfemale_xpath).is_selected()
    
    def clickCheckboxSunday(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_sunday_xpath))
        )
        self.driver.find_element(By.XPATH, self.checkbox_sunday_xpath).click()
    
    def clickCheckboxMonday(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_monday_xpath))
        )
        self.driver.find_element(By.XPATH, self.checkbox_monday_xpath).click()
    
    def isCheckboxSundaySelected(self):
        return self.driver.find_element(By.XPATH, self.checkbox_sunday_xpath).is_selected()
    def isCheckboxMondaySelected(self):
        return self.driver.find_element(By.XPATH, self.checkbox_monday_xpath).is_selected()
    