import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_option=Options()
chrome_option.add_argument("--headless")
import time
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(options=chrome_option, executable_path=ChromeDriverManager().install())
        #cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
    def test_search(self):
        self.driver.get('https://www.seleniumeasy.com/test/')
        self.assertEqual(self.driver.title,'Selenium Easy - Best Demo website to practice Selenium Webdriver Online')
    def test_msg(self):
        self.driver.get('https://www.seleniumeasy.com/test/')
        wait=WebDriverWait(self.driver,10)
        element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='at-cv-lightbox-button-holder']/a[2]")))
        element.click()
        self.driver.find_element_by_xpath(
            "//*[@id='navbar-brand-centered']/ul/li[@class='dropdown']/a[@class='dropdown-toggle']").click()
        simple_form = self.driver.find_element_by_xpath(
            "//*[@id='navbar-brand-centered']/ul[1]/li[1]/ul/li/a[@href='./basic-first-form-demo.html']").click()
        msg = 'How are you?'
        e_m = self.driver.find_element_by_xpath("//div[@class='form-group']/input[@id='user-message']").send_keys(
            msg)
        s_m = self.driver.find_element_by_xpath("//form[@id='get-input']/button[@class='btn btn-default']").click()
        text1 = self.driver.find_element_by_xpath("//div[@id='user-message']/span[@id='display']").text
        self.assertEqual(text1,msg)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='UnitTest/Report_unit_test/example_dir'))
