inputs = [3.6, 7.9, 5.2]
weights = [4.6, 8.0, 9.3]

bias = 3

output = sum(map(lambda e: e[1] * weights[e[0]], enumerate(inputs))) + bias
print(output)
