import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake attributes
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"
change_to = direction
score = 0
level = 1
speed = 15
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]

# Function to display text on screen
def show_text(text, color, x, y, size=32):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

# Main game loop
game_over = False
clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Check for invalid directions
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Move snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    # Check for collision with wall
    if snake_pos[0] < 0 or snake_pos[0] > width - 10 or snake_pos[1] < 0 or snake_pos[1] > height - 10:
        game_over = True

    # Check for collision with snake's body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # Check for collision with food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        snake_body.append(list(snake_pos))
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]

        # Increase speed every 3 foods
        if score % 3 == 0:
            level += 1
            speed += 3

    else:
        snake_body.insert(0, list(snake_pos))
        snake_body.pop()

    # Draw background
    screen.fill(black)

    # Draw snake
    for block in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(block[0], block[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, green, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Display score and level
    show_text(f"Score: {score}", white, 50, 10)
    show_text(f"Level: {level}", white, 50, 40)

    # Update display
    pygame.display.update()

    # Control game speed
    clock.tick(speed)

# Game over message
show_text("Game Over", red, width/2, height/2)
pygame.display.update()
pygame.time.wait(2000)
pygame.quit()
sys.exit()
