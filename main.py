import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/s?k=shoes+for+men&i=shoes"
proxies = {
    "http" : "http://202.124.43.254"
}
response = requests.get(url, proxies=proxies)
soup = BeautifulSoup(response.text , "html.parser")
for data in soup.find_all(class_="a-size-base-plus a-color-base") :
    print(data.text)
for data in soup.find_all(class_="a-price-whole") :
    print(data.text)

