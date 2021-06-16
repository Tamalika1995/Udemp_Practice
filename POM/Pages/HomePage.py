from POM.Locators.HomePageLocator import homePageLoc
class homepage():
    def __init__(self,driver):
        self.driver=driver
        self.welcome_xpath=homePageLoc.welcome_xpath
        self.logout_xpath=homePageLoc.logout_xpath

    def welcome(self):
        self.driver.find_element_by_xpath(self.welcome_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()
