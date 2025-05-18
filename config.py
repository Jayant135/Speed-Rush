import pygame

pygame.init()
info = pygame.display.Info()

DISPLAY_WIDTH = info.current_w
DISPLAY_HEIGHT = info.current_h

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)

CAR_WIDTH = 41
BLOCK_WIDTH = 100
BLOCK_HEIGHT = 100

CAR_SPEED = 5
BLOCK_SPEED = 7
