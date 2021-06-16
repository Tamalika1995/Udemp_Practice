from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/')
driver.implicitly_wait(10)
time.sleep(5)
print(driver.title)
driver.close()