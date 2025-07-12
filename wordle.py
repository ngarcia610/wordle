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
letters = [["" for _ in range(COLS)] for _ in range(ROWS)]
current_row = 0
current_col = 0

with open("words.txt") as f:
    valid_words = set(word.strip().upper() for word in f.readlines())

# Example target word to guess (you can randomize it later)
target_word = "CRANE"

# Function to draw the grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * (TILE_SIZE + TILE_MARGIN) + (WIDTH - (COLS * (TILE_SIZE + TILE_MARGIN))) // 2
            y = row * (TILE_SIZE + TILE_MARGIN) + TOP_OFFSET
            pygame.draw.rect(screen, TILE_COLOR, (x, y, TILE_SIZE, TILE_SIZE), border_radius=5)

            if letters[row][col] != "":
                letter_surface = font.render(letters[row][col], True, TEXT_COLOR)
                letter_rect = letter_surface.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
                screen.blit(letter_surface, letter_rect)

# Game loop
def main():
    global current_row, current_col

    while True:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if current_col > 0:
                        current_col -= 1
                        letters[current_row][current_col] = ""
                elif event.key == pygame.K_RETURN:
                    if current_col == COLS:
                        guess = "".join(letters[current_row])
                        if guess in valid_words:
                            print("Valid guess:", guess)
                            if guess == target_word:
                                print("🎉 You guessed the word!")
                            else:
                                current_row += 1
                                current_col = 0
                        else:
                            print("❌ Invalid word. Try again.")
                elif event.unicode.isalpha() and len(event.unicode) == 1:
                    if current_col < COLS and current_row < ROWS:
                        letters[current_row][current_col] = event.unicode.upper()
                        current_col += 1

        draw_grid()
        pygame.display.flip()
        clock.tick(60)
c
if __name__ == "__main__":
    main()
