import time
from selenium import webdriver
chrome_browser=webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/')
chrome_browser.implicitly_wait(10)
#a=chrome_browser.find_element_by_xpath("//*[@id='at-cv-lightbox-button-holder']/a[2]").click()
chrome_browser.find_element_by_xpath("//*[@id='navbar-brand-centered']/ul/li[@class='dropdown']/a[@class='dropdown-toggle']").click()
simple_form=chrome_browser.find_element_by_xpath("//*[@id='navbar-brand-centered']/ul[1]/li[1]/ul/li/a[@href='./basic-first-form-demo.html']").click()
msg='How are you?'
e_m=chrome_browser.find_element_by_xpath("//div[@class='form-group']/input[@id='user-message']").send_keys(msg)
s_m=chrome_browser.find_element_by_xpath("//form[@id='get-input']/button[@class='btn btn-default']").click()
text1=chrome_browser.find_element_by_xpath("//div[@id='user-message']/span[@id='display']").text
if  msg==text1:
    print("Message shows properly")
else:
    print("something went wrong")
time.sleep(5)
print(chrome_browser.title)
chrome_browser.close()