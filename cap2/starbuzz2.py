#Exercício do capítulo 2 - Starbuzz com preço para cliente fidelidade

import urllib.request

page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")

text = page.read().decode("utf8")

price = text[234:238]

print(price)
