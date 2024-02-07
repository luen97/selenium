import csv, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 
from ddt import ddt, data, unpack

from time import sleep 

@ddt
class SearchDDT(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        # cls.driver = webdriver.Chrome(executable_path= './geckodriver')
        #cls.driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver') Esto abre es chromium
        driver = cls.driver
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get('https://www.colombiaenmapas.gov.co/?e=-85.86663681749562,0.6232744283930004,-62.22405869250189,18.46640601723434,4686&b=igac&u=0&t=23&servicio=5&cescala=1:100.000')
        
    # WHERE WE GET THE DATA
    # @data(('dress',4),('music',5))
    # @unpack
    def test_search_ddt(self):
        driver = self.driver

        # storing the current window handle to get back to dashboard
        main_page = driver.current_window_handle  

        # escala

        # escala = driver.find_element(by=By.XPATH, value = '/html/body/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div[2]/p[2]/span/span[1]/span/ul/li/input')
        # escala.send_keys('10000')
        sleep(5)

        # Intento de escala escogiendo el selector, pero no da        
        # select_language = Select(
        #     self.driver.find_element(
        #         by=By.XPATH,value='/html/body/div[1]/div[1]/div/div/div/div[2]/div[5]/div[6]/div[3]/div[3]/label/select'
        #         ))
        #         # print(len(select_language))
        # select_language.select_by_index(3) 
        # sleep(2)


        # Entramos a la imagen que queremos descargar
        boton = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[1]/div/div/div/div[2]/div[5]/div[5]/div[2]')
        boton.click()

        # Seleccionamos el formato de descarga shp
        boton_formato_descarga = Select(driver.find_element(by=By.XPATH,value='//*[@id="detalleCartoDescargaFormato"]'))
        boton_formato_descarga.select_by_index(3) 
        sleep(2)
        # cartolist = self.driver.find_element(by=By.ID, value='searchCartoList')
        # print(len(cartolist))
        # remove_button = WebDriverWait(driver,5).until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/div[4]/div[5]/div[1]/div/div')
        #         ))
        # remove_button.click()

        # Download

        boton_download = driver.find_element(by=By.XPATH,value='//*[@id="detalleCartoDescarga"]/button')
        boton_download.click()

        #Iniciamos sesión google
        boton_login = driver.find_element(by=By.XPATH,value='//*[@id="authContainer"]/div/div[1]/form/ul/li[1]/button')
        boton_login.click()

        # changing the handles to access login page
        for handle in driver.window_handles:
            if handle != main_page:
                login_page = handle

        # change the control to signin page        
        driver.switch_to.window(login_page)
        
        # user input for email and password
        email = 'manalgom'

        

        # enter the email
        # driver.find_element_by_xpath('//*[@id ="identifierId"]').send_keys(email)
        driver.find_element(by=By.XPATH, value = '//input[@type="email"]').send_keys(email)

        # click en siguiente
        # driver.find_element(by=By.XPATH,value="//span[text()=='Siguiente']").click()
        driver.find_element(by=By.XPATH,value='//*[@id="identifierNext"]/div/button/span').click()
        sleep(5)
        # enter the password
        driver.find_element(by=By.XPATH, value = '//input[@type="password"]').send_keys(password)
        # click en siguiente
        driver.find_element(by=By.XPATH,value='//span[text()=="Siguiente"]').click()
        sleep(5)
        # click the login button
        driver.find_element_by_xpath('//*[@id ="u_0_0"]').click()

        sleep(5)
        # change control to main page
        driver.switch_to.window(main_page)
        
        sleep(10)



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
