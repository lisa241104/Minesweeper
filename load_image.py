import pygame as pg


def load_image(image):
    i = pg.image.load(image)
    i = pg.transform.scale(i, (30, 30))
    return i
