from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_service = Service(executable_path="C:\TestFiles\chromedriver.exe")
# driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

driver.get("https://www.discuvver.com/")

time.sleep(2)

przycisk = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/button")
przycisk.click()

time.sleep(4)
driver.quit()