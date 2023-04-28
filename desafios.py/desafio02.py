# solicita ao usuário a temperatura em graus Celsius
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# converte a temperatura para Fahrenheit
temperatura_fahrenheit = temperatura_celsius * (9/5) + 32

# exibe o resultado na tela
print(f"A temperatura em Fahrenheit é {temperatura_fahrenheit:.2f} °F")