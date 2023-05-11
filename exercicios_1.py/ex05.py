nome_do_usuario = input('Digite seu nome ')
idade_do_usuario = input('Digite sua idade ')


if nome_do_usuario or idade_do_usuario == True:
    print(f'Seu nome é {nome_do_usuario}')
    print(f'Seu nome invertido é {nome_do_usuario[::-1]}')
    if ' ' in nome_do_usuario:
        print('seu nome contem espaços')
    else:
        print('seu nome não contem espaços')

    print(f'Seu nome possui {len(nome_do_usuario)} letras')
    print(f'A primeira letra do seu nome é {nome_do_usuario[0]}')
    print(f'A ultima letra do seu nome é {nome_do_usuario[-1]}')

else:
    print('Desculpe, você deixou campos vazios')
