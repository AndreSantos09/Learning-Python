import tkinter as tk
from datetime import datetime
from models import Locomotiva, Vagao, Composicao

locomotivas = []
vagoes = []
composicoes = []

def exibir_menu(opcoes):
    menu_window = tk.Tk()
    menu_window.title("Sistema Ferroviário")

    label = tk.Label(menu_window, text="Escolha uma opção:")
    label.pack()

    for i, opcao in enumerate(opcoes, 1):
        button = tk.Button(menu_window, text=opcao, command=lambda op=opcao: opcoes[op]())
        button.pack()

    menu_window.mainloop()

def listar_locomotivas():
    if locomotivas:
        print("\n=== Lista de Locomotivas ===")
        for locomotiva in locomotivas:
            print(f"Locomotiva {locomotiva.numero}: Modelo {locomotiva.modelo}")
    else:
        print("Nenhuma locomotiva cadastrada.")

def listar_tipos_de_vagoes():
    if vagoes:
        print("\n=== Tipos de Vagões e Produtos Transportados ===")
        tipos_de_vagoes = set()
        for vagao in vagoes:
            tipos_de_vagoes.add((vagao.tipo, vagao.produto))

        for tipo, produto in tipos_de_vagoes:
            print(f"Tipo de Vagão: {tipo}, Produto Transportado: {produto}")
    else:
        print("Nenhum vagão cadastrado.")

def listar_composicoes():
    if composicoes:
        print("\n=== Lista de Composições ===")
        for composicao in composicoes:
            print(f"Composição {composicao.numero}:")
            print(f"Horário de Início: {composicao.horario_inicio}")
            print(f"Horário de Fim: {composicao.horario_fim}")
            print("Vagões:")
            for vagao in composicao.vagoes:
                print(f"  Tipo: {vagao.tipo}, Produto Transportado: {vagao.produto}")
    else:
        print("Nenhuma composição cadastrada.")

def listar_composicoes_por_locomotiva():
    if locomotivas:
        print("\n=== Composições por Locomotiva ===")
        for locomotiva in locomotivas:
            if locomotiva.composicoes:
                print(f"Locomotiva {locomotiva.numero}:")
                for composicao in locomotiva.composicoes:
                    print(f"  Composição {composicao.numero}")
            else:
                print(f"Locomotiva {locomotiva.numero} não possui composições.")
    else:
        print("Nenhuma locomotiva cadastrada.")

def adicionar_locomotiva():
    numero = input("Número da locomotiva: ")
    modelo = input("Modelo da locomotiva: ")
    locomotiva = Locomotiva(numero, modelo)
    locomotivas.append(locomotiva)
    print(f"\nLocomotiva {numero} adicionada com sucesso!")

def adicionar_composicao():
    numero = input("Número da composição: ")
    horario_inicio_str = input("Horário de Início (formato YYYY-MM-DD HH:MM): ")
    horario_fim_str = input("Horário de Fim (formato YYYY-MM-DD HH:MM): ")

    horario_inicio = datetime.strptime(horario_inicio_str, "%Y-%m-%d %H:%M")
    horario_fim = datetime.strptime(horario_fim_str, "%Y-%m-%d %H:%M")

    composicao = Composicao(numero, horario_inicio, horario_fim)
    composicoes.append(composicao)
    print(f"\nComposição {numero} adicionada com sucesso!")

def adicionar_vagao():
    composicao_numero = input("Número da composição: ")
    tipo = input("Tipo de vagão: ")
    produto = input("Produto transportado: ")

    for composicao in composicoes:
        if composicao.numero == composicao_numero:
            vagao = Vagao(tipo, produto)
            composicao.adicionar_vagao(vagao)
            vagoes.append(vagao)
            print(f"\nVagão adicionado à Composição {composicao_numero}")
            return
    print("\nComposição não encontrada.")

def listar_trajetos():
    if composicoes:
        print("\n=== Trajetos das Composições ===")
        for composicao in composicoes:
            print(f"Composição {composicao.numero}:")
            print(f"Horário de Início: {composicao.horario_inicio}")
            print(f"Horário de Fim: {composicao.horario_fim}")
            print("Trajeto: Início - Fim")
            print("--------------")
            # Aqui você pode adicionar detalhes do trajeto da composição se necessário.
    else:
        print("Nenhuma composição cadastrada.")

def contar_quantidade_de_produtos_por_mes():
    if composicoes:
        print("\n=== Quantidade de Produtos Transportados por Mês ===")
        produtos_por_mes = {}

        for composicao in composicoes:
            mes_inicio = composicao.horario_inicio.month
            mes_fim = composicao.horario_fim.month

            for vagao in composicao.vagoes:
                mes = mes_inicio
                while mes <= mes_fim:
                    if mes not in produtos_por_mes:
                        produtos_por_mes[mes] = {}

                    produto = vagao.produto
                    if produto not in produtos_por_mes[mes]:
                        produtos_por_mes[mes][produto] = 0
                    produtos_por_mes[mes][produto] += 1

                    mes += 1

        for mes, produtos in produtos_por_mes.items():
            print(f"Mês {mes}:")
            for produto, quantidade in produtos.items():
                print(f"  Produto: {produto}, Quantidade: {quantidade}")
    else:
        print("Nenhuma composição cadastrada.")

opcoes = {
    "Listar locomotivas": listar_locomotivas,
    "Listar tipos de vagões com produtos transportados": listar_tipos_de_vagoes,
    "Listar todas as composições": listar_composicoes,
    "Listar composições por locomotiva": listar_composicoes_por_locomotiva,
    "Listar trajetos das composições": listar_trajetos,
    "Contar quantidade de produtos transportados por mês": contar_quantidade_de_produtos_por_mes,
    "Adicionar Locomotiva": adicionar_locomotiva,
    "Adicionar Composição": adicionar_composicao,
    "Adicionar Vagão": adicionar_vagao,
    "Sair": lambda: print("Saindo do programa.")
}

if __name__ == "__main__":
    exibir_menu(opcoes)
