#!/usr/bin/env python3

cin = open('input', 'r')
values = {}
for i in range(15):
	# 反正重量和价值都设置为一样的
	values[i + 1] = int(cin.readline())

f = [0 for v in range(5001)]
for i in range(1, 16):
	for v in range(5000, values[i] - 1, -1):
		f[v] = max(f[v], f[v - values[i]] + values[i])

print(f[5000])
