import os
os.system('cls')
frase = 'Olá mundo, sou Andre e tenho dezenove anos'
i = 0
quantidade_vezes = 0
letras_vezes = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    quantidade_vezes_atual = frase.count(letra_atual)

    if quantidade_vezes < quantidade_vezes_atual:
        quantidade_vezes = quantidade_vezes_atual
        letras_vezes = letra_atual

    i += 1

print(f'A letra que mais apareceu foi "{letras_vezes}", {quantidade_vezes} x ')
