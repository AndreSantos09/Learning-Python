from datetime import datetime

class Locomotiva:
    def __init__(self, numero, modelo):
        self.numero = numero
        self.modelo = modelo
        self.composicoes = []

    def adicionar_composicao(self, composicao):
        self.composicoes.append(composicao)

class Vagao:
    def __init__(self, tipo, produto):
        self.tipo = tipo
        self.produto = produto

class Composicao:
    def __init__(self, numero, horario_inicio, horario_fim):
        self.numero = numero
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim
        self.vagoes = []

    def adicionar_vagao(self, vagao):
        self.vagoes.append(vagao)

locomotivas = []
vagoes = []
composicoes = []

# Função para exibir o menu
def exibir_menu():
    print("Menu:")
    print("1. Listar locomotivas")
    print("2. Listar tipos de vagões com produtos transportados")
    print("3. Listar todas as composições")
    print("4. Listar composições por locomotiva")
    print("5. Listar trajetos das composições")
    print("6. Contar quantidade de produtos transportados por mês")
    print("7. Adicionar Locomotiva")
    print("8. Adicionar Composição")
    print("9. Adicionar Vagão")
    print("10. Sair")

# Função para adicionar locomotiva
def adicionar_locomotiva():
    numero = int(input("Número da locomotiva: "))
    modelo = input("Modelo da locomotiva: ")
    locomotiva = Locomotiva(numero, modelo)
    locomotivas.append(locomotiva)
    print(f"Locomotiva {numero} adicionada com sucesso!")

# Função para adicionar composição
def adicionar_composicao():
    numero = int(input("Número da composição: "))
    horario_inicio_str = input("Horário de Início (formato YYYY-MM-DD HH:MM): ")
    horario_fim_str = input("Horário de Fim (formato YYYY-MM-DD HH:MM): ")
    
    horario_inicio = datetime.strptime(horario_inicio_str, "%Y-%m-%d %H:%M")
    horario_fim = datetime.strptime(horario_fim_str, "%Y-%m-%d %H:%M")
    
    composicao = Composicao(numero, horario_inicio, horario_fim)
    composicoes.append(composicao)
    print(f"Composição {numero} adicionada com sucesso!")


# Função para listar locomotivas
def listar_locomotivas():
    for locomotiva in locomotivas:
        print(f"Locomotiva {locomotiva.numero}: Modelo {locomotiva.modelo}")

# Função para listar tipos de vagões com produtos transportados
def listar_tipos_de_vagoes():
    tipos_de_vagoes = set()
    for vagao in vagoes:
        tipos_de_vagoes.add((vagao.tipo, vagao.produto))
    
    for tipo, produto in tipos_de_vagoes:
        print(f"Tipo de Vagão: {tipo}, Produto Transportado: {produto}")

# Função para listar todas as composições
def listar_composicoes():
    for composicao in composicoes:
        print(f"Composição {composicao.numero}:")
        print(f"Horário de Início: {composicao.horario_inicio}")
        print(f"Horário de Fim: {composicao.horario_fim}")
        print("Vagões:")
        for vagao in composicao.vagoes:
            print(f"  Tipo: {vagao.tipo}, Produto Transportado: {vagao.produto}")

# Função para listar composições por locomotiva
def listar_composicoes_por_locomotiva():
    for locomotiva in locomotivas:
        print(f"Locomotiva {locomotiva.numero}:")
        for composicao in locomotiva.composicoes:
            print(f"  Composição {composicao.numero}")

# Função para adicionar uma composição a uma locomotiva
def adicionar_composicao_a_locomotiva(locomotiva_numero, composicao_numero):
    for locomotiva in locomotivas:
        if locomotiva.numero == locomotiva_numero:
            for composicao in composicoes:
                if composicao.numero == composicao_numero:
                    locomotiva.adicionar_composicao(composicao)
                    print(f"Composição {composicao_numero} adicionada à Locomotiva {locomotiva_numero}")
                    return
    print("Locomotiva ou Composição não encontrada.")

# Função para adicionar vagão a composição
def adicionar_vagao():
    composicao_numero = int(input("Número da composição: "))
    tipo = input("Tipo de vagão: ")
    produto = input("Produto transportado: ")
    
    for composicao in composicoes:
        if composicao.numero == composicao_numero:
            vagao = Vagao(tipo, produto)
            composicao.adicionar_vagao(vagao)
            vagoes.append(vagao)
            print(f"Vagão adicionado à Composição {composicao_numero}")
            return
    print("Composição não encontrada.")

# Função para listar trajetos das composições
def listar_trajetos():
    for composicao in composicoes:
        print(f"Composição {composicao.numero}:")
        print(f"Horário de Início: {composicao.horario_inicio}")
        print(f"Horário de Fim: {composicao.horario_fim}")
        print("Trajeto: Início - Fim")
        print("--------------")
        # Aqui você pode adicionar detalhes do trajeto da composição se necessário.

# Função para contar a quantidade de produtos transportados no mês
def contar_quantidade_de_produtos_por_mes():
    produtos_por_mes = {}
    for composicao in composicoes:
        mes_inicio = composicao.horario_inicio.month
        mes_fim = composicao.horario_fim.month
        if mes_inicio == mes_fim:
            mes = mes_inicio
            if mes not in produtos_por_mes:
                produtos_por_mes[mes] = {}
            for vagao in composicao.vagoes:
                produto = vagao.produto
                if produto not in produtos_por_mes[mes]:
                    produtos_por_mes[mes][produto] = 0
                produtos_por_mes[mes][produto] += 1
    
    for mes, produtos in produtos_por_mes.items():
        print(f"Mês {mes}:")
        for produto, quantidade in produtos.items():
            print(f"  Produto: {produto}, Quantidade: {quantidade}")

# Exemplo de uso do sistema
if __name__ == "__main__":
    

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_locomotivas()
        elif escolha == "2":
            listar_tipos_de_vagoes()
        elif escolha == "3":
            listar_composicoes()
        elif escolha == "4":
            listar_composicoes_por_locomotiva()
        elif escolha == "5":
            listar_trajetos()
        elif escolha == "6":
            contar_quantidade_de_produtos_por_mes()
        elif escolha == "7":
            adicionar_locomotiva()
        elif escolha == "8":
            adicionar_composicao()
        elif escolha == "9":
            adicionar_vagao()
        elif escolha == "10":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

