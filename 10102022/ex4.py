def atriang(x:int,y:int):
    return (x*y)/2
basetri = int(input(f'Informe o tamanho da base do triângulo: '))
alttri = int(input(f'Informe o tamanho da altura do triângulo: '))
print(f'A área do triângulo é de: {atriang(basetri,alttri)}m2.')