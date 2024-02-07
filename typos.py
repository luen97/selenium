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
        driver.find_element(by=By.LINK_TEXT,value='Typos').click()

    def test_find_typo(self):

        driver = self.driver
        paragraph_to_check = driver.find_element(by=By.CSS_SELECTOR,value="#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text

        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."
        sleep(3)

        while text_to_check != correct_text:

            tries +=1
            driver.refresh()

            paragraph_to_check = driver.find_element(by=By.CSS_SELECTOR,value="#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            sleep(3)

        print(f"It took {tries} tries to find the typo")




    def tearDown(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)