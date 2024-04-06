from selenium.webdriver.common.by import By


class CheckoutPage:
    
    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.CSS_SELECTOR, '.card-title a')
    cardFooter = (By.CSS_SELECTOR, '.card-footer button')

    def getCardTitles(self):
        return self.driver.find_elements(self.cardTitles)

    def getCardFooter(self):
        return self.driver.find_element(self.cardFooter)