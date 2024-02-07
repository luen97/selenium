import csv, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ddt import ddt, data, unpack


# Creamos primero la función para leer el csv

def get_data(file_name):
    rows = []
    data_file = open(file_name,'r')
    reader = csv.reader(data_file)

    #Saltamos la cabecera
    next(reader,None)

    for row in reader:
        rows.append(row)

    return rows


@ddt
class SearchCsvDDT(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        #cls.driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver') Esto abre es chromium
        driver = cls.driver
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')
        

    @data(*get_data('testdata2.csv'))
    @unpack

    def test_search_ddt(self,search_value,expected_count):
        driver = self.driver

        print(search_value,expected_count)
        
    @data(*get_data('testdata2.csv'))
    @unpack
    def test_search_ddt2(self,search_value,expected_count):
        driver = self.driver

        print(search_value,expected_count)



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)

