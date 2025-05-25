import pytest
from pageObjects.loginpage import LoginPage
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.blogpage1 import BlogPage1  # Add this import, adjust the module path if needed

class Test_radiobtn:
    baseURL2 = ReadConfig.getApplicationURL2()

    def test_radiobtnmale(self, driver):
        self.driver = driver
        self.driver.get(self.baseURL2)
        self.driver.maximize_window()

        # Locate the radio button
        self.bp = BlogPage1(driver)
        self.bp.clickRadioBtnMale()
        assert self.bp.isRadioBtnMaleSelected() == True
    
    def test_radiobtnfemale(self, driver):
        self.driver = driver
        self.driver.get(self.baseURL2)
        self.driver.maximize_window()

        # Locate the radio button
        self.bp = BlogPage1(driver)
        self.bp.clickRadioBtnFemale()
        assert self.bp.isRadioBtnFemaleSelected() == True

