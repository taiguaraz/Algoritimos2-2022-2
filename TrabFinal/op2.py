
arq = open('equipes.txt','w')
a = int(input('Para Informar uma nova equipe pressione 1, ou digite 2 para sair: '))
while a == 1:
    for i in range(1):
        pais = str(input('Informe o nome do país: '))
        arq.write(str(pais)+'\n')
        abrv = str(input('Informe a abreviação do país: '))
        arq.write(str(abrv)+'\n')
        grupo = str(input('Informe o grupo ao qual o país pertence: '))
        arq.write(str(grupo)+'\n')
        a = int(input('Para Informar uma nova equipe pressione 1, ou digite 2 para sair: '))
    if a != 1:
        break
arq.close()