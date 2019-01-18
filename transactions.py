#Exercício do capítulo 6

def save_transaction(price, credit_card, description):
    file = open("transactions.txt", "a")
    file.write("%s%07d%s \n" % (credit_card, price * 100, description))
    file.close()

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]

prices = [1.50, 2.0, 1.80, 1.20]

running = True

while running:
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
           
        
        
        
        
        
        
        choice = int(input("Choose an option: "))

