#Exercício do capítulo 2 - Starbuzz com preço para cliente fidelidade

#Fazendo uma pesquisa de substring de maneira "burra"

import urllib.request
import time

page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")

text = page.read().decode("utf8")

a = 1
b = 3

busca = text[a:b]

while (busca != '>$'):
	
		print("Procurando substring '>$' no intervalo",a,":",b)
		a = a + 1
		b = b + 1
		busca = text[a:b]
		time.sleep(0.1)

inicio = b
fim = b + 4
print("Preço encontrado no intervalo",inicio,":",fim)

price = text[inicio:fim]

print("O preço para cliente fidelidade é: $",price)
