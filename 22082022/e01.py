# import numpy as np
# N = 5
# vetor = np.zeros(N)
# print(vetor)

import numpy as np
# define o tamanho do array
N = 5
#preenche a estrutura com zeros
vetor = np.zeros(N)
#preenche o vetor com valores do tipo float
for i in range(N):
    vetor[i] = float(input(f'Informe um valor para V[{i}]'))
for i in range(N):
    print(f'V[{i}] = {vetor[i]}')
# outra forma de mostrar
# for i in range(N):
# print(f'V[{i}] = {vetor[i]} ')