from selenium.webdriver.common.by import By
from pageObjects.homepage import homePage
from pageObjects.loginpage import LoginPage
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogout:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_Logoutuser(self, driver):
        self.driver = driver
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.logger.info("website opened")
        self.lp = LoginPage(driver)
        self.lp.setUserName("standard_user")
        self.lp.setPassword("secret_sauce")
        self.lp.clickLogin()

        self.hp = homePage(driver)
        self.hp.closePasswordAlertIfPresent()
        assert self.hp.getLogo().is_displayed()
        self.hp.clickMenu()
        self.hp.clickLogout()
        self.logger.info("logout button clicked")
        assert "https://www.saucedemo.com/v1/index.html" in driver.current_url
        self.logger.info("Logout test passed")
