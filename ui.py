import pygame
from config import *
from utils import text_objects

def button(gameDisplay, msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, small_text, BLACK)
    textRect.center = (x + w / 2, y + h / 2)
    gameDisplay.blit(textSurf, textRect)

def pause_menu(gameDisplay, clock, unpause_func, quit_func):
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects("Paused", largeText, RED)
    TextRect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
    gameDisplay.blit(TextSurf, TextRect)

    button_width = int(DISPLAY_WIDTH * 0.2)
    button_height = int(DISPLAY_HEIGHT * 0.1)

    continue_x = int(DISPLAY_WIDTH * 0.2)
    quit_x = int(DISPLAY_WIDTH * 0.6)
    button_y = int(DISPLAY_HEIGHT * 0.75)

    button(gameDisplay, "Continue", continue_x, button_y, button_width, button_height, GREEN, BRIGHT_GREEN, unpause_func)
    button(gameDisplay, "QUIT", quit_x, button_y, button_width, button_height, RED, BRIGHT_RED, quit_func)

    pygame.display.update()
    clock.tick(15)

def game_over_menu(gameDisplay, clock, score, unpause_func, quit_func):
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects("Game Over", largeText, RED)
    TextRect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2 - 50)
    gameDisplay.blit(TextSurf, TextRect)

    score_font = pygame.font.Font('freesansbold.ttf', 40)
    score_text, score_rect = text_objects(f"Score: {score}", score_font, BLACK)
    score_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2 + 20)
    gameDisplay.blit(score_text, score_rect)

    button_width = int(DISPLAY_WIDTH * 0.2)
    button_height = int(DISPLAY_HEIGHT * 0.1)

    continue_x = int(DISPLAY_WIDTH * 0.2)
    quit_x = int(DISPLAY_WIDTH * 0.6)
    button_y = int(DISPLAY_HEIGHT * 0.75)

    button(gameDisplay, "Play Again", continue_x, button_y, button_width, button_height, GREEN, BRIGHT_GREEN, unpause_func)
    button(gameDisplay, "QUIT", quit_x, button_y, button_width, button_height, RED, BRIGHT_RED, quit_func)

    pygame.display.update()
    clock.tick(15)
