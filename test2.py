from selenium import webdriver

from selenium.webdriver.chrome.service import Service

s = Service('C:\TestFiles\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://tvn24.pl')
title = driver.title
print(title)

assert title == 'Wiadomości z kraju i ze świata - najnowsze informacje w TVN24 - TVN24'

driver.close()
