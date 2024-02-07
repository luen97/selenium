import unittest
from selenium import webdriver


"""Esto lo importamos para el find_element"""
from selenium.webdriver.common.by import By

"""Esta excepción sirve para cuando queremos validar
la presencia de un elemento"""
from selenium.common.exceptions import NoSuchElementException  


class AssertionsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        #cls.driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver')
        driver = cls.driver
        driver.get('http://demo.onestepcheckout.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)


    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME,"q"))


    # def test_language_option(self):
    #     self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    """Función de utilidad para identificar cuando 
    un elemento está presente de acuerdo a sus paráms
    how: indica tipo de selector
    what: indica el valor"""
    def is_element_present(self,how,what):

        # Si encuentra elemento True, sino False
        # Usaría (self,selector, value)
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)

