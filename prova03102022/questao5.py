import numpy as np
n = 5
matriz = np.zeros((n, n), dtype=int)
max = None
pos = 0
for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Informe um valor para a posição {i},{j}: "))
        if max is None or matriz[i][j] > max:
            max = matriz[i][j]
            pos = (i)
min = None
for i in range(n):
    if min is None or [i] < min:
        min = [i]
print(f' Na Matriz:\n{matriz}\nO maior elemento é o: {max} na posição: {pos}. O valor Minimax é: {min}')
