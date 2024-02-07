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
        driver.find_element(by=By.LINK_TEXT,value='Add/Remove Elements').click()

    def test_add_remove(self):

        driver = self.driver
        elements_added = int(input('How many elements do you want to create? '))
        elements_removed = int(input('How many elements do you want to remove? '))

        total_elements = elements_added - elements_removed

        add_button = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="content"]/div/button')))


        for i in range(elements_added):
            add_button.click()

                
        for i in range(elements_removed):
            try:
                """A pesar de qut todos los botones creados tienen el nombre de clase
                added-manually, el EC solo toma el primero que encuentra, da lo mismo 
                si lo hacemos con el xpath"""
                delete_button = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME,'added-manually')))
                delete_button.click()
            except:
                print('You\'re trying to delete more elements that the created')

        if total_elements > 0:
            print(f'There are {total_elements} elements on screen')
        else:
            print('There are 0 elements on screen')
        
        sleep(3)

    def tearDown(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)