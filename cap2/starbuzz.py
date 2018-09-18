#Exercício do capítulo 2 - Starbuzz café

import urllib.request 

page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices.html")

text = page.read().decode("utf8")

price = text[234:238] #Extrai uma substring de text. O primeiro valor é referente ao primeiro caractere da substring e, o segundo valor é o índice após o último caractere.

print(price)
