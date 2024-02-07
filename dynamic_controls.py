import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(by=By.LINK_TEXT,value='Dynamic Controls').click()

    def test_test_dynamic_controls(self):

        driver = self.driver

        # remove_button = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.LINK_TEXT,'Remove')))
        # remove_button.click()

        # add_button = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.LINK_TEXT,'Add')))
        # add_button.click()

        remove_button = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="checkbox-example"]/button')))
        remove_button.click()
        sleep(3)

        add_button = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="checkbox-example"]/button')))
        add_button.click()

    def tearDown(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)