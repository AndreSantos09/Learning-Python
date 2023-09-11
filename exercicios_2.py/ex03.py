def soma(*args):
    
    result = 0
    for i in args:
        if isinstance(i, (int , float)):
            result += i
        else:
            print(f'Error o valor {i} não é um número')
    
    print(result)



soma(2,4,5)