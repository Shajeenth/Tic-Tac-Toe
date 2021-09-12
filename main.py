import pygame
import sys
import time
from TicTacToe import TicTacToe
import random
pygame.init()

icon = pygame.image.load("logo.png")
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((300, 350))
game = TicTacToe()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            j, i = [ x // 100 for x in pygame.mouse.get_pos()]
            game.move((i, j))

    screen.fill((0, 0, 0))
    game.display(screen)

    pygame.display.update()
