#Jogo de perguntas e respostas

import play_music


nperguntas = 0
ncorretas = 0
nerradas = 0

resp = 3

while resp != 0:

    nperguntas += 1

    resp = int(input("Digite 1 para resposta certa, 2 para errada e 0 para encerrar: "))

    if resp == 1:
        play_music.play("correct.wav")
        ncorretas += 1
    elif resp == 2:
        play_music.play("wrong.wav")
        nerradas += 1

print("O numero de respostas certas foi: ",ncorretas)
print("O numero de respostas erradas foi: ",nerradas)
print("O numero de perguntas foi: ",nperguntas-1)


