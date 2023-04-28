
'''
Exercício: Calcular o preço final de um produto com desconto.

Descrição: Crie um programa que solicite ao usuário o preço original de um produto e a porcentagem de desconto a ser aplicada.
Em seguida, o programa deve calcular o preço final com desconto e exibir o resultado na tela.

Dica: Para calcular o preço final com desconto, você pode utilizar a seguinte fórmula:

preco_final = preco_original - (preco_original * (percentual_desconto / 100))

'''

# solicita ao usuário o preço original e a porcentagem de desconto
preco_original = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto a ser aplicado: "))

# calcula o preço final com desconto
preco_final = preco_original - (preco_original * (percentual_desconto / 100))

# exibe o resultado na tela
print(f"O preço final com desconto é R$ {preco_final:.2f}")
