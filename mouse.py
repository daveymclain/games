import pygame


class Mouse (pygame.sprite.Sprite):


    def __init__(self):
        super(Mouse, self).__init__()
        self.image =  pygame.image.load("mouse.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self,x,y):
        self.rect.y = y
        self.rect.x = x
    def draw(self,surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
