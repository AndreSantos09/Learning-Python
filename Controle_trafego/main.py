import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações iniciais
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Variáveis da cobrinha
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_speed = 15
snake_size = 20
snake_x_change = 0
snake_y_change = 0

# Variáveis da comida
food_x = random.randint(0, WIDTH - snake_size)
food_y = random.randint(0, HEIGHT - snake_size)

# Pontuação
score = 0

# Lista que guarda as coordenadas da cobrinha
snake_body = []
snake_length = 1

# Função para desenhar a cobrinha
def draw_snake(snake_body):
    for part in snake_body:
        pygame.draw.rect(screen, GREEN, [part[0], part[1], snake_size, snake_size])

# Função principal do jogo
def game_loop():
    global snake_x, snake_y, snake_x_change, snake_y_change, snake_length, score

    game_over = False
    game_close = False

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            font = pygame.font.Font(None, 36)
            text = font.render("Você perdeu! Pressione Q para sair ou C para jogar novamente.", True, WHITE)
            text_rect = text.get_rect()
            text_rect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(text, text_rect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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
            game_close = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [food_x, food_y, snake_size, snake_size])

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        for part in snake_body[:-1]:
            if part == snake_head:
                game_close = True

        draw_snake(snake_body)

        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = random.randint(0, WIDTH - snake_size)
            food_y = random.randint(0, HEIGHT - snake_size)
            snake_length += 1
            score += 1

        pygame.time.delay(1000 // snake_speed)

    pygame.quit()
    quit()

game_loop()
