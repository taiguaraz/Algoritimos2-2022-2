listaa = [0,0,0]
listab = [0,0,0]
for i in range(3):
    listaa[i] = int(input(f'Informe os valores para lista A na posição {i}: '))
for i in range(3):
    listab[i] = int(input(f'Informe os valores para lista B na posição {i}: '))
print(f'A:{listaa}, B:{listab}')
listaa = listaa[::-1]
listab = listab[::-1]
print(f'Inverso de A:{listaa}, Inverso de B:{listab}')