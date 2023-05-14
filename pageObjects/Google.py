from logging import getLogger

import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utilities.BaseClass import BaseClass
from utilities.log import get_logger

logger = get_logger()


class GooglePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    search_box = (By.XPATH, "//*[@type='search']")
    search_results = (By.XPATH, "//div[@class='yuRUbf']/a")

    """This function Perform the google sarch with provided test data
        Parameters:
        get_data 
    """

    def perform_google_search(self, get_data):
        self.enter_input_by_locator(get_data["search_data"], *GooglePage.search_box)
        self.enter_input_by_locator(Keys.RETURN, *GooglePage.search_box)
        logger.info("Google searched performed -->{}".format({get_data["search_data"]}))

    """This function return the first test result link
        return:
        str
    """

    def get_first_result_href(self):
        search_results = self.driver.find_elements(*GooglePage.search_results)
        first_result_link = search_results[0].get_attribute("href")
        logger.info(f"first search result is {first_result_link}")
        return first_result_link
