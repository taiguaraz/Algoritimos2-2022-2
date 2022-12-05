#TAIGUARA ZUKOSKI - TURMA PROF. RAFAEL
from lib import *

equipes = lerEquipes()
jogos = lerJogos()

while True:
    op = validaNumero(opcoes())
    if op == 1:
        break
    if op == 2:
        a = validaNumero(input('Para Informar uma nova equipe pressione 1, ou digite 2 para sair: '))
        while a == 1:
            pa = input('Informe o nome do país: ')
            paises = [equipe for equipe in equipes if equipe['pais'] == pa]
            if len(paises) > 0:
                print('Pais Inválido, já existe')
                continue
            ab = input('Informe a abreviação do país: ')
            gr = input('Informe o grupo ao qual o país pertence: ')

            equipes.append(Equipe(pa, ab, gr))

            a = validaNumero(input('Para Informar uma nova equipe pressione 1, ou digite 2 para sair: '))
        if op == 1:
            break
    elif op == 3:
        j = validaNumero(input('Para Informar um novo jogo pressione 1, ou digite 2 para sair: '))
        while j == 1:

            arqler = lerEquipes()
            #equipes = [eval(e) for e in arqler.readlines()]
            print('\nPaises possíveis:\n')

            mostraPais(equipes)

            print(f'Escolha dois países para criar um jogo: \n')
            p1i = input('Índice do Pais 1: ')
            p1 = equipes[int(p1i)-1]['pais']
            p2i = input('Índice do Pais 2: ')
            p2 = equipes[int(p2i)-1]['pais']
            print(f'Agora informe os gols: \n')
            g1 = input(f'Gols {p1}: ')
            g2 = input(f'Gols {p2}: ')
            print(f'Agora informe o número de faltas: \n')
            f1 = input(f'Faltas {p1}: ')
            f2 = input(f'Faltas {p2}: ')

            jogos.append(Jogos(p1, p2, g1, g2, f1, f2))

            j = validaNumero(input('Para Informar um novo jogo pressione 1, ou digite 2 para sair: '))
    elif op == 4:
        for i in range(len(jogos)):
            jogo = jogos[i]
        print(f'\nNúmero Total de Jogos: {len(jogos)}\n')
    elif op == 5:
        lerEquipes = lerEquipes()
        for i in range(len(equipes)):
            equipe = equipes[i]
        print(f'\nNúmero Total de Equipes: {len(equipes)}\n')
    elif op == 6:
        gravarEquipes(equipes)
        gravarJogos(jogos)
        print('Dados salvos no arquivo.')
    elif op == 7:
        lerJogos = lerJogos()
        for i in range(len(jogos)):
            jogo = jogos[i]
            print(f'Jogo {i+1}:\n {jogo["p1"]} x {jogo["p2"]}')
            print(f'Gols: {jogo["g1"]} x {jogo["g2"]}')
            print(f'Faltas: {jogo["f1"]} x {jogo["f2"]}')
        print(f'\nNúmero Total de Jogos: {len(jogos)}\n')
print('Saindo do Pragrama')
