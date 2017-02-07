import pygame

sensitivity = 5
class Tile (pygame.sprite.Sprite):



    def __init__(self, x ,y):
        super(Tile, self).__init__()
        self.image =  pygame.image.load("tile.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.selected = False
        self.count = 0
        self.owned = False
        self.owned_red = False
        self.amount = 0
        self.occupied = 0
        self.occupied_red = 0
    def move(self,y):
        self.rect.y = y
    def update(self,un_select=False):
        self.count += 1
        if self.selected:
            self.image = pygame.image.load("tile_clicked.png")
        if un_select:
            self.selected = False
        if self.owned:
            self.image = pygame.image.load("tile_owned.png")
        if self.owned and self.selected:
            self.image = pygame.image.load("tile_owned_selected.png")
        if self.owned_red:
            self.image = pygame.image.load("tile_red.png")
        if self.owned_red and self.selected:
            self.image = pygame.image.load("tile_red_selected.png")
        if self.occupied == 10:
            self.owned = True
        if self.occupied_red == 10:
            self.owned_red = True
        if self.occupied == 0:
            self.owned = False
        if self.occupied_red == 0:
            self.owned_red = False

    def hover(self):
        self.image = pygame.image.load("tile_hover.png")
    def un_hover(self):
        self.image = pygame.image.load("tile.png")
    def clicked(self):
        if self.selected and self.count >= sensitivity:
            self.selected = False
            self.count = 0
        elif self.count >= sensitivity :
            self.selected = True
            self.count = 0


