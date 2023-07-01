import logging
import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from page.Search_flight_results_page import SearchFlightResults
from utilities.utils import Utils
#C:\Users\nongp\PycharmProjects\Test Framework Demo> pytest -v --browser chrome url https://be.trip.com/?locale=nl_b

class LaunchPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver): #definind a constructor
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait

        #locator
    DEPART_FROM_FIELD = "//span[@aria-expanded='true']//b[@role='presentation']"
    GOING_TO_FIELD = "//span[@aria-expanded='true']//span[@role='presentation']"
    GOING_TO_RESULT_LIST = "//li[normalize-space()='Select your Destination']"
    SELECT_DATE_FIELD = "//td[normalize-space()='24']"
    ALL_DATES = "//input[@id='DepartDate']"
    SEARCH_BUTTON = "//button[@id='findFlights']"


    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)
    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def getGoingToField (self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD )

    def getGoingToResults(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getDepartureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_BUTTON)

    def enterGoingToLocation(self, goingtolocation):
        self.getDepartFromField().click()
        self.log.info("Clicked on going to")
        time.sleep(2)
        self.getGoingToField().send_keys(goingtolocation)
        self.log.info("Type text into going to field successfully")
        time.sleep(2)
        search_results = self.getGoingToResults()
        for results in search_results:
            if goingtolocation in results.text:
                results.click()
                break


    def enterDepartureDate(self, departuredate):
        self.getDepartureDateField().click()
        all_dates = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("date.date") == departuredate:
                date.click()
                break
    def clickSearchFlightsButton(self):
        self.getSearchButton().click()
        time.sleep(4)

    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        self.clickSearchFlightsButton()
        search_flights_result = SearchFlightResults(self.driver)
        return search_flights_result

