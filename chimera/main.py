# https://orac.amt.edu.au/cgi-bin/train/problem.pl?problemid=779&set=aio14int
# load data
L = 0
S = 1
G = 2

with open('chimin.txt') as f:
	N = int(f.readline().strip())
	animals = [f.readline().strip(), f.readline().strip(), f.readline().strip()]
	lion = animals[0]
	snake = animals[1]
	goat = animals[2]


result = [None] * N
twosIndices = []

total = [0, 0, 0]

# Add 3s and 2s
for i in range(N):
	if lion[i] == snake[i] == goat[i]:
		result[i] = lion[i]
		total[L] += 1
		total[S] += 1
		total[G] += 1
		continue

	elif lion[i] == snake[i]:
		result[i] = lion[i]
		total[L] += 1
		total[S] += 1

	elif lion[i] == goat[i]:
		result[i] = lion[i]
		total[L] += 1
		total[G] += 1

	elif snake[i] == goat[i]:
		result[i] = goat[i]
		total[S] += 1
		total[G] += 1

	twosIndices.append(i)


# Add 1s
for i in range(N):
	if result[i] == None:
		minIndex = total.index(min(total))
		result[i] = animals[minIndex][i]
		total[minIndex] += 1

# balance
for i in twosIndices:
	minIndex = total.index(min(total))

	if animals[minIndex][i] != result[i]:
		other1 = (minIndex + 1) % 3
		other2 = (minIndex + 2) % 3

		if not (total[other1] > total[minIndex] and total[other2] > total[minIndex]):
			break

		result[i] = animals[minIndex][i]
		total[minIndex] += 1
		total[other1] -= 1
		total[other2] -= 1

with open('chimout.txt', 'w') as f:
	f.write(str(min(total)))
