from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_service = Service(executable_path="C:\TestFiles\chromedriver.exe")
# driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

#Wyszukiwanie na stronie muzyki z serialu "Gra o tron" z 1-go odcinka 1-go sezonu i wykonanie zrzutu ekranu

driver.get("https://www.tunefind.com/")
time.sleep(2)

driver.maximize_window()
print(driver.current_url)

przycisk = driver.find_element(By.XPATH, "//html/body/div[1]/div/div/div/div[2]/div/button[2]").click()
time.sleep(1)

lupa = driver.find_element(By.XPATH, "/html/body/div[3]/div/nav/div/div[2]/div/button").click()

szukanie = driver.find_element(By.XPATH, "/html/body/div[3]/div/nav/div/div[2]/div/div/form/input")
szukanie.send_keys('Game of Thrones')
szukanie.send_keys(Keys.ENTER)
time.sleep(1)

wynik1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/a/div[1]").click()
time.sleep(1)
sezon1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div/ul/li[1]/div/div[1]/h3/a").click()
time.sleep(1)
S1E1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/ul/li[1]/div/div[1]/h3/a").click()
time.sleep(1)

driver.get_screenshot_as_png()
driver.save_screenshot("Test.png")
time.sleep(2)

driver.quit()

