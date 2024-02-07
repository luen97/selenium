from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    
    """En setUp: Preparativos para la prueba
    test: Acciones del test
    tearDown: Cierre de ventana
    Añadimos el @classmethod y cambiamos self por cls
    para que las operaciones se hagan en una misma
    ventana del navegador"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, 
    testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

