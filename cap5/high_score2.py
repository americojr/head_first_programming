###  Exercise ###

scores = []
names = []

result_f = open("results.txt")

for line in result_f:

    (name,score) = line.split()
    scores.append(score)
    names.append(name)

result_f.close()
scores.sort(reverse = True)
names.sort(reverse = True)

print("The top scores were:")

print(names[0])
print(scores[0])
print(names[1])
print(scores[1])
print(names[2])
print(scores[2])

