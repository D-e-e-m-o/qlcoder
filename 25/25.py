#!/usr/bin/env python3

cin = open('input', 'r')
values = {}
for i in range(15):
	weight = int(cin.readline())
	values[i+1] = [weight, weight]
f = []
for i in range(16):
	f.append([0 for j in range(5001)])
for i in range(1, 16):
	for j in range(1, 5001):
		if j-values[i][0] >= 0:
			f[i][j] = max(f[i-1][j], f[i-1][j-values[i][0]]+values[i][1])
		else:
			f[i][j] = f[i-1][j]
print(f[15][5000])

i = 15
j = 5000
while i > 0 and j >= 0:
	if j - values[i][0] >= 0 and f[i][j] == f[i - 1][j - values[i][0]] + values[i][1]:
		print([i, values[i][0]])
		j -= values[i][0]
	i -= 1
