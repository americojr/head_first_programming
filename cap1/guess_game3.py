#Exercício do 1 capítulo do livro Use a cabeça programação - usando randint

from random import randint
secret = randint(1,10) #O randint gera um número aleatório entre 1 e 10
guess = 0

print("Welcome!")

while guess != secret:
        
        g = input("Guess the number: ")

        guess = int(g)

        if guess == secret:
                print("You win!")

        else:
                if guess > secret:
                        print("Too high")
                else:
                        print("Too low")

print("Game Over!")
