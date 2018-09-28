#Exercício Capítulo 3

import urllib.request
import time

def get_price():

    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices.html")

    text = page.read().decode("utf8")

    where = text.find(">$")

    start_of_price = where + 2

    end_of_price = start_of_price + 4

    return float(text[start_of_price:end_of_price])


answer = input("Do you want to see the price right now (Y/N)?")

answer.upper()

if answer == "Y":

    print(get_price())

else:
    price = 99.99
    
    while price > 4.74:

        time.sleep(900)

        print("Looking for the best price...")

        price = get_price()

    print("Buy!")
    
