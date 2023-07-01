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
from page.launch_page import LaunchPage
from page.launch_page import LaunchPage
from selenium.webdriver.support import expected_conditions as EC
#base driver is an extension of ur driver method
class BaseDriver:
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(4)
            lenOfpage = self.driver.execute("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength")
        if lastCount == pageLength:
            match = True

        time.sleep(4)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = self.wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements
    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element


