import pygame

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def is_overlapping(new_x, new_y, block_width, block_height, blocks, min_gap=50):
    for bx, by in blocks:
        if abs(new_x - bx) < block_width + min_gap and abs(new_y - by) < block_height + min_gap:
            return True
    return False
