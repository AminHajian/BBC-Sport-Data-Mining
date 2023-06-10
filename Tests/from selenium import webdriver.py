from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://arzdigital.com/coins/bitcoin/"

driver_path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"
refresh_interval = 6000

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(executable_path=driver_path, options=options)
driver.get(url)

previous_page_source = driver.page_source

while True:
    driver.refresh()

    current_page_source = driver.page_source
    if current_page_source != previous_page_source:
        print("changed")

    previous_page_source = current_page_source

    WebDriverWait(driver, refresh_interval).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
