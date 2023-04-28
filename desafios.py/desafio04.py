# solicita ao usuário as duas notas
nota1 = float(input("Digite a primeira nota (de 0 a 10): "))
nota2 = float(input("Digite a segunda nota (de 0 a 10): "))

# calcula a média das notas
media = (nota1 + nota2) / 2

# verifica a situação do aluno e exibe o resultado na tela
if media >= 0 and media < 5:
    situacao = "Reprovado"
elif media >= 5 and media < 7:
    situacao = "Em recuperação"
else:
    situacao = "Aprovado"

print(f"A média do aluno é {media:.2f} e sua situação é {situacao}")