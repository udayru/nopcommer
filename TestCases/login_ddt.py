import time

import pytest
from utiites.readproperties import readdata
from pageObject.LoginPage import Login
from utiites import xlutilites
import openpyxl


class Test_login_ddt:
    url = readdata.seturl()
    path = "./testData/logn.xlsx"
    sheet = "Sheet1"

    def test_login_dtt(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Login(self.driver)
        result = []
        rownum = xlutilites.getRowCount(self.path, self.sheet)
        for r in range(2, rownum + 1):
            self.username = xlutilites.readData(self.path, self.sheet, r, 1)
            self.password = xlutilites.readData(self.path, self.sheet, r, 2)
            self.exp = xlutilites.readData(self.path, self.sheet, r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.Clicklogin()
            time.sleep(5)
            tile = self.driver.title
            if tile == "Dashboard / nopCommerce administration":
                # xlutilites.writeData(self.path, self.sheet, r, 3,"pass")
                if self.exp == "pass":
                    time.sleep(10)
                    self.lp.Clicklogout()
                    result.append('pass')
                elif self.exp == "fail":
                    self.lp.Clicklogout()
                    result.append('fail')

            elif tile != "Dashboard / nopCommerce administration":
                # xlutilites.writeData(self.path, self.sheet, r, 3, "fail")
                if self.exp == "fail":
                    result.append('pass')
                elif self.exp == "pass":
                    result.append('fail')

        self.driver.close()
        if "fail" not in result:
            print("test is passed")
        else:
            print("test is fail")
