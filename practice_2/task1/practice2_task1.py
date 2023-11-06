import numpy as np
import json

matrix = np.load("matrix_18.npy")
# print(matrix)
size = len(matrix)

matrix_stat = dict()
matrix_stat['sum'] = matrix.sum()
matrix_stat['avr'] = matrix_stat.get("sum")/matrix.size
matrix_stat['sumMD'] = matrix.trace()
matrix_stat['avrMD'] = matrix_stat['sumMD']/size
matrix_stat['sumSD'] = matrix[::-1].trace()
matrix_stat['avrSD'] = matrix_stat['sumSD']/size
matrix_stat['max'] = matrix.max()
matrix_stat['min'] = matrix.min()

print(matrix_stat)

for key in matrix_stat.keys():
    matrix_stat[key] = float(matrix_stat[key])

with open("matrix_stat.json", "w") as result:
    result.write(json.dumps(matrix_stat))

norm_matrix = np.ndarray((size, size), dtype=float)

for i in range(0, size):
    for j in range(0, size):
        norm_matrix[i][j] = matrix[i][j]/matrix_stat['sum']

print(norm_matrix.sum())
np.save("norm_matrix", norm_matrix)
