#Exercício capítulo 5 - colocando os dados em seu lugar


scores = {} 

result_f = open("results.txt")

for line in result_f:

    (name, score) = line.split()
    scores[score] = name

result_f.close()

print("The top scores were:")

#O método items() retorna o par chave-valor

for score,surfer in sorted(scores.items(),reverse = True):
    
    print(surfer+" had a score of "+score)



