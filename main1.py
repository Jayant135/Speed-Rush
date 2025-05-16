import pygame
import time
import random

pygame.init()

# Constants
display_width = 800
display_height = 600
car_width = 41

white = (255,255,255)
black = (0,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
red = (200,0,0)
green = (0,200,0)
dodged = 0

# Setup
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Speed Rush')
clock = pygame.time.Clock()

carImg = pygame.image.load('race_car.png')
icon = pygame.image.load('race_car.jpg')
pygame.display.set_icon(icon)
crash_sound = pygame.mixer.Sound("crash.wav")

# Game state
pause = False
x_change = 0

# Functions
def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(count), True, black)
    text_rect = text.get_rect(topright=(display_width - 10, 10))
    gameDisplay.blit(text, text_rect)

def draw_obstacle(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def crash():
    pygame.mixer.Sound.play(crash_sound)
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects("Game Over", largeText, red)
    TextRect.center = ((display_width / 2), (display_height / 2) - 50)
    gameDisplay.blit(TextSurf, TextRect)

    #  Display the score 
    score_font = pygame.font.Font('freesansbold.ttf', 40)
    score_text, score_rect = text_objects(f"Score: { dodged } ", score_font, black)
    score_rect.center = ((display_width / 2), (display_height / 2) + 20)
    gameDisplay.blit(score_text, score_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play again", 100, 450, 160, 60, green, bright_green, game_loop)
        button("QUIT", 550, 450, 100, 60, red, bright_red, quitGame)
        pygame.display.update()
        clock.tick(15)

def quitGame():
    pygame.quit()
    quit()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    small_text = pygame.font.Font("freesansbold.ttf", 30)
    textSurf, textRect = text_objects(msg, small_text, black)
    textRect.center = (x + w/2, y + h/2)
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False

def game_pause():
    global pause
    pause = True
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects("Paused", largeText, red)
    TextRect.center = (display_width/2, display_height/2)
    gameDisplay.blit(TextSurf, TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Continue", 150, 450, 120, 60, green, bright_green, unpause)
        button("QUIT", 550, 450, 100, 60, red, bright_red, quitGame)
        pygame.display.update()
        clock.tick(15)

def move_left():
    global x_change
    x_change = -5

def move_right():
    global x_change
    x_change = 5

def stop_movement():
    global x_change
    x_change = 0

def game_loop():
    global x_change, pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    obstacle_speed = 7
    obstacle_width = 100
    obstacle_height = 100

    num_obstacles = 3
    obstacles = []

    for _ in range(num_obstacles):
        start_x = random.randrange(0, display_width - obstacle_width)
        start_y = random.randrange(-800, -100)
        obstacles.append([start_x, start_y])

    dodged = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                stop_movement()

        x += x_change
        gameDisplay.fill(white)

        # Draw all obstacles
        for i in range(num_obstacles):
            draw_obstacle(obstacles[i][0], obstacles[i][1], obstacle_width, obstacle_height, black)
            obstacles[i][1] += obstacle_speed

            if obstacles[i][1] > display_height:
                obstacles[i][1] = random.randint(-600, -100)
                obstacles[i][0] = random.randrange(0, display_width - obstacle_width)
                dodged += 1

            # Collision
            if y < obstacles[i][1] + obstacle_height:
                if x + car_width > obstacles[i][0] and x < obstacles[i][0] + obstacle_width:
                    crash()

        car(x, y)
        things_dodged(dodged)

        # UI buttons
        button("||", 10, 10, 60, 60, white, (200, 200, 200), game_pause)
        button("<", 50, display_height - 100, 80, 80, green, bright_green, move_left)
        button(">", display_width - 130, display_height - 100, 80, 80, green, bright_green, move_right)

        if x < 0 or x > display_width - car_width:
            crash()

        pygame.display.update()
        clock.tick(60)

def game_intro():
    intro = True 
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects("Speed Rush", largeText, red)
        TextRect.center = (display_width/2, display_height/2)
        gameDisplay.blit(TextSurf, TextRect)
        button("GO!", 150, 450, 100, 60, green, bright_green, game_loop)
        button("QUIT", 550, 450, 100, 60, red, bright_red, quitGame)
        pygame.display.update()
        clock.tick(15)


# Run Game
game_intro()
pygame.quit()
quit()
