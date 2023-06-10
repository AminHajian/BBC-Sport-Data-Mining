import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s = Service('C:\\Program Files\\Mozilla Firefox\\geckodriver.exe')

driver = webdriver.Firefox(service=s)
driver.get("https://corbah.com/")

driver.refresh()