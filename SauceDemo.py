from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_service = Service(executable_path="C:\TestFiles\chromedriver.exe")
# driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

#loging in and finishing order processing

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(1)

current_url = driver.current_url
print(current_url)

userName = driver.find_element(By.NAME, "user-name").send_keys("standard_user")
time.sleep(1)

password = driver.find_element(By.NAME, "password").send_keys("secret_sauce")
time.sleep(1)

login_button = driver.find_element(By.NAME, "login-button").click()
time.sleep(1)

add_to_cart = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").click()
time.sleep(1)

cart = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a").click()
time.sleep(1)

checkout_button = driver.find_element(By.NAME, "checkout").click()
time.sleep(1)

first_name = driver.find_element(By.NAME, "firstName").send_keys("Jan")
last_name = driver.find_element(By.NAME, "lastName").send_keys("Testowy")
post_code = driver.find_element(By.NAME, "postalCode").send_keys("123!@#")
time.sleep(1)
continue_button = driver.find_element(By.NAME, "continue").click()
time.sleep(1)

finish_button = driver.find_element(By.NAME, "finish").click()
time.sleep(1)

back_home = driver.find_element(By.ID, "back-to-products").click()
time.sleep(2)

if current_url == "https://www.saucedemo.com/inventory.html":
    print("URL is same as before starting order")
else:
    print("URL is different than before starting order")

driver.close()
