# print()
# O comando print() é utilizado para imprimir valores na tela. Por exemplo:
print("Olá, mundo!")

# Este código imprime a mensagem "Olá, mundo!" na tela. O print() pode receber um ou mais valores separados por vírgula e imprime-os na tela, separados por espaço. Por exemplo:

nome = "Maria"
idade = 25
print("O nome é", nome, "e a idade é", idade)

# Este código imprime a mensagem "O nome é Maria e a idade é 25" na tela.


# Operadores matemáticos
# Python possui diversos operadores matemáticos, que podem ser utilizados para realizar cálculos. Alguns exemplos são:

# +: soma
# -: subtração
# *: multiplicação
# /: divisão
# %: módulo (resto da divisão)
# **: potenciação

# Por exemplo

a = 10
b = 3
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
potenciacao = a ** b

# Variáveis
# Variáveis são utilizadas para armazenar valores. Por exemplo:

nome = "Maria"
idade = 25

# Neste caso, a variável nome armazena o valor "Maria" e a variável idade armazena o valor 25. As variáveis podem ter diferentes tipos, como strings (textos), números inteiros, números decimais, etc.

# Comentários
# Comentários são trechos de código que são ignorados pelo Python, utilizados para incluir informações ou explicações sobre o código. Por exemplo:

# este é um comentário
nome = "Maria"  # este é outro comentário
idade = 25


# Entrada de dados
# Para solicitar que o usuário insira um valor, utiliza-se o comando input(). Por exemplo:

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

# Este código solicita ao usuário que digite o seu nome e a sua idade, armazenando os valores nas variáveis nome e idade, respectivamente. Note que utilizei a função int() para converter a entrada do usuário em um número inteiro.

# Estruturas condicionais
# As estruturas condicionais permitem que o programa execute diferentes ações dependendo de uma condição. Por exemplo:

idade = 20

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

# Este código verifica se a idade é maior ou igual a 18 e imprime a mensagem correspondente.


# Estruturas de repetição
# As estruturas de repetição permitem que o programa execute uma ação várias vezes. Por exemplo:

contador = 0

while contador < 10:
    print(contador)
    contador += 1

# Este código imprime os números de 0 a 9 na tela.

# for

for i in range(10):
    print(i)

# O comando for é utilizado para iterar sobre uma sequência de valores (como uma lista ou uma faixa numérica) e executar um bloco de código para cada um desses valores.

# No exemplo acima, a sequência de valores é definida pela função range(10), que cria uma sequência de números de 0 a 9 (já que o argumento passado para a função é 10, que é o limite superior da sequência).

# A cada iteração do loop, a variável i recebe um valor da sequência e o bloco de código dentro do for é executado. Nesse caso, o bloco de código consiste apenas do comando print(i), que imprime o valor de i na tela.

# Assim, o programa irá imprimir os valores de 0 a 9, já que a variável i assume cada um desses valores a cada iteração do loop.
