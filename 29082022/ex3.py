x = []
y = []
for i in range(5):
    x.append(int(input("Informe valores inteiros para lista 1: ")))
    y.append(int(input("Informe valores inteiros para lista 2: ")))
z = []
for i in range(5):
    z.append(x[i]+y[i])
print(f'{x} , {y} então a soma é: {z}')