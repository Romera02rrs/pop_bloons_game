import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pop the Balloons")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Variables del juego
FPS = 60
clock = pygame.time.Clock()
balloon_speed = 1
balloon_spawn_rate = 60
score = 0
lives = 5
time_elapsed = 0

# Función para crear globos
def create_balloon():
    size = random.randint(80, 150)
    x = random.randint(0, WIDTH - size)
    y = HEIGHT + size
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return {'rect': pygame.Rect(x, y, size, size), 'color': color}

# Función principal del juego
def main():
    global score, lives, balloon_speed, time_elapsed

    balloons = []
    line_y = 50

    while True:
        screen.fill(WHITE)

        # Crear globos
        if random.randint(1, balloon_spawn_rate) == 1:
            balloons.append(create_balloon())

        # Mover y dibujar globos
        for balloon in balloons:
            balloon['rect'].move_ip(0, -balloon_speed)
            pygame.draw.ellipse(screen, balloon['color'], balloon['rect'])

        # Dibujar la línea roja
        pygame.draw.line(screen, RED, (0, line_y), (WIDTH, line_y), 2)

        # Dibujar puntaje y vidas
        font = pygame.font.SysFont(None, 36)
        score_text = font.render("Score: " + str(score), True, BLACK)
        lives_text = font.render("Lives: " + str(lives), True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        # Actualizar la pantalla
        pygame.display.flip()
        clock.tick(FPS)

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for balloon in balloons:
                    if balloon['rect'].collidepoint(event.pos):
                        balloons.remove(balloon)
                        score += 1

        # Verificar si los globos han salido de la pantalla
        for balloon in balloons:
            if balloon['rect'].top <= line_y:
                balloons.remove(balloon)
                lives -= 1

        # Verificar si el jugador ha perdido todas las vidas
        if lives == 0:
            game_over()

        # Aumentar la velocidad de los globos con el tiempo
        time_elapsed += 1
        if time_elapsed % FPS == 0:
            balloon_speed += 0.01

# Función para mostrar el mensaje de fin de juego
def game_over():
    font = pygame.font.SysFont(None, 72)
    game_over_text = font.render("Game Over", True, RED)
    screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2 - 50))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
