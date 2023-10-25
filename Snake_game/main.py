import pygame
import random

# Inicialização do Pygame
pygame.init()

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tamanho da tela e da cobrinha
WIDTH, HEIGHT = 800, 600
snake_size = 20
snake_speed = 15

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")

# Fonte para exibir pontuação
font = pygame.font.Font(None, 36)

# Variáveis de pontuação e cor da cobra
score = 0
snake_color_index = 0

# Cores da cobra
SNAKE_COLORS = [GREEN, RED, BLUE]

# Menu
menu_options = ["INICIAR", "OPÇÕES", "SAIR"]
options_submenu = ["Mudar cor da cobra", "Voltar"]
color_options = ["Verde", "Vermelho", "Azul"]
selected_option = 0  # Índice da opção selecionada no menu principal
selected_submenu_option = 0  # Índice da opção selecionada no submenu de opções

# Função para desenhar o menu
def draw_menu():
    screen.fill(BLACK)
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("Jogo da Cobrinha", True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (WIDTH // 2, HEIGHT // 4)

    menu_font = pygame.font.Font(None, 48)
    for i, option in enumerate(menu_options):
        text = menu_font.render(option, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2 + i * 50)
        if i == selected_option:
            pygame.draw.rect(screen, WHITE, (text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20), 3)
        screen.blit(text, text_rect)

    screen.blit(title_text, title_rect)
    pygame.display.update()

# Função para exibir o submenu de opções
def draw_options_submenu():
    screen.fill(BLACK)
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("Opções", True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (WIDTH // 2, HEIGHT // 4)

    submenu_font = pygame.font.Font(None, 48)
    for i, option in enumerate(options_submenu):
        text = submenu_font.render(option, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2 + i * 50)
        if i == selected_submenu_option:
            pygame.draw.rect(screen, WHITE, (text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20), 3)
        screen.blit(text, text_rect)

    screen.blit(title_text, title_rect)
    pygame.display.update()

# Função para exibir o submenu de cores
def draw_color_submenu():
    screen.fill(BLACK)
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("Cores Disponíveis", True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (WIDTH // 2, HEIGHT // 4)

    submenu_font = pygame.font.Font(None, 48)
    for i, option in enumerate(color_options):
        text = submenu_font.render(option, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2 + i * 50)
        if i == snake_color_index:
            pygame.draw.rect(screen, WHITE, (text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20), 3)
        screen.blit(text, text_rect)

    screen.blit(title_text, title_rect)
    pygame.display.update()

# Função para controlar o menu
def control_menu():
    global selected_option, selected_submenu_option, snake_color_index
    in_menu = True

    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if selected_option < len(menu_options) - 1:
                        selected_option += 1
                elif event.key == pygame.K_UP:
                    if selected_option > 0:
                        selected_option -= 1
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == "INICIAR":
                        in_menu = False
                    elif menu_options[selected_option] == "OPÇÕES":
                        control_options_submenu()
                    elif menu_options[selected_option] == "SAIR":
                        pygame.quit()
                        quit()

        draw_menu()

# Função para controlar o submenu de opções
def control_options_submenu():
    global selected_option, selected_submenu_option, snake_color_index
    in_submenu = True

    while in_submenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if selected_submenu_option < len(options_submenu) - 1:
                        selected_submenu_option += 1
                elif event.key == pygame.K_UP:
                    if selected_submenu_option > 0:
                        selected_submenu_option -= 1
                elif event.key == pygame.K_RETURN:
                    if options_submenu[selected_submenu_option] == "Mudar cor da cobra":
                        control_color_submenu()
                    elif options_submenu[selected_submenu_option] == "Voltar":
                        in_submenu = False

        draw_options_submenu()

# Função para controlar o submenu de cores
def control_color_submenu():
    global selected_option, selected_submenu_option, snake_color_index
    in_color_submenu = True

    while in_color_submenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if snake_color_index < len(color_options) - 1:
                        snake_color_index += 1
                elif event.key == pygame.K_UP:
                    if snake_color_index > 0:
                        snake_color_index -= 1
                elif event.key == pygame.K_RETURN:
                    in_color_submenu = False

        draw_color_submenu()

# Função para desenhar a cobrinha
def draw_snake(snake_body):
    for part in snake_body:
        pygame.draw.rect(screen, SNAKE_COLORS[snake_color_index], [part[0], part[1], snake_size, snake_size])

# Função para exibir pontuação
def show_score(score):
    text = font.render("Pontuação: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

# Função para gerar a posição da maçã
def generate_apple(snake_body):
    while True:
        apple_x = random.randrange(0, WIDTH - snake_size, snake_size)
        apple_y = random.randrange(0, HEIGHT - snake_size, snake_size)
        if [apple_x, apple_y] not in snake_body:
            return apple_x, apple_y

# Função para verificar a colisão entre a cabeça da cobra e a maçã
def is_collision(snake_x, snake_y, food_x, food_y):
    return snake_x == food_x and snake_y == food_y

# Função para exibir a tela de início
def show_start_screen():
    control_menu()

# Função para exibir a tela de game over
def show_game_over_screen():
    global score
    score = 0  # Reinicia a pontuação
    selected_option = 0  # Redefine a opção selecionada no menu principal
    control_menu()  # Volta para o menu

# Função principal do jogo
def game_loop():
    global score

    show_start_screen()

    while True:
        snake_x = WIDTH // 2
        snake_y = HEIGHT // 2
        snake_x_change = 0
        snake_y_change = 0
        snake_body = []
        snake_length = 1
        food_x, food_y = generate_apple(snake_body)
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        snake_x_change = -snake_size
                        snake_y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        snake_x_change = snake_size
                        snake_y_change = 0
                    elif event.key == pygame.K_UP:
                        snake_y_change = -snake_size
                        snake_x_change = 0
                    elif event.key == pygame.K_DOWN:
                        snake_y_change = snake_size
                        snake_x_change = 0

            if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
                game_over = True

            snake_x += snake_x_change
            snake_y += snake_y_change
            screen.fill(BLACK)
            pygame.draw.rect(screen, WHITE, [food_x, food_y, snake_size, snake_size])

            snake_head = [snake_x, snake_y]
            snake_body.append(snake_head)

            if len(snake_body) > snake_length:
                del snake_body[0]

            for part in snake_body[:-1]:
                if part == snake_head:
                    game_over = True

            draw_snake(snake_body)
            show_score(score)

            if is_collision(snake_x, snake_y, food_x, food_y):
                snake_length += 1
                score += 1
                food_x, food_y = generate_apple(snake_body)

            pygame.display.update()
            pygame.time.delay(1000 // snake_speed)

        show_game_over_screen()

# Chame a função principal do jogo
game_loop()
