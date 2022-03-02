from selenium.webdriver.common.by import By


class CheckoutPage:
    #driver.find_elements_by_css_selector(".card-title a")
    #driver.find_element_by_css_selector(".card-footer button").click()
    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.CSS_SELECTOR, '.card-title a')
    cardFooter = (By.CSS_SELECTOR, '.card-footer button')

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)