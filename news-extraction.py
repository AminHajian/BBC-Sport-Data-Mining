import os
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
firefox_driver = os.path.join(os.getcwd(), 'drivers', 'geckodriver.exe')
firefox_service = Service(firefox_driver)
firefox_options = Options()
firefox_options.set_preference('general.useragent.override', user_agent)
firefox_options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

# # Launch Firefox browser
browser = webdriver.Firefox(service=firefox_service, options=firefox_options)
browser.get("https://www.bbc.com/sport")

page_source = browser.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find all <span> tags with role="text"
news = soup.find_all("span", attrs={"role": "text"})

for item in news:
    text = item.text
    url = item.find_parent('a')['href'] if item.find_parent('a') else None
    url = "https://www.bbc.com" + url
    print("Text:", text)
    print("URL:" , url)



















# refresh_interval = 10
# previous_page_source = browser.page_source
# while True:
#     browser.refresh()
#     # time.sleep(10)
#     current_page_source = browser.page_source
#     if current_page_source != previous_page_source:
#         print("changed")
#     else :
#         print ("Not changed")
    
    
    
#     previous_page_source = current_page_source

#     WebDriverWait(browser, refresh_interval).until(
#         EC.presence_of_element_located((By.TAG_NAME, "body"))
#     )












# Refresh the page every 10 seconds
# while True:
#     time.sleep(10)  # Delay for 10 seconds
#     browser.refresh()





# Remember to close the browser when you're done
# browser.quit()
