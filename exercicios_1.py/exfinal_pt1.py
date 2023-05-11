# CALCULO DO PRIMEIRO DIGITO DO CPF
cpf = '124.643.970-79'
n_cpf = cpf
for i in cpf:
    if i.isnumeric() == False:
        cpf = cpf.replace(i, '')

nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_dig1 = 0

for digito in nove_digitos:
    resultado_dig1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_dig1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


# CALCULO DO SEGUNDO DIGITO DO CPF
dez_digitos = cpf[:10]
contador_regressivo_2 = 11
resultado_dig2 = 0

for digito in dez_digitos:
    resultado_dig2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_dig2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
## Validador de cpf
if digito_1 == int(cpf[9]) and digito_2 == int(cpf[10]):
    print(f'este cpf é [v]álido {n_cpf}')
else:
    print(f'este cpf é [i]nválido {n_cpf}')
