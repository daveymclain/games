import pygame
import random


random_movements = 2

class Man (pygame.sprite.Sprite):


    def __init__(self,x,y,file_image):
        super(Man, self).__init__()
        self.image =  pygame.image.load(file_image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.selected = False
        self.dest_x = self.rect.x
        self.dest_y = self.rect.y


    def move(self,x,y):
            self.dest_x = x
            self.dest_y = y



    def draw(self,surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        if self.dest_x > self.rect.x:
            self.rect.x += random_movements + random.randrange(-random_movements,random_movements)
        if self.dest_y > self.rect.y:
            self.rect.y += random_movements + random.randrange(-random_movements,random_movements)
        if self.dest_x < self.rect.x:
            self.rect.x -= random_movements + random.randrange(-random_movements,random_movements)
        if self.dest_y < self.rect.y:
            self.rect.y -= random_movements + random.randrange(-random_movements,random_movements)