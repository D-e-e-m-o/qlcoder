#!/usr/bin/env python3

cin = open('input','r')
values = {}
for i in range(15):
	weight = int(cin.readline())
	values[i] = [weight, weight]
f = []
for i in range(15):
	f.append([0 for j in range(5000)])
for i in range(15):
	for j in range(5000):
		if j-values[i][0] >= 0:
			f[i][j] = max(f[i-1][j], f[i-1][j-values[i][0]]+values[i][1])
		else:
			f[i][j] = f[i-1][j]
print(f[14][4999])

i = 14
j = 4999
while i >= 0 and j >= 0:
	if j - values[i][0] >= 0 and f[i][j] == f[i - 1][j - values[i][0]] + values[i][1]:
		print([i+1, values[i][0]])
		j -= values[i][0]
	i -= 1

