import pytest
from pageObjects.loginpage import LoginPage
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_valid_login(self, driver):
        self.driver = driver
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("website opened")

        self.lp = LoginPage(driver)
        self.lp.setUserName("standard_user")
        self.lp.setPassword("secret_sauce")
        self.lp.clickLogin()
        self.logger.info("login button clicked")

        assert "inventory" in driver.current_url

    def test_invalid_login(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/v1/index.html")
        self.driver.maximize_window()

        self.lp = LoginPage(driver)
        self.lp.setUserName("standard_user")
        self.lp.setPassword("wrong_password")
        self.lp.clickLogin()
        error_message = self.lp.getErrorMessage()
        print("Error message is: ", error_message)
        assert error_message == "Epic sadface: Username and password do not match any user in this service"

    def test_only_username_login(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/v1/index.html")
        self.driver.maximize_window()

        self.lp = LoginPage(driver)
        self.lp.setUserName("standard_user")
        self.lp.clickLogin()
        error_message = self.lp.getErrorMessageCSS()
        print("Error message is: ", error_message)
        assert error_message == "Epic sadface: Password is required"
        self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshot\\"+"test_only_username_login.png")