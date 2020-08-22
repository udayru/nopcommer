import time

import pytest
from selenium import webdriver
from pageObject.LoginPage import Login
from utiites.readproperties import readdata
from utiites import xlutilites



class Test_001_login:

    baseUrl = readdata.seturl()
    username = readdata.setusername()
    password = readdata.setpassword()
    path="./testData/testlogindata.xlsx"
    sheet="Sheet1"

    def test_homePageTitle(self, setup):

        self.driver = setup
        self.driver.get(self.baseUrl)
        act_Title = self.driver.title


        if act_Title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./screenShots/" + "test_loginhomrpage.png")
            self.driver.close()
            assert False

