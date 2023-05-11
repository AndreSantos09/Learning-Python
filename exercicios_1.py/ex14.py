import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor:')
        if valor == '':
            print('Você inseriu um item sem nome')

        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha qual o item que quer apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possível apagar este item')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, item in enumerate(lista):
            print(i, item)

    else:
        print('Por favor, escolha apenas [i][a] ou [l].')
