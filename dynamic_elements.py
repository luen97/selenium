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
        driver.find_element(by=By.LINK_TEXT,value='Disappearing Elements').click()

    def test_add_remove(self):

        driver = self.driver
        elements_list = WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.TAG_NAME,'li')))
        # elements_list = driver.find_element(by=By.TAG_NAME,value='li')
        # elements_list = driver.find_elements_by_tag_name('li')

        intentos = 1
        print(', '.join(list(map(lambda s: s.text,elements_list))))

        while len(elements_list) < 5:

            intentos += 1
            print(', '.join(list(map(lambda s: s.text,elements_list))))
            driver.refresh()
            ## Pilas aquí con el plural del método de EC, así encuentra todos los
            # elementos que cumplen la condicion y nos permite iterar en ellos
            elements_list = WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.TAG_NAME,'li')))

        print(', '.join(list(map(lambda s: s.text,elements_list))))
        print(f'Se logró en {intentos} intentos')

    def tearDown(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)