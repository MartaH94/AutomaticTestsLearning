from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path="C:\TestFiles\chromedriver.exe")
# driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)


driver.get("https://www.flightradar24.com/")

driver.quit()