nome_usuario = input('insira o seu nome ')

if len(nome_usuario) <= 4:
    print(f'{nome_usuario}, seu nome é curto')
elif len(nome_usuario) >= 5 and len(nome_usuario) <= 6:
    print(f'{nome_usuario}, seu nome é normal')
elif len(nome_usuario) > 6:
    print(f'{nome_usuario}, seu nome é longo')