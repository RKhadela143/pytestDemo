import pytest

from pageObjects.HomePage import HomePage
from helpers.BaseClass import BaseClass
from TestData.HomePageData import HomePageData

class TestHomePage(BaseClass):

    def test_formSubmission(self, firstname, lastname):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(firstname)
        homepage.getEmail().send_keys(lastname)

        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), "Female")

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    # @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    # def getData(self, request):
    #     return request.param