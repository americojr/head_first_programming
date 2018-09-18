#Exercício do capítulo 2 - Starbuzz com preço para cliente fidelidade

import urllib.request

page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")

text = page.read().decode("utf8")

position = text.find('>$')

first = position + 2 #início do preço
last = first + 4 #final do preço

price = text[first:last]

print(price)
