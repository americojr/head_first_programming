#Exercício capítulo 4 - manipulando dados em arquivos e arrays

scores = []

# A ideia desta v2 é usar o file handle(result_f) de outra forma e, armazenar a linha num array ao invés de fazer atribuição múltipla de variáveis

result_f = open("results.txt")

while True:
    line = result_f.readline()
    if not line: break
    info = line.split()
    scores.append(float(info[1]))

result_f.close()

scores.sort(reverse=True)

print("The top scores were:")

print(scores[0])
print(scores[1])
print(scores[2])



