import pytest

from pageObjects.Homepage import Homepage
from utilities.Baseclass import Baseclass


class TestHomePage(Baseclass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = Homepage(self.driver)
        log.info("first name is " + getData["firstname"])
        homepage.getname().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckbox().click()
        self.SelectOptionByText(homepage.getgender(), getData["gender"])
        homepage.submitForm().click()
        alertText = homepage.getSuccessMessage().text
        assert ("success" in alertText)
        self.driver.refresh()



    @pytest.fixture(params=[{"firstname": "Kishor", "lastname": "Dhotre", "gender": "Male"},
                            {"firstname": "Tushar", "lastname": "Patil", "gender": "Male"}])
    def getData(self, request):

        return request.param
