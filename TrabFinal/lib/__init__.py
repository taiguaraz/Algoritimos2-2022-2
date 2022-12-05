#TAIGUARA ZUKOSKI - TURMA PROF. RAFAEL
def opcoes():
    return input(
        f'Informe a opção desejada: \n(1) Sair do programa.\n(2) Nova equipe.\n(3) Novo Jogo.\n(4) Número total de jogos armazenados no banco da Copa do Mundo.\n(5) Número total de equipes no banco da Copa do Mundo.\n(6) Gravar os dados dos jogos no arquivo.\n(7) Listar os jogos que constam no banco e suas respectivas equipes.\n')

def Equipe(pais, abr, grupo):
    return {'pais': pais, 'abr': abr, 'grupo': grupo}

def Jogos(p1, p2, g1, g2, f1, f2):
    return {'p1': p1, 'p2': p2, 'g1': g1, 'g2': g2, 'f1': f1, 'f2': f2}

def lerEquipes():
    try:
        arq = open('equipes.txt', 'r+')
        equipes = [eval(equipe) for equipe in arq.readlines()]
    except:
        arq = open('equipes.txt', 'w')
        equipes = []
    arq.close()
    return equipes

def gravarEquipes(equipes):
    arq = open('equipes.txt', 'w')
    arq.writelines([str(equipe) + '\n' for equipe in equipes])
    arq.close()

def lerJogos():
    try:
        arq = open('jogos.txt', 'r+')
        jogos = [eval(jogo) for jogo in arq.readlines()]
    except:
        arq = open('jogos.txt', 'w')
        jogos = []
    arq.close()
    return jogos

def gravarJogos(jogos):
    arq = open('jogos.txt', 'w')
    arq.writelines([str(jogo) + '\n' for jogo in jogos])
    arq.close()

def mostraPais(equipes):
    for i in range(len(equipes)):
        print(f'{i + 1} - {equipes[i]["pais"]}')

def validarPais(novoPais, compara):
    paises = compara['pais']
    for i in range(len(paises)):
        if compara['pais'][i] == novoPais:
            print('Pais já existe')
            return True
    return False

def validaNumero(n):
    if n.isdigit():
        n = int(n)
    if not isinstance(n, int):
        return print(f'{n} não é um número válido')
    return n