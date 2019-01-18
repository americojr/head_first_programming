#Exercício capítulo 5 - colocando os dados em seu lugar


# A estrutura de dados conhecida como hash({}) é uma variável que tem duas colunas, o que permite fazer associação entre dados

# Assim, através do hash é possível fazer a relação entre pontuação e surfista

scores = {} #criação do hash

result_f = open("results.txt")

for line in result_f:

    (name, score) = line.split()
# Associação chave valor scores[key] = value
    scores[score] = name

result_f.close()

print("The top scores were:")

#O método keys() retorna um array de chaves do hash. Também existe um método chamado values() que retorna os valores.
for each_score in sorted(scores.keys(),reverse = True):
    
    print("Surfer "+scores[each_score]+" had a score of "+each_score)



