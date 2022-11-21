nome = input('nome do arquivo: ')
arq = open(nome+'.txt','w')
for i in range(5):
    numero = int(input('informe número: '))
    arq.write(str(numero)+'\n')
arq.close()
arq = open(nome+'.txt','r')
linhas = arq.readlines()
lista = []
for i in range(5):
    lista.append(int(linhas[i]))
print(lista)
#for i in range(5):
#    print(linhas[i])
