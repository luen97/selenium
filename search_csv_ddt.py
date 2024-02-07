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

    """los decoradores tomaran la tupla que les llega y meteran sus valores como argumentos de la función
    ¿de la primera función o de todas? Encima de donde se pongan los decoradores, en pruebita se ve cómo"""

    @data(*get_data('testdata.csv'))
    @unpack
    def test_search_ddt(self,search_value,expected_count):
        driver = self.driver

        search_field = driver.find_element(by=By.NAME,value='q')
        search_field.clear() 
		
        search_field.send_keys(search_value)
        search_field.submit()

        # Creo que ese xpath es todas las tags a dentro de los h2 con class product-name
        products = driver.find_elements(by=By.XPATH,value='//h2[@class="product-name"]/a')
        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count,len(products))

        else:
            message = self.driver.find_element(by=By.CLASS_NAME,value='note-msg')
            self.assertEqual('Your search returns no results.',message)

        print(f'Found {len(products)} products')



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)

