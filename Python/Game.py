import pygame

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the game window size to match the screen resolution
infoObject = pygame.display.Info()
WINDOW_WIDTH = infoObject.current_w
WINDOW_HEIGHT = infoObject.current_h

# Scale the objects inside the window to match the new window size
SCALE_WIDTH = WINDOW_WIDTH / SCREEN_WIDTH
SCALE_HEIGHT = WINDOW_HEIGHT / SCREEN_HEIGHT

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Load the background image
background = pygame.image.load("background.png").convert()

# Scale the background image to fit the window size
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the title of the window
pygame.display.set_caption("My Game")

# Set the font
font = pygame.font.Font(None, int(50 * SCALE_HEIGHT))

# Create the start screen text
start_text = font.render("Welcome to My Game!", True, WHITE)

# Get the rectangle for the text
text_rect = start_text.get_rect()

# Center the text
text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Create the "Start Game" button
start_button = pygame.Rect(int(SCREEN_WIDTH * SCALE_WIDTH // 2 - 75 * SCALE_WIDTH), int(SCREEN_HEIGHT * SCALE_HEIGHT // 2 + 50 * SCALE_HEIGHT), int(150 * SCALE_WIDTH), int(50 * SCALE_HEIGHT))

# Create the "Quit Game" button
quit_button = pygame.Rect(int(SCREEN_WIDTH * SCALE_WIDTH // 2 - 75 * SCALE_WIDTH), int(SCREEN_HEIGHT * SCALE_HEIGHT // 2 + 110 * SCALE_HEIGHT), int(150 * SCALE_WIDTH), int(50 * SCALE_HEIGHT))

# Set the background color
screen.fill(BLACK)

# Draw the background image onto the screen
screen.blit(background, (0, 0))

# Draw the text onto the screen
screen.blit(start_text, text_rect)

# Draw the buttons onto the screen
pygame.draw.rect(screen, GREEN, start_button)
pygame.draw.rect(screen, RED, quit_button)

# Set the text for the buttons
start_text = font.render("Start Game", True, BLACK)
quit_text = font.render("Quit Game", True, BLACK)

# Get the rectangle for the button text
start_rect = start_text.get_rect()
quit_rect = quit_text.get_rect()

# Center the button text
start_rect.center = start_button.center
quit_rect.center = quit_button.center

# Draw the button text onto the screen
screen.blit(start_text, start_rect)
screen.blit(quit_text, quit_rect)

# Update the screen
pygame.display.flip()

# Wait for the user to click a button or close the window
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                print("Start Game button clicked!")
            elif quit_button.collidepoint(event.pos):
                done = True

# Quit pygame properly
pygame.quit()
