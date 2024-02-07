import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        #cls.driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver')
        driver = cls.driver
        driver.get('http://demo.onestepcheckout.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)


    def test_select_language(self):
        exp_options = ['English','French','German']
        act_options = []
        
        #para acceder a las opciones del dropdown, abre el dropdown
        select_language = Select(self.driver.find_element_by_id('select-language'))

        #Comprobamos que hayan3 idiomas
        self.assertEqual(3, len(select_language))

        for option in select_language.options:
            act_options.append(option.text)

        #Comprobamos que la lista desplegada sea igual a la correcta
        self.assertListEqual(exp_options, act_options)

        #Comprobamos que English sea la primera opción (por defecto?)
        self.assertEqual('English', select_language.first_selected_option.text)

		#seleccionamos "German" por el texto visible
        select_language.select_by_visible_text('German')

        #Verificamos que cambiaramos a Alemán viendo el url
        self.assertTrue('store=german'in self.driver.current_url)

        #Nos cambiamos a inglés seleccionando el primer elemento de la lista
        select_language = Select(self.driver.find_elements_by_id('select-language'))
        select_language.select_by_index(0)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)

