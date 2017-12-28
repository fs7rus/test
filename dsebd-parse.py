import requests 
import re
from bs4 import BeautifulSoup

URL = "http://www.dsebd.org/latest_share_price_alpha.php"
r = requests.get(URL)
 # Create a BeautifulSoup object
soup = BeautifulSoup(r.content, 'html5lib')
soup.prettify()

try:
    fh = open("company_list.txt", "w")
    fh.write(soup.find_all("div")[1].get_text())
finally:
    fh.close

latest_share_price_alpha_list = []
try:
    with open('company_list.txt', 'r') as file:
        result = file.read()
        for data in result.split():
            latest_share_price_alpha_list.append(data)
finally:
    fh.close()

company_list = []
counter = 0
while counter < len(latest_share_price_alpha_list):
    if counter == 0:
        company_list = latest_share_price_alpha_list[counter]
        print(latest_share_price_alpha_list[counter])
    else:
        company_list = latest_share_price_alpha_list[counter].split("%")
        print(company_list[1])
    counter += 3

