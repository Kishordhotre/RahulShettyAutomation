from selenium.webdriver.common.by import By

from pageObjects.Checkoutpage import CheckOutPage


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name = 'name']")
    email = (By.NAME, "name")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*Homepage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getname(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getCheckbox(self):
        return self.driver.find_element(*Homepage.check)

    def getgender(self):
        return self.driver.find_element(*Homepage.gender)

    def submitForm(self):
        return self.driver.find_element(*Homepage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*Homepage.successMessage)

