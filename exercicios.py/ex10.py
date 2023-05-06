
while True:
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    operadores_validos = '+-/*'

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('numeros invalidos')
        continue

    if operador not in operadores_validos:
        print('operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        soma = (num_1_float + num_2_float)
        print(f'Resultado da operação foi {soma}')
    elif operador == '-':
        subtracao = (num_1_float - num_2_float)
        print(f'Resultado da operação foi {subtracao}')
    elif operador == '*':
        multiplicacao = (num_1_float * num_2_float)
        print(f'Resultado da operação foi {multiplicacao}')
    elif operador == '/':
        divisao = (num_1_float / num_2_float)
        print(f'Resultado da operação foi {divisao}')

    sair = input('Quer sair ? [s]im: ').lower().startswith('s')

    if sair is True:
        break
