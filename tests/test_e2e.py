from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from helpers.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        # log = self.test_getLogger()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopItems()
        # log.info("Getting all the card titles")


        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter().click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        # time.sleep(5)
        self.linkText("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = (self.driver.find_element_by_css_selector(".alert-success").text)
        print(textMatch)

        assert ("Success! Thank you!" in textMatch)