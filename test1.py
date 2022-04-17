from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#

# s=Service('C:\TestFiles\chromedriver.exe')
# browser = webdriver.Chrome(service=s)
# url='https://www.google.com'
# browser.get(url)

#tu leci błąd DeprecationWarning:
# driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')
# driver.get('https://tvn24.pl')
# title = driver.title
# print(title)


#ten działa:
from selenium.webdriver.chrome.service import Service
s = Service('C:\TestFiles\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://tvn24.pl')
title = driver.title
print(title)



# time.sleep(5)
# # search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)