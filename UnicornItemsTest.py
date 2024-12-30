import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestUnicornItems(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def test_python_website(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "username")))
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        
        username.send_keys("test")
        password.send_keys("test")

        login = driver.find_element(By.NAME, "login")
        login.click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")))
        # /html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul
        alert = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")
        assert "ERROR: Incorrect username or password" in alert.text
        
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()