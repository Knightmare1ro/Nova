import pygame
import random
import time

# Dimensiones de la ventana del juego
WIDTH = 800
HEIGHT = 600

# Inicializar Pygame
pygame.init()

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Carreras")

# Cargar imágenes
car_image = pygame.image.load("Car.png")
obstacle_image = pygame.image.load("Piedra.png")
background_image = pygame.image.load("Carretera.jpg")
# Redimensionar imágenes
car_width = 50
car_height = 100
car_image = pygame.transform.scale(car_image, (car_width, car_height))

obstacle_width = 100
obstacle_height = 20
obstacle_image = pygame.transform.scale(obstacle_image, (obstacle_width, obstacle_height))

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Coordenadas del automóvil
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 9

# Coordenadas del obstáculo
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 10

# Contador de puntos
score = 0

# Variable para controlar si el jugador perdió
game_over = False

# Cargar imagen de la pantalla de inicio
start_image = pygame.image.load("Inicio.jpg")
start_image = pygame.transform.scale(start_image, (WIDTH, HEIGHT))

# Bucle para la pantalla de inicio
showing_start_screen = True

while showing_start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Si se presiona la tecla ESPACIO, comienza el juego
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            showing_start_screen = False

    screen.blit(start_image, (0, 0))
    pygame.display.flip()

#Pedrada
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed_x = 5  # Velocidad horizontal del obstáculo
obstacle_speed_y = 7  # Velocidad vertical del obstáculo

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Lógica del juego
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= car_speed
        elif keys[pygame.K_RIGHT]:
            car_x += car_speed

  # Mover el obstáculo verticalmente
        obstacle_y += obstacle_speed_y
        if obstacle_y > HEIGHT:
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = -obstacle_height

        # Mover el obstáculo horizontalmente
        obstacle_x += obstacle_speed_x
        if obstacle_x < 0 or obstacle_x + obstacle_width > WIDTH:
            obstacle_speed_x *= -1  # Cambiar la dirección cuando llegue a los límites de la pantalla

        obstacle_y += obstacle_speed
        if obstacle_y > HEIGHT:
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            # Aumentar el contador de puntos cada vez que se esquiva un obstáculo
            score += 1

        # Detectar colisión entre el automóvil y el obstáculo
        car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        if car_rect.colliderect(obstacle_rect):
            game_over = True

    # Dibujar en la pantalla
    screen.blit(background_image, (0, 0))
    screen.blit(car_image, (car_x, car_y))
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))

    if game_over:
        # Si el jugador perdió, muestra el mensaje de "Game Over"
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, (HEIGHT - game_over_text.get_height()) // 2))

        # Actualizar la pantalla para mostrar el mensaje de "Game Over"
        pygame.display.flip()

        # Pausar el juego durante 5 segundos
        time.sleep(5)

        # Salir del bucle principal para cerrar el juego
        running = False

    else:
        # Mostrar el contador de puntos en la pantalla
        font = pygame.font.Font(None, 36)
        score_text = font.render("Puntos: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

pygame.quit()