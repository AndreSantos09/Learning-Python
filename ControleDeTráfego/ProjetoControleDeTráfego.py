from datetime import datetime, timedelta  # Importe a classe datetime e timedelta

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

# Função para adicionar um vagão a uma composição
def adicionar_vagao_a_composicao(composicao_numero, tipo, produto):
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
    # Criar algumas locomotivas
    locomotiva1 = Locomotiva(1, "Modelo A")
    locomotiva2 = Locomotiva(2, "Modelo B")
    locomotiva3 = Locomotiva(3, "Modelo C")
    locomotivas.extend([locomotiva1, locomotiva2, locomotiva3])

    # Criar algumas composições
    composicao1 = Composicao(101, datetime(2023, 1, 10, 8, 0), datetime(2023, 1, 10, 12, 0))
    composicao2 = Composicao(102, datetime(2023, 1, 15, 10, 0), datetime(2023, 1, 15, 14, 0))
    composicao3 = Composicao(103, datetime(2023, 2, 5, 9, 0), datetime(2023, 2, 5, 13, 0))
    composicoes.extend([composicao1, composicao2, composicao3])

    # Adicionar composições às locomotivas
    adicionar_composicao_a_locomotiva(1, 101)
    adicionar_composicao_a_locomotiva(2, 102)
    adicionar_composicao_a_locomotiva(3, 103)

    # Adicionar vagões às composições
    adicionar_vagao_a_composicao(101, "Vagão A", "Produto X")
    adicionar_vagao_a_composicao(103, "Vagão C", "Produto X")

    # Listar informações
    listar_locomotivas()
    print("\n")
    listar_tipos_de_vagoes()
    print("\n")
    listar_composicoes()
    print("\n")
    listar_composicoes_por_locomotiva()
    print("\n")
    listar_trajetos()
    print("\n")
    contar_quantidade_de_produtos_por_mes()
