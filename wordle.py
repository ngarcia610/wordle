import pygame
import sys

# Constants
WIDTH, HEIGHT = 500, 700
ROWS, COLS = 6, 5
TILE_SIZE = 70
TILE_MARGIN = 10
TOP_OFFSET = 100
BACKGROUND_COLOR = (18, 18, 19)
TILE_COLOR = (58, 58, 60)
TEXT_COLOR = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle in Python")
font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

# Function to draw the grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * (TILE_SIZE + TILE_MARGIN) + (WIDTH - (COLS * (TILE_SIZE + TILE_MARGIN))) // 2
            y = row * (TILE_SIZE + TILE_MARGIN) + TOP_OFFSET
            pygame.draw.rect(screen, TILE_COLOR, (x, y, TILE_SIZE, TILE_SIZE), border_radius=5)

# Game loop
def main():
    while True:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_grid()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
