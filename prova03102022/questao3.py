l18 = []
tam = 18
for i in range(18):
    vlr = int(input(f'Informe valores para lista: '))
    l18.append(vlr)
ordem = sorted(l18)
maior = ordem[17]
menor = ordem[0]

print(f'Na lista: {l18}, o maior número é o: {maior} na posição: {l18.index(maior)}, e o menor número é o: {menor} na posição: {l18.index(menor)}.')
