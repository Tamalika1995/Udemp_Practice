from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest
chrome_option=Options()
# chrome_option.add_argument('--headless--')
class TestSample():
    @pytest.fixture()
    def test_setUp(self):
        global driver
        driver=webdriver.Chrome(options=chrome_option,executable_path=ChromeDriverManager().install())
        driver.get('https://opensource-demo.orangehrmlive.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        driver.close()

    def test_login(self,test_setUp):
        driver.find_element_by_xpath('//*[@id="divUsername"]/input').send_keys('Admin')
        driver.find_element_by_xpath('//*[@id="divPassword"]/input').send_keys('admin123')
        driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
        driver.find_element_by_xpath('//*[@id="welcome"]').click()
        driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li/a[@href="/index.php/auth/logout"]').click()
    @pytest.mark.skip
    def test_skip_demo(self):
        print("this is for skip")
    # def test_tearDown():
    #     driver.close()