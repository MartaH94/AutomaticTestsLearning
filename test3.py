# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

s=Service(path)
driver=webdriver.Chrome(service=s)
driver.get('https://www.google.com')
driver.find_element(By.NAME, 'q').send_keys('Marta')