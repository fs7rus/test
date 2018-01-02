#!/usr/bin/python3

import requests 
import re
import collections
from bs4 import BeautifulSoup
    
def convert_to_html5lib(URL, my_list):
    """
    This function will convert .php file to beautiful html5 soup object.
    Parameter e.g. URL = "http://www.dsebd.org/latest_share_price_alpha.php"
    """    
    r = requests.get(URL)
    # Create a BeautifulSoup object
    soup = BeautifulSoup(r.content, 'html5lib')
    soup.prettify()

    result = soup.find_all("div")[1].get_text()
    for item in result.split():
        my_list.append(item)
    return

details_list = []
convert_to_html5lib("http://www.dsebd.org/latest_share_price_scroll_l.php", details_list)
counter = 0
while counter < len(details_list):
    if counter == 0:
        company_name = details_list[counter]
        counter += 1
    last_trading_price = details_list[counter]
    counter += 1
    last_change_price_in_value = details_list[counter]
    counter += 1
    if details_list[counter].split("%"):
        last_change_price_in_percentage = details_list[counter][0]
        if details_list[counter].split("%")[1]:
            company_name = details_list[counter].split("%")[1]
        counter += 1
        
    print(company_name)
    print(last_trading_price)
    print(last_change_price_in_value)
    print(last_change_price_in_percentage)
