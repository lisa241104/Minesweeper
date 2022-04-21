import pygame as pg
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

        self.flag = False
        self.status = ''

    def is_clicked(self, pos):
        # return true if the mouse position is on the cell
        return (self.rect.centerx - 15 < pos[0] < self.rect.centerx + 15) and \
                (self.rect.centery - 15 < pos[1] < self.rect.centery + 15)

    def revealed(self, screen):
        if self.flag:
            self.image = load_image('GamePictures/flag.png')
        elif self.status == 'bomb':
            self.image = load_image('GamePictures/bomb.png')
        elif self.status == 'empty':
            self.image = load_image('GamePictures/opened.png')
        elif self.status == '1':
            self.image = load_image('GamePictures/1.png')
        elif self.status == '2':
            self.image = load_image('GamePictures/2.png')
        elif self.status == '3':
            self.image = load_image('GamePictures/3.png')
        elif self.status == '4':
            self.image = load_image('GamePictures/4.png')
        elif self.status == '5':
            self.image = load_image('GamePictures/5.png')
        elif self.status == '6':
            self.image = load_image('GamePictures/6.png')
        elif self.status == '7':
            self.image = load_image('GamePictures/7.png')
        elif self.status == '8':
            self.image = load_image('GamePictures/8.png')
        self.draw(screen)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
