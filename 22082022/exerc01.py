import numpy as np
N = 10
s2 = 0
vtr = np.zeros(N)
for i in range(N):
    vtr[i] = float(input(f'informe um valor [{i}]: '))
#s2 = vtr.sum()
for i in range(N):
    s2 = s2+vtr[i]
print(f'A soma é: {s2}')