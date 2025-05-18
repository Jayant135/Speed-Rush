import pygame
import random
from config import *
from utils import is_overlapping
from game_objects import car, things
from ui import pause_menu, game_over_menu

def game_loop(gameDisplay, clock, car_img, crash_sound):
    dodged = 0
    pause = False

    x = DISPLAY_WIDTH * 0.45
    y = DISPLAY_HEIGHT * 0.8
    x_change = 0

    num_blocks = 5
    blocks = []
    attempts = 0

    while len(blocks) < num_blocks and attempts < 1000:
        block_x = random.randrange(0, DISPLAY_WIDTH - BLOCK_WIDTH)
        block_y = random.randrange(-int(DISPLAY_HEIGHT * 1.5), -BLOCK_HEIGHT)

        if not is_overlapping(block_x, block_y, BLOCK_WIDTH, BLOCK_HEIGHT, blocks):
            blocks.append([block_x, block_y])
        attempts += 1

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -CAR_SPEED
                elif event.key == pygame.K_RIGHT:
                    x_change = CAR_SPEED
                elif event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    pause = True

                    def unpause():
                        nonlocal pause
                        pause = False

                    while pause:
                        for ev in pygame.event.get():
                            if ev.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if ev.type == pygame.KEYDOWN:
                                if ev.key == pygame.K_p or ev.key == pygame.K_SPACE:
                                    pause = False
                        pause_menu(gameDisplay, clock, unpause, pygame.quit)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(WHITE)

        for i in range(len(blocks)):
            blocks[i][1] += BLOCK_SPEED
            things(gameDisplay, blocks[i][0], blocks[i][1], BLOCK_WIDTH, BLOCK_HEIGHT, BLACK)

            if blocks[i][1] > DISPLAY_HEIGHT:
                while True:
                    new_x = random.randrange(0, DISPLAY_WIDTH - BLOCK_WIDTH)
                    new_y = random.randrange(-int(DISPLAY_HEIGHT * 1.5), -100)
                    if not is_overlapping(new_x, new_y, BLOCK_WIDTH, BLOCK_HEIGHT, blocks[:i] + blocks[i + 1:]):
                        blocks[i][0] = new_x
                        blocks[i][1] = new_y
                        break
                dodged += 1
            
            max_blocks = num_blocks + dodged // 15  # for example, increase with dodged
            if len(blocks) < max_blocks:
                block_x = random.randrange(0, DISPLAY_WIDTH - BLOCK_WIDTH)
                block_y = random.randrange(-int(DISPLAY_HEIGHT * 1.5), -100)
                if not is_overlapping(block_x, block_y, BLOCK_WIDTH, BLOCK_HEIGHT, blocks[:i] + blocks[i+1:]):
                    blocks.append([block_x, block_y])

            if y < blocks[i][1] + BLOCK_HEIGHT:
                if (x > blocks[i][0] and x < blocks[i][0] + BLOCK_WIDTH) or (x + CAR_WIDTH > blocks[i][0] and x + CAR_WIDTH < blocks[i][0] + BLOCK_WIDTH):
                    crash_sound.play()
                    while True:
                        for ev in pygame.event.get():
                            if ev.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        game_over_menu(gameDisplay, clock, dodged, lambda: game_loop(gameDisplay, clock, car_img, crash_sound), pygame.quit)

        car(gameDisplay, car_img, x, y)

        font = pygame.font.SysFont(None, 25)
        score_text = font.render("Score: " + str(dodged), True, BLACK)
        score_rect = score_text.get_rect(topright=(DISPLAY_WIDTH - 10, 10))
        gameDisplay.blit(score_text, score_rect)

        if x > (DISPLAY_WIDTH - CAR_WIDTH) or x < 0:
            crash_sound.play()
            while True:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                game_over_menu(gameDisplay, clock, dodged, lambda: game_loop(gameDisplay, clock, car_img, crash_sound), pygame.quit)

        pygame.display.update()
        clock.tick(60)
