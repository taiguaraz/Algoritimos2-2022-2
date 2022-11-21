x = []
y = []
for i in range(5):
    x.append(int(input("Informe valores inteiros para lista 1: ")))
for i in range(5):
     y.append(int(input("Informe valores inteiros para lista 2: ")))
yi = list(reversed(y))
#print(yi)
z = []
for i in range(5):
    z.append(x[i]*yi[i])
print(f'Para lista {x} multiplicado por {yi} temos: {z}')