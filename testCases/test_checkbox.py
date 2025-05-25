import pytest
from pageObjects.loginpage import LoginPage
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.blogpage1 import BlogPage1  # Adjust the import path as necessary

class Test_checkbox:
    baseURL2 = ReadConfig.getApplicationURL2()

    def test_checkbox_sunday(self, driver):
        self.driver = driver
        self.driver.get(self.baseURL2)
        self.driver.maximize_window()

        # Locate the checkbox for Sunday
        self.bp = BlogPage1(driver)
        self.bp.clickCheckboxSunday()
        assert self.bp.isCheckboxSundaySelected() == True

    def test_checkbox_monday(self, driver):
        self.driver = driver
        self.driver.get(self.baseURL2)
        self.driver.maximize_window()

        # Locate the checkbox for Monday
        self.bp = BlogPage1(driver)
        self.bp.clickCheckboxMonday()
        assert self.bp.isCheckboxMondaySelected() == True

    def test_checkbox_sunday_uncheck(self, driver):
        self.driver = driver
        self.driver.get(self.baseURL2)
        self.driver.maximize_window()
        self.bp = BlogPage1(driver)
        self.bp.clickCheckboxMonday()

        # Uncheck the checkbox for Sunday
        
        if self.bp.isCheckboxSundaySelected():
            self.bp.clickCheckboxSunday()
        assert self.bp.isCheckboxSundaySelected() == False