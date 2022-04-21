import pygame as pg
from minesweeper import Minesweeper
from load_image import load_image


class Cell(pg.sprite.Sprite):
    def __init__(self, pos, row, column):
        # Call the parent class (Sprite) constructor
        pg.sprite.Sprite.__init__(self)

        self.image = load_image('GamePictures/empty.png')

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.rect.center = pos
        self.row = row
        self.column = column

        self.closed = True

    def is_clicked(self, pos):
        # return true if the mouse position is on the cell
        return (self.rect.centerx - 15 < pos[0] < self.rect.centerx + 15) and \
                (self.rect.centery - 15 < pos[1] < self.rect.centery + 15)

    def set_image(self, image):
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, self.rect)
