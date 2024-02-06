import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        expected_result = "Wrong usename or password"
        self.browser.find_element(By.ID, "inputUsername").send_keys("admin")
        self.browser.find_element(By.ID, "inputPassword").send_keys("herisa")
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        label_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/form/div/label"))
        )
        actual_result = label_element.text
        self.assertIn(expected_result, actual_result)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 