#Exercício capítulo 2

import urllib.request

price = 99.99

while price > 4.74:

    print("Looking for the best price...")
    
    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices.html")

    text = page.read().decode("utf8")

    where = text.find(">$")

    start_of_price = where + 2

    end_of_price = start_of_price + 4

    price = float(text[start_of_price:end_of_price])

print("Buy!")
    
