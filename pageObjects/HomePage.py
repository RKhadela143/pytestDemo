from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")


    def shopItems(self):
        self.driver.find_element(self.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(self.name)

    def getEmail(self):
        return self.driver.find_element(self.email)

    def getCheckBox(self):
        return self.driver.find_element(self.check)

    def getGender(self):
        return self.driver.find_element(self.gender)

    def submitForm(self):
        return self.driver.find_element(self.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(self.successMessage)