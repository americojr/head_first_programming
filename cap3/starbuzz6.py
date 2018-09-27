#Exercício Capítulo 3

import urllib.request
import time

def get_price():

    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices.html")

    text = page.read().decode("utf8")

    where = text.find(">$")

    start_of_price = where + 2

    end_of_price = start_of_price + 4

    return(float(text[start_of_price:end_of_price]))

