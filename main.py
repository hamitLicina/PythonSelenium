from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
'''
driver.get("https://www.google.com/")   # URL of google search page
time.sleep(2)  # Wait for 2 seconds
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "q")))
input_element_by_name = driver.find_element(By.NAME, "q")  # Search for selenium
print(input_element_by_name.get_attribute("name"))  # Print the name of the input element

input_element_by_name.send_keys("hamit licina")  # Send the keys to the input element
time.sleep(2)  # Wait for 2 seconds
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "btnK")))
search_button = driver.find_element(By.NAME, "btnK")  # Search for the search button 
time.sleep(2)  # Wait for 2 seconds
WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "btnK")))
search_button.click()  # Click the search button
'''
driver.get("https://atilsamancioglu.com")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")))
blog_page = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")
blog_page.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button")))
# read_buttons = driver.find_elements(By.CLASS_NAME, "button")
read_button = driver.find_element(By.CLASS_NAME, "button")
read_button.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button")))
article_list = driver.find_elements(By.CLASS_NAME, "button")
print(f"Atil Samancioglu has {len(article_list.text.splitlines())} blog posts!!!")

# while True:
#     continue
