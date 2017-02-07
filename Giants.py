import pygame
import random
from tile import  Tile as tile
from mouse import  Mouse as mouse
from man import  Man as man


pygame.init()

pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

FPS = 25
spawn_freq = 24
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
random_number_limit = 30

display_width = 1000
display_hight = 800

smallFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)

gameDisplay = pygame.display.set_mode([display_width,display_hight])


def main():
    game_over = False
    tile_width = 180
    board_across = 5
    board_down = 13
    board_start_x = 178
    board_start_y = 52
    spawn_count = 0
    mouse_image = mouse()
    right_click_x = None
    right_click_y = None
    right_clicked = False
    moved = False
    moved_count = 0

    tile_sprite_group_y = pygame.sprite.Group()
    human_sprite_group = pygame.sprite.Group()
    human_red_sprite_group = pygame.sprite.Group()

    #***generate board x****
    for e in range(0,board_across):
        board_x = board_start_x  * e
        if e < board_across:
            for i in range(0,board_down):
                if i % 2 == 0:
                    tile_y = tile((board_x + tile_width/2) , board_start_y * i)
                    tile_sprite_group_y.add(tile_y)
                else:
                    tile_y = tile(board_x, board_start_y *i)
                    tile_sprite_group_y.add(tile_y)

    list_to_kill = [0,1,2,3,5,7,9,10,11,12,13,14,24,25,39,51,52,53,54,62,63,64]
    for i in reversed(list_to_kill):
        tile_sprite_group_y.sprites()[i].kill()
    tile_sprite_group_y.update()
    tile_sprite_group_y.sprites()[1].occupied = 10
    tile_sprite_group_y.sprites()[12].occupied_red = 10
    tile_sprite_group_y.sprites()[20].occupied_red = 10

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    tile_sprite_group_y.update(True)

        gameDisplay.fill(black)

        pos =pygame.mouse.get_pos()

        mouse_image.update(pos[0],pos[1])

        spawn_count += 1

        if right_clicked and moved and moved_count >= 1:
            tile_sprite_group_y.update(True)
            right_clicked = False
            moved = False
            moved_count = 0
        if moved:
            moved_count += 1


        for s in tile_sprite_group_y:
            if s.owned and s.amount <= 500 and spawn_count == spawn_freq:
                human = man(s.rect.center[0]-10+random.randrange(-random_number_limit,random_number_limit),
                            s.rect.center[1]-10+random.randrange(-random_number_limit,random_number_limit),"man.png")
                human_sprite_group.add(human)
                s.amount += 1
            if  s.selected and right_clicked and pygame.sprite.collide_mask(s,mouse_image):
                for hum in human_sprite_group:
                    if pygame.sprite.collide_mask(s, hum):
                        if not s.owned and s.occupied_red == 0 and s.occupied < 10:
                            s.occupied += 1
                            hum.kill()
                        if s.owned_red and 0 < s.occupied_red :
                            s.occupied_red -= 1
                            hum.kill()
                for hum in human_red_sprite_group:
                    if pygame.sprite.collide_mask(s, hum):
                        if not s.owned_red and s.occupied == 0 and s.occupied_red < 10:
                            s.occupied_red += 1
                            hum.kill()
                        if s.owned and 0 < s.occupied :
                            s.occupied -= 1
                            hum.kill()
                tile_sprite_group_y.update(True)
            if s.owned_red and s.amount <= 500 and spawn_count == spawn_freq:
                human = man(s.rect.center[0]-10+random.randrange(-random_number_limit,random_number_limit),
                            s.rect.center[1]-10+random.randrange(-random_number_limit,random_number_limit),"man_red.png")
                human_red_sprite_group.add(human)
                s.amount += 1
            if s.selected:
                for hum in human_sprite_group:
                    if pygame.sprite.collide_mask(s, hum) and right_clicked:
                        hum.move(right_click_x + random.randrange(-random_number_limit,random_number_limit),
                                 right_click_y + random.randrange(-random_number_limit,random_number_limit))
                        moved = True

                for hum in human_red_sprite_group:
                    if pygame.sprite.collide_mask(s, hum) and right_clicked:
                        hum.move(right_click_x + random.randrange(-random_number_limit,random_number_limit),
                                 right_click_y + random.randrange(-random_number_limit,random_number_limit))
                        moved = True
            if pygame.sprite.collide_mask(s,mouse_image):
                s.hover()
                if pygame.mouse.get_pressed()[0]:
                    s.clicked()
                    right_clicked = False
                if pygame.mouse.get_pressed()[2]:
                    right_clicked = True
                    right_click_x = s.rect.center[0]-10
                    right_click_y = s.rect.center[1]-10
            else:
                s.un_hover()
            if spawn_count == spawn_freq + 1:
                spawn_count = 0

        #***human collision***
        for blue in human_sprite_group:
            for red in human_red_sprite_group:
                if pygame.sprite.collide_mask(blue, red):
                    blue.kill()
                    red.kill()

        tile_sprite_group_y.update()
        human_sprite_group.update()
        human_red_sprite_group.update()
        tile_sprite_group_y.draw(gameDisplay)
        human_sprite_group.draw(gameDisplay)
        human_red_sprite_group.draw(gameDisplay)
        mouse_image.draw(gameDisplay)
        pygame.display.flip()
        clock.tick(FPS)

main()