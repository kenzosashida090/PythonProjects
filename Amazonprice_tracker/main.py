
import requests
import smtplib
import lxml

from bs4 import  BeautifulSoup
URL = "https://www.amazon.com.mx/Sgt-Peppers-Lonely-Heart-Vinyl/dp/B076W8Y6BB/ref=sr_1_1?keywords=sargent+pepper+vinyl&qid=1664260083&qu=eyJxc2MiOiIwLjAwIiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=sargents+peppe%2Caps%2C96&sr=8-1"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50",
    "Accept-Language": "es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5"

}
response = requests.get(URL,headers=headers)

soup = BeautifulSoup(response.content, "lxml")

price = float(soup.find("span", class_ = "a-price-whole").getText().replace('.',''))
print(price)
my_email = "kenzosashida5@gmail.com"
price_message = f"The album has a price of {price}"
password = "tkbftknaxpicleva"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
if price < 650.0 :

    connection.sendmail(from_addr=my_email,to_addrs="kenzosashida1@gmail.com",msg =price_message )
