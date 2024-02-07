import unittest
from selenium import webdriver



class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        #cls.driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver')
        driver = cls.driver
        driver.get('http://demo.onestepcheckout.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enable(self):
        search_field = self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')

        """Validaciones en el código para verificar que una condición 
        de cumple o no
        Aquí verificaremos que sean 3 imagenes en los banners"""
        self.assertEqual(3, len(banners))

    """usamos este cuando no hay ni class name ni id ni nada más, último recurso
    además esto puede cambiar si la webpage cambia; se da nuevo xpath"""
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div[1]/div[2]/div[2]/div/div/div[2]/div/ul/li[4]/a/img')

    def test_shopping_cart(self):
        """Tomé el tag y la clase tag.class_name para atrapar el ícono del carrito"""
        shopping_cart_icon = self.driver.find_elements_by_css_selector("div.header-minicart span.icon")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)

