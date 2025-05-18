import pygame
import config
import ui
import game

pygame.init()

gameDisplay = pygame.display.set_mode((config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT))
pygame.display.set_caption('Speed-Rush')

car_img = pygame.image.load('race_car.png')
icon = pygame.image.load('race_car.jpg')
pygame.display.set_icon(icon)

crash_sound = pygame.mixer.Sound('crash.ogg')

clock = pygame.time.Clock()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(config.WHITE)
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf = largeText.render("Speed Rush", True, config.RED)
        TextRect = TextSurf.get_rect()
        TextRect.center = (config.DISPLAY_WIDTH / 2, config.DISPLAY_HEIGHT / 2)
        gameDisplay.blit(TextSurf, TextRect)

        button_width = int(config.DISPLAY_WIDTH * 0.2)
        button_height = int(config.DISPLAY_HEIGHT * 0.1)

        go_x = int(config.DISPLAY_WIDTH * 0.2)
        quit_x = int(config.DISPLAY_WIDTH * 0.6)
        button_y = int(config.DISPLAY_HEIGHT * 0.75)

        ui.button(gameDisplay, "GO!", go_x, button_y, button_width, button_height,
                  config.GREEN, config.BRIGHT_GREEN,
                  lambda: game.game_loop(gameDisplay, clock, car_img, crash_sound))

        ui.button(gameDisplay, "QUIT", quit_x, button_y, button_width, button_height,
                  config.RED, config.BRIGHT_RED, pygame.quit)

        pygame.display.update()
        clock.tick(15)

if __name__ == "__main__":
    game_intro()
    pygame.quit()
    quit()

