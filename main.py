# import requests
# from bs4 import BeautifulSoup
# url = "https://www.amazon.in/s?k=shoes+for+men&i=shoes"
# proxies = {
#     "http" : "http://202.124.43.254"
# }
# response = requests.get(url, proxies=proxies)
# soup = BeautifulSoup(response.text , "html.parser")
# for data in soup.find_all(class_="a-size-base-plus a-color-base") :
#     print(data.text)
# for data in soup.find_all(class_="a-price-whole") :
#     print(data.text)


import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext

def scrape_data():
    url = "https://www.amazon.in/s?k=shoes+for+men&i=shoes"
    proxies = {
        "http" : "http://184.95.235.194"
    }
    response = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract data
    titles = [data.text for data in soup.find_all(class_="a-size-base-plus a-color-base")]
    prices = [data.text for data in soup.find_all(class_="a-price-whole")]
    
    return titles, prices

def display_data():
    titles, prices = scrape_data()
    
    text_area.delete(1.0, tk.END)
    
    text_area.insert(tk.END, "Titles:\n")
    for title in titles:
        text_area.insert(tk.END, f"- {title}\n")
    
    text_area.insert(tk.END, "\nPrices:\n")
    for price in prices:
        text_area.insert(tk.END, f"- {price}\n")

root = tk.Tk()
root.title("Amazon Shoes Scraper")

scrape_button = tk.Button(root, text="Scrape Data", command=display_data)
scrape_button.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, width=80, height=20)
text_area.pack(padx=10, pady=10)

root.mainloop()
