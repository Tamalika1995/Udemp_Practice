from POM.Locators.LoginPageLocator import loginPageLoc
class loginpage():
    def __init__(self,driver):
        self.driver=driver
        self.username_xpath=loginPageLoc.username_xpath
        self.password_xpath=loginPageLoc.password_xpath
        self.login_xpath=loginPageLoc.login_xpath
    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.username_xpath).clear()
        self.driver.find_element_by_xpath(self.username_xpath).send_keys(username)
    def enter_psswrd(self,password):
        self.driver.find_element_by_xpath(self.password_xpath).clear()
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)
    def login(self):
        self.driver.find_element_by_xpath(self.login_xpath).click()
