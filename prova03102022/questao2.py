l10 = []
tam = 10
for i in range(tam):
    l10.append(int(input(f'Informe valores inteiros: ')))
print(f'Números informados:{l10}')

cont = 0
for i in range(tam):
    if l10[i] <= 0:
        print(l10[i])
        print(i)
        cont += 1
if cont == 0:
    print(f'Não foram informados números menores ou iguais a 0.')
