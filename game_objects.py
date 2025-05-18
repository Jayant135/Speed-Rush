import pygame

def car(gameDisplay, car_img, x, y):
    gameDisplay.blit(car_img, (x, y))

def things(gameDisplay, thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
