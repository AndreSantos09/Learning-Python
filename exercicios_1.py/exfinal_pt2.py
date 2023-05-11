cpf = '10022798013'
dez_digitos = cpf[:10]
contador_regressivo_2 = 10
resultado_dig2 = 0

for digito_2 in dez_digitos:
    resultado_dig2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -=1
digito_2 = (resultado_dig2 * 10) % 11
digito_2 = digito_2 if digito_2 <=9 else 0
print(digito_2)