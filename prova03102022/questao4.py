vetor = []
matriz = []
for i in range(3):
    vetor.append(int(input(f'Informe valores para o Vetor na posição {i}: ')))
print(f' Os valores do Vetor são: {vetor}')
for i in range(3):
    linha = []
    for j in range(4):
        vlr = int(input(f'Informe um valor para matriz na posição {i},{j}: '))
        linha.append(vlr)
    matriz.append(linha)
print(f' Os valores da Matriz são: {matriz}')
nvetor = [0,0,0]
for i in range(3):
    nvetor[i] = matriz[i][1]
for i in range(3):
    matriz[i][1] = vetor[i]
vetor = nvetor

print(f'Os valores novos do vetor são: {vetor}, e da nova matriz são: {matriz}')