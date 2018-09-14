#Exercício do capítulo 2 - Starbuzz café

import urllib.request

page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices.html")

text = page.read().decode("utf8")

print(text)
