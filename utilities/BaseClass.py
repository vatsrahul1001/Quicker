import pytest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.log import get_logger

logger = get_logger()


@pytest.mark.usefixtures("setup")
class BaseClass:
    def explict_wait(
        self, locator, expected_condition, timeout=10, poll_frequency=0.05
    ):
        wait = WebDriverWait(self.driver, timeout), poll_frequency
        if expected_condition == "bytitle":
            wait.until(EC.title_is(locator))
            print("Wait for title successful")
        elif expected_condition == "byclickable":
            wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
            print("Wait for element to be clickable successful")
        elif expected_condition == "visibility":
            wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            print("Wait for element to be clickable successful")

    def find_visible_element_by_locator(
        self, *locator, timeout=40, poll_frequency=0.05
    ):
        element = None

        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located((locator[0], locator[1]))
            )
        except:
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located((locator[0], locator[1]))
            )

        return element

    def enter_input_by_locator(self, text, *locator):
        self.find_visible_element_by_locator(*locator, timeout=40).send_keys(text)

    def click_button_by_text(self, text):
        button_xpath = (By.XPATH, "//button[contains(text(),'" + text + "')]")
        self.find_visible_element_by_locator(*button_xpath).click()

    def click_element_by_locator(self, *locator, timeout=20, poll_frequency=0.05):
        try:
            self.find_visible_element_by_locator(*locator, timeout=40).click()
        except:
            print("in except")
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable((locator[0], locator[1]))
            )

            ActionChains(self.driver).move_to_element(element).click().pause(
                4
            ).perform()
