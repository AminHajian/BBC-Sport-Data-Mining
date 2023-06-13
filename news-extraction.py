import os
import time
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import mysql.connector 

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="mmmm1382",
    database="bbc"

)
mycursor = mydb.cursor()
sql = "INSERT INTO news (title, url, publish_date) VALUES (%s, %s ,NOW())"
# val = (["html","kk"])
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")




user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
firefox_driver = os.path.join(os.getcwd(), 'drivers', 'geckodriver.exe')
firefox_service = Service(firefox_driver)
firefox_options = Options()
firefox_options.set_preference('general.useragent.override', user_agent)
firefox_options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

# # Launch Firefox browser
browser = webdriver.Firefox(service=firefox_service, options=firefox_options)
browser.get("https://www.bbc.com/sport")


while True:
    page_source = browser.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all <span> tags with role="text"
    news = soup.find_all("span", attrs={"role": "text"})
    
    for item in news:
        text = item.text
        if text == "Twitter":
            break
        # Check if the news already exists in the database
        mycursor.execute("SELECT * FROM news WHERE title = %s", (text,))
        result = mycursor.fetchone()
        if result is None:
            url = item.find_parent('a')['href'] if item.find_parent('a') else None
            url = "https://www.bbc.com" + url
            # image = open("C:/Users/Amin/Desktop/pp.jpg")
            val = (text, url)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Text:", text)
            print("URL:", url)
        
        mycursor.fetchall()

    browser.refresh()
    time.sleep(10)














