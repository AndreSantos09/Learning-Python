## CALCULO DO PRIMEIRO DIGITO DO CPF
cpf ='10022798013'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_dig1 = 0
for digito in nove_digitos:
    resultado_dig1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -=1
digito_1 = (resultado_dig1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)


