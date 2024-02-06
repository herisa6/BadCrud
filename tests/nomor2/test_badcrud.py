import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class loginTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # option = webdriver.EdgeOptions()
        # option.add_argument('--headless')
        # self.browser = webdriver.Edge(options=option)
        
        self.browser = webdriver.Edge()
        # extension_path = "D:/adblocker.xpi"
        # self.browser.install_addon(extension_path)
        # self.addCleanup(self.browser.quit)

    def test_1_home_check(self):
        self.browser.get('http://localhost/BadCRUD/login.php')
        expected_result = "Login"        
        actual_result = self.browser.title
        self.assertIn(expected_result, actual_result)

    def test_2_login_page(self):           
        expected_result = "Dashboard"
        self.browser.find_element(By.ID, "inputUsername").send_keys("admin")
        self.browser.find_element(By.ID, "inputPassword").send_keys("namin66!")
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()      
        actual_result = self.browser.title         
        self.assertIn(expected_result, actual_result)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 