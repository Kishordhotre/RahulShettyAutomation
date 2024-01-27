import time

from selenium.webdriver.common.by import By

from pageObjects.Homepage import Homepage
from utilities.Baseclass import Baseclass


class TestOne(Baseclass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = Homepage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitle()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter().click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmpage = checkoutpage.CheckOutItems()
        log.info("Entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.VerifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text
        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)
