import logging
import time
from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from page.launch_page import LaunchPage
from utilities.utils import Utils


class SearchFlightResults(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):  # defining a constructor
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait

    #Locators
    FILTER_BY_1_STOP_ICON = "//span[@id='w35']"
    FILTER_BY_2_STOP_ICON = "//span[@id='w35']"
    FILTER_BY_NON_STOP_ICON = "//span[@id='w35']"
    SEARCH_FLIGHT_RESULT = "//span[@id='w35']"
    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULT)


    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            self.log.warning("Selected flights with 1 stop")
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            self.log.warning("Selected flights with 2 stop")
            time.sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click()
            self.log.warning("Selected non stop flights")
            time.sleep(2)
        else:
            self.log.warning("Please provide valid filter option")

    """def filter_flights(self):
        self.driver.find_element(By.XPATH, "//dd[@class='filter-list filter-padding c-filter-common']//dl[@class='filter']//dd[2]//div[1]//label[1]//span[1]//i[1]").click()
        time.sleep(4)"""


