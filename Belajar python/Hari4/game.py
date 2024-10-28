import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Game")

# Warna
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Kecepatan gerak Pac-Man
PACMAN_SPEED = 5

# Membuat karakter Pac-Man
pacman_radius = 20
pacman_x = SCREEN_WIDTH // 2
pacman_y = SCREEN_HEIGHT // 2
pacman_dx = 0
pacman_dy = 0

# Fungsi menggambar Pac-Man
def draw_pacman(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), pacman_radius)
    mouth_rect = pygame.Rect(x - 10, y - 10, 20, 20)
    pygame.draw.polygon(screen, BLACK, [(x, y), (x + 20, y - 10), (x + 20, y + 10)])

# Game Loop
while True:
    screen.fill(BLACK)
    
    # Mengambil event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Kontrol Pac-Man
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman_dx = -PACMAN_SPEED
                pacman_dy = 0
            if event.key == pygame.K_RIGHT:
                pacman_dx = PACMAN_SPEED
                pacman_dy = 0
            if event.key == pygame.K_UP:
                pacman_dy = -PACMAN_SPEED
                pacman_dx = 0
            if event.key == pygame.K_DOWN:
                pacman_dy = PACMAN_SPEED
                pacman_dx = 0
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                pacman_dx = 0
                pacman_dy = 0

    # Gerakan Pac-Man
    pacman_x += pacman_dx
    pacman_y += pacman_dy

    # Batas layar
    if pacman_x - pacman_radius < 0:
        pacman_x = pacman_radius
    if pacman_x + pacman_radius > SCREEN_WIDTH:
        pacman_x = SCREEN_WIDTH - pacman_radius
    if pacman_y - pacman_radius < 0:
        pacman_y = pacman_radius
    if pacman_y + pacman_radius > SCREEN_HEIGHT:
        pacman_y = SCREEN_HEIGHT - pacman_radius

    # Gambar Pac-Man
    draw_pacman(pacman_x, pacman_y)

    # Update layar
    pygame.display.flip()

    # Kontrol kecepatan frame
    pygame.time.Clock().tick(30)
