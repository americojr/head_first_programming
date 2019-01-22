#Exercício do capítulo 7

nperguntas = 0
ncorretas = 0
nerradas = 0

running = True

while running:
    resp = input("Digite 1 para resposta certa e 2 para errada: ")
    nperguntas += 1
    if resp == 1:
        ncooretas += 1
        play aplausos
    if resp == 0:
        running = False  
    else:
        nerradas += 1
        play vaia
print("O numero de respostas certas foi: ",ncorretas)
print("O numero de respostas erradas foi: ",nerradas)
print("O numero de perguntas foi: ",nperguntas)
