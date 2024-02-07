import csv, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ddt import ddt, data, unpack

from time import sleep 

@ddt
class SearchDDT(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        #cls.driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver') Esto abre es chromium
        driver = cls.driver
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')
        
    # WHERE WE GET THE DATA
    @data(('dress',4),('music',5))
    @unpack

    def test_search_ddt(self,search_value,expected_count):
        driver = self.driver

        search_field = driver.find_element(by=By.NAME,value='q')
        search_field.clear() 
		
        search_field.send_keys(search_value)
        search_field.submit()
        # Ponemos una pausa demostrativa
        sleep(3)

        # Creo que ese xpath es todas las tags a dentro de los h2 con class product-name
        products = driver.find_elements(by=By.XPATH,value='//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count,len(products))



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)

