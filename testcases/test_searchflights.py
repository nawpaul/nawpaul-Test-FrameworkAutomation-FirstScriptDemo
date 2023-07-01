#Test case 1 is to test the website
####Fubctional specifications
#Test case manaully is to=
#launch the travel websites
#provide going from location
#provide going to location
#select the departure date
#click on flight search button
#To handle dynamic scroll
#select that the filtered results show flights having only 1 stop
#verify that all the filter results shoes only one stop results
import logging
import time
import pytest
import softest
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.Search_flight_results_page import SearchFlightResults
from page.launch_page import LaunchPage
from page.launch_page import LaunchPage
from utilities.utils import Utils
from base.base_driver import BaseDriver

from ddt import ddt, data, file_data, unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyfilter(softest.TestCase):
    log = Utils.custom_logger(logLevel=logging.WARNING)


    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

   # @data(*Utils.read_data_from_excel("C:\\Users\\nongp\\PycharmProjects\\Test Framework Demo\testdata\tdata.excel.xlsx", "Sheet1")) #you don't have to provide the set of data in the data decorator
    @data(*Utils.read_data_from_csv("C:\Users\\nongp\PycharmProjects\\Test Framework Demo\\testdata\\tdatacsv.csv"))
    @unpack #unpack is not required from reading the value from the testdate using json
    #@file_data("../testdata/testyml.yaml") reading the data from yml
    #@file_data("../testdata/testdata.json") reading the data from the json

    def test_search_flights_1_stop(self, goingfrom, goingto, date, stops):
        search_flights_result = self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.page_scroll()
        search_flights_result.filter_flights_by_stop(stops)
        allstops1 = search_flights_result.get_search_flight_results()
        self.log.info(len(allstops1))
        ut = Utils()
        ut.assertListItemText(allstops1, stops)
"""
    @data(("LHR London Heathrow Airport", "BRU, Brussels Airport, Brussels, Belgium", "16/02/2023", "1 stop"))
    @unpack
    def test_search_flights_2_stop(self, goingfrom, goingto, date, stops):
        search_flights_result = self.lp.searchFlights("LHR London Heathrow Airport", "HEL Helsinki all airports", "16/02/2023")
        self.lp.page_scroll()
        search_flights_result.filter_flights_by_stop(stops)
        allstops1 = search_flights_result.get_search_flight_results()
        self.log.info(len(allstops1))
        ut = Utils()
        ut.assertListItemText(allstops1, stops) """

testflight = TestSearchAndVerifyfilter()
testflight.test_search_flights()



