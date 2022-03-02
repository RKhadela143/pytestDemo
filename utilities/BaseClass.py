import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures('setup')
class BaseClass:
    def linkText(self, text):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def test_getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        return logger