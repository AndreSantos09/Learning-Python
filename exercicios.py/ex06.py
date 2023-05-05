#numero_int = input('digite um numero inteiro ')

#try:
    # numero_int = float(numero_int)
    # par_impar = numero_int % 2 == 0
    # par_impar_str = 'impar'
    

    # if par_impar:
        #par_impar_str = 'par'
        
    # print(f'o numero {numero_int} é {par_impar_str}')    

#except:
    #print(f'{numero_int} não é um numero inteiro')
    
    
num = input('numero ')

if "." in num:
    num = float(num) 
    print(f'o número {num} não é inteiro')       
else:
    num = int (num)
    print(f'o número {num} é um inteiro')
    

