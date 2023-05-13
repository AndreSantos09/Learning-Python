

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

print(multiplicar(1,2,3))
