
def impar_par(num):
    multiplo_de_dois =  num % 2 == 0

    if multiplo_de_dois == True:
        return f'{num} é par'
    return f'{num} é impar'

print(impar_par(2))

print(impar_par(1))

print(impar_par(235))

print(impar_par(17))