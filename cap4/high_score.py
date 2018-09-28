#Exercício capítulo 4 - manipulando dados em arquivos e arrays

scores = []

result_f = open("results.txt")

for line in result_f:

    (name, score) = line.split()

    scores.append(score)

result_f.close()

print("The top scores were:")

print(scores[0])
print(scores[1])
print(scores[2])



