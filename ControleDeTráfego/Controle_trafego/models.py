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
