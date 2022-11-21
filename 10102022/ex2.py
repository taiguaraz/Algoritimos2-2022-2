def repar (x:int):
    if x % 2 == 0:
        return True
    else:
        return False


num = int(input(f'Informe um número para saber se é par ou não: '))
if repar(num):
    print (f'True')
else:
    print (f'False')