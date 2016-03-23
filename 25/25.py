#!/usr/bin/env python3


values = {}
for i in range(15):
	weight = int(input())
	values[i] = [weight, weight]
f = []
for i in range(15):
	f.append([0 for j in range(5000)])
for i in range(1, 15):
	for j in range(1, 5000):
		if j-values[i][0] >= 0 :
			f[i][j] = max(f[i-1][j], f[i-1][j-values[i][0]]+values[i][1])
		else:
			f[i][j] = f[i-1][j]
print(f[14][4999])
