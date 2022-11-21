x = []
for i in range(10):
    vlr = (float(input("Informe um valor: ")))
    x.append(vlr)
print(f'Entrada: {x}')
for k, v in enumerate(x):
    if v%2:
        x[k] = k
    else:
        x[k] = v*k
print(f'Resultado: {x}')