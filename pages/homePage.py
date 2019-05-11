class HomePage():

    def _init_(self,driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"

    def click_welcome(self):
        self.driver.find_element_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_id(self.logout_link_linkText).click()