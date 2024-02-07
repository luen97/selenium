import unittest
from selenium import webdriver


"""Esto lo importamos para el find_element"""
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        #cls.driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')
        

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(by=By.NAME,value='q')
        search_field.clear() #limpia el campo de búsqueda en caso de que haya algún texto. 
		
        search_field.send_keys('tee') #simulamos la escritura del teclado para poner "tee"
        search_field.submit() #envía los datos ('tee') para que la página muestre los resultados de "tee"
	
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(by=By.NAME,value='q')
        search_field.clear() 
		
        search_field.send_keys('salt shaker') #escribimos 'salt shaker' en la barra de búsqueda
        search_field.submit() #envíamos la petición

		#hago una lista de los resultados buscando los elementos por su Xpath. Es la forma más rápida.
        #products = driver.find_elements(by=By.XPATH,value='//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li/div/h2/a')
        products = driver.find_elements(by=By.XPATH,value='//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        #products = driver.find_elements(by=By.XPATH,value='//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul')



		#vamos a preguntar si la cantidad de resultados es igual a 1
        self.assertEqual(1, len(products))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)

