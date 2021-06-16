import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import unittest
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.Pages.LoginPage import loginpage
from POM.Pages.HomePage import homepage
chrome_option=Options()
chrome_option.add_argument("--headless")
class loginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(options=chrome_option, executable_path=ChromeDriverManager().install())
        cls.driver.get('https://opensource-demo.orangehrmlive.com/')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    def test_login(self):
        driver=self.driver
        login=loginpage(driver)
        hmpg=homepage(driver)
        login.enter_username('Admin')
        login.enter_psswrd('admin123')
        login.login()
        hmpg.welcome()
        hmpg.logout()
        self.assertEqual(self.driver.title,"OrangeHRM")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='POM/report'))

