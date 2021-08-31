import pygame
import time
from System import System
pygame.init()



icon = pygame.image.load("logo.png")
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((300, 350))
board = pygame.image.load('tic_tac_toe.png')
img_x = pygame.image.load('x.png')
img_o = pygame.image.load('o.png')
mouse_clicks = 0
ind_x = pygame.image.load('x_indicator.png')
ind_o = pygame.image.load('o_indicator.png')
xwin = pygame.image.load('Xwin.png')
owin = pygame.image.load('Owin.png')

state = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]

system = System()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicks += 1
            x, y = pygame.mouse.get_pos()
            if mouse_clicks % 2 == 1:
                if round(x) in range(0, 100) and round(y) in range(0, 100):
                    if state[0] == 0:
                        state[0] = 1
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(100, 200) and round(y) in range(0, 100):
                    if state[1] == 0:
                        state[1] = 1
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(200, 300) and round(y) in range(0, 100):
                    if state[2] == 0:
                        state[2] = 1
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(0, 100) and round(y) in range(100, 200):
                    if state[3] == 0:
                        state[3] = 1
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(100, 200) and round(y) in range(100, 200):
                    if state[4] == 0:
                        state[4] = 1
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(200, 300) and round(y) in range(100, 200):
                    if state[5] == 0:
                        state[5] = 1
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(0, 100) and round(y) in range(200, 300):
                    if state[6] == 0:
                        state[6] = 1
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(100, 200) and round(y) in range(200, 300):
                    if state[7] == 0:
                        state[7] = 1
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(200, 300) and round(y) in range(200, 300):
                    if state[8] == 0:
                        state[8] = 1
                    else:
                        mouse_clicks -= 1
            elif mouse_clicks % 2 == 0:
                if round(x) in range(0, 100) and round(y) in range(0, 100):
                    if state[0] == 0:
                        state[0] = 2
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(100, 200) and round(y) in range(0, 100):
                    if state[1] == 0:
                        state[1] = 2
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(200, 300) and round(y) in range(0, 100):
                    if state[2] == 0:
                        state[2] = 2
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(0, 100) and round(y) in range(100, 200):
                    if state[3] == 0:
                        state[3] = 2
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(100, 200) and round(y) in range(100, 200):
                    if state[4] == 0:
                        state[4] = 2
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(200, 300) and round(y) in range(100, 200):
                    if state[5] == 0:
                        state[5] = 2
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(0, 100) and round(y) in range(200, 300):
                    if state[6] == 0:
                        state[6] = 2
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(100, 200) and round(y) in range(200, 300):
                    if state[7] == 0:
                        state[7] = 2
                    else:
                        mouse_clicks -= 1
                elif round(x) in range(200, 300) and round(y) in range(200, 300):
                    if state[8] == 0:
                        state[8] = 2
                    else:
                        mouse_clicks -= 1




    screen.fill((0, 0, 0))
    screen.blit(board,(0,0))
    if state[0] == 1:
        screen.blit(img_x, (0, 0))
    if state[1] == 1:
        screen.blit(img_x, (100, 0))
    if state[2] == 1:
        screen.blit(img_x, (200, 0))
    if state[3] == 1:
        screen.blit(img_x, (0, 100))
    if state[4] == 1:
        screen.blit(img_x, (100, 100))
    if state[5] == 1:
        screen.blit(img_x, (200, 100))
    if state[6] == 1:
        screen.blit(img_x, (0, 200))
    if state[7] == 1:
        screen.blit(img_x, (100, 200))
    if state[8] == 1:
        screen.blit(img_x, (200, 200))
    if state[0] == 2:
        screen.blit(img_o, (0, 0))
    if state[1] == 2:
        screen.blit(img_o, (100, 0))
    if state[2] == 2:
        screen.blit(img_o, (200, 0))
    if state[3] == 2:
        screen.blit(img_o, (0, 100))
    if state[4] == 2:
        screen.blit(img_o, (100, 100))
    if state[5] == 2:
        screen.blit(img_o, (200, 100))
    if state[6] == 2:
        screen.blit(img_o, (0, 200))
    if state[7] == 2:
        screen.blit(img_o, (100, 200))
    if state[8] == 2:
        screen.blit(img_o, (200, 200))

    if mouse_clicks%2 == 1:
        screen.blit(ind_o, (0, 300))
    if mouse_clicks%2 == 0 or mouse_clicks == 0:
        screen.blit(ind_x, (0, 300))

    system.if_o_win(state)
    system.if_x_win(state)

    if system.o_win == True:
        screen.blit(owin, (0, 0))

    if system.x_win == True:
        screen.blit(xwin, (0, 0))
    pygame.display.update()