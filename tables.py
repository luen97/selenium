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
        driver.find_element(by=By.LINK_TEXT,value='Sortable Data Tables').click()

    def test_sort_tables(self):

        driver = self.driver
        num_cols = 5 
        num_rows = 4

        table_data = [[] for i in range(num_cols)] 
        print(table_data)

        for i in range(num_cols):
            header = driver.find_element(by=By.XPATH,value=f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)

            for j in range(num_rows):
                row_data = driver.find_element(by=By.XPATH,value=f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]')
                table_data[i].append(row_data.text)

        print(table_data)






    def tearDown(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)