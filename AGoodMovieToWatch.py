from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Weryfikacja poprawności logowania na stronie agoodmovietowatch.com

driver_service = Service(executable_path="C:\TestFiles\chromedriver.exe")
# driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

driver.get("https://agoodmovietowatch.com/")
print(driver.current_url)
time.sleep(2)

driver.maximize_window()
consent_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[4]/div/h6").click()
time.sleep(2)

login_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/div[5]/div[2]/input")
login_field.send_keys("kotofor")
time.sleep(2)

password_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/div[6]/div[2]/input")
password_field.send_keys("test1234!")
time.sleep(3)

login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/div[8]/div").click()
time.sleep(3)

driver.quit()

