from datetime import datetime
from models import Locomotiva, Vagao, Composicao
import curses

locomotivas = []
vagoes = []
composicoes = []

# Função para exibir o menu


def exibir_menu(stdscr, opcoes, escolha):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    stdscr.addstr(0, 0, "======================= Sistema Ferroviário =======================", curses.A_BOLD)
    for i, opcao in enumerate(opcoes):
        if i == escolha:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(i + 2, 1, f"{i + 1}. {opcao}")
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(i + 2, 1, f"{i + 1}. {opcao}")
    
    stdscr.addstr(len(opcoes) + 2, 0, "====================================================================", curses.A_BOLD)
    stdscr.refresh()

def menu_interativo(opcoes):
    curses.wrapper(main, opcoes)

def main(stdscr, opcoes):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    escolha = 0
    exibir_menu(stdscr, opcoes, escolha)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and escolha > 0:
            escolha -= 1
        elif key == curses.KEY_DOWN and escolha < len(opcoes) - 1:
            escolha += 1
        elif key == 10:  # Tecla Enter
            stdscr.clear()
            stdscr.addstr(0, 0, f"Opção selecionada: {opcoes[escolha]}")
            stdscr.refresh()
            stdscr.getch()
            break

        exibir_menu(stdscr, opcoes, escolha)

def exibir_menu_principal():
    opcoes = [
        "Listar locomotivas",
        "Listar tipos de vagões com produtos transportados",
        "Listar todas as composições",
        "Listar composições por locomotiva",
        "Listar trajetos das composições",
        "Contar quantidade de produtos transportados por mês",
        "Adicionar Locomotiva",
        "Adicionar Composição",
        "Adicionar Vagão",
        "Sair"
    ]
    menu_interativo(opcoes)

if __name__ == "__main__":
    exibir_menu_principal()


# Função para listar locomotivas
def listar_locomotivas():
    if locomotivas:
        print("\n=== Lista de Locomotivas ===")
        for locomotiva in locomotivas:
            print(f"Locomotiva {locomotiva.numero}: Modelo {locomotiva.modelo}")
    else:
        print("Nenhuma locomotiva cadastrada.")

# Função para listar tipos de vagões com produtos transportados
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

# Função para listar todas as composições
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

# Função para listar composições por locomotiva
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

# Função para adicionar locomotiva
def adicionar_locomotiva():
    numero = int(input("Número da locomotiva: "))
    modelo = input("Modelo da locomotiva: ")
    locomotiva = Locomotiva(numero, modelo)
    locomotivas.append(locomotiva)
    print(f"\nLocomotiva {numero} adicionada com sucesso!")

# Função para adicionar composição
def adicionar_composicao():
    numero = int(input("Número da composição: "))
    horario_inicio_str = input("Horário de Início (formato YYYY-MM-DD HH:MM): ")
    horario_fim_str = input("Horário de Fim (formato YYYY-MM-DD HH:MM): ")
    
    horario_inicio = datetime.strptime(horario_inicio_str, "%Y-%m-%d %H:%M")
    horario_fim = datetime.strptime(horario_fim_str, "%Y-%m-%d %H:%M")
    
    composicao = Composicao(numero, horario_inicio, horario_fim)
    composicoes.append(composicao)
    print(f"\nComposição {numero} adicionada com sucesso!")

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
            print(f"\nVagão adicionado à Composição {composicao_numero}")
            return
    print("\nComposição não encontrada.")

# Função para listar trajetos das composições
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

# Função para contar a quantidade de produtos transportados por mês
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


# Dicionário de opções
opcoes = {
    "1": listar_locomotivas,
    "2": listar_tipos_de_vagoes,
    "3": listar_composicoes,
    "4": listar_composicoes_por_locomotiva,
    "5": listar_trajetos,
    "6": contar_quantidade_de_produtos_por_mes,
    "7": adicionar_locomotiva,
    "8": adicionar_composicao,
    "9": adicionar_vagao,
    "10": lambda: print("Saindo do programa.")
}

# Loop principal
while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")
    if escolha in opcoes:
        opcoes[escolha]()
    else:
        print("Opção inválida. Tente novamente.")
