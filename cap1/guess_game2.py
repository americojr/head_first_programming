#Exercício do 1 capítulo do livro Use a cabeça programação - usando while

print("Welcome!")

guess = 1

while guess != 5: #Condição do laço. Caso seja True, o corpo do laço será executado.
        
        g = input("Guess the number: ")

        guess = int(g)

        if guess == 5:
                print("You win!")

        else:
                if guess > 5:
                        print("Too high")
                else:
                        print("Too low")

print("Game Over!")

#A grande diferença entre um desvio (if/else) e um laço (while/for) é quantas vezes ele executa o código associado.
#O desvio executará o seu código apenas uma vez, ao passo que o código do laço será executado tantas vezes quanto sua condição for verdadeira.
