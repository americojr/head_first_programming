#Exercício do 1 capítulo do livro Use a cabeça programação

print("Welcome!") #A função print exibe a mensagem entre ""(aspas) na tela

g = input("Guess the number: ") #A função input exibirá a mensagem entre aspas e vai receber a entrada do usuário.

# Essa entrada do usuário será atribuída a variável g através do sinal de atribuição "=". Lembre-se que =(atribuição) e ==(igualdade) são diferentes em programação.
# Uma variável é um "rótulo" para o dado

guess = int(g) #Como a função input por default retorna uma string, transformamos a informação de "g" em um número inteiro e atribuímos a variável "guess".

#A linha acima poderia ser removida se colocássemos um int() antes do input.
# Se nós não transformarmos "g" em int o computador vai entender a entrada como uma letra. Dessa forma, mesmo que fosse digitado "5", o computador diria que você perdeu. Por que? Por que ele entende que se duas partes de informação são de "tipos" diferentes, não há nenhum mode de serem iguais.

if guess == 5: #Faz uma comparação entre o conteúdo da variável "guess" e o número 5. Uma condição de um desvio tem o valor True ou False.

#Caminho True
	print("You win!")
else:
#Caminho False
        if guess > 5:
                print("Too high")
        else:
                print("Too low")

print("Game Over!")
