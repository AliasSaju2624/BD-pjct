import pytest
import csv
from selenium.webdriver.common.by import By 
import logging
from baseClass import BaseClass

class TestLogin(BaseClass):
    @pytest.mark.usefixtures("setup")  # Use setup fixture in the test class
    def test_login(self):
        try:
            driver = self.driver
            username_input = driver.find_element(By.NAME, 'name')
            username_input.send_keys('JohnDoe1')

            password_input = driver.find_element(By.NAME, 'password')
            password_input.send_keys('JohnDoe1')

            login_button = driver.find_element(By.NAME, 'sign-in')
            login_button.click()

           
        except Exception as e:
            logging.error("Error occurred during login")
            logging.error(e)
            assert False, "Login failed" + str(e)