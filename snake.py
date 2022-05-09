import pygame
from pygame.locals import *  # importa tudo com o *
import random

WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10


def collision(pos1, pos2):
    return pos1 == pos2  # se forem iguais, a cobra colidiu entre si


def off_limites(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:  # limites da janela
        return False  # dentro dos limites
    else:
        return True  # fora dos limites


def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

snake_pos = [(250, 50), (260, 50), (270, 50)]  # posição da cobra
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))  # corpo da cobra
snake_surface.fill((255, 255, 255))  # cor da cobra
snake_direction = K_LEFT

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))  # corpo da maça
apple_surface.fill((255, 0, 0))  # cor da maça
apple_pos = random_on_grid()


def restart_game(): # restarta ao inves de fechar
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()


while True:
    pygame.time.Clock().tick(15)  # delay de movimentação
    screen.fill((0, 0, 0))  # pinta a tela toda de preto
    for event in pygame.event.get():  # lista todos os eventos atuais
        if event.type == QUIT:  # pra fechar o programa
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:  # quando uma tecla é pressionada para BAIXO
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:  # confere se é algumas das setas
                snake_direction = event.key

    screen.blit(apple_surface, apple_pos)  # comando pra "desenhar" a maça na tela

    if collision(apple_pos, snake_pos[0]):  # checa se a cobra ta colidindo com a maça
        snake_pos.append((-10, -10))  # acrescenta a maça na posição 0 da cobra
        apple_pos = random_on_grid()

    for pos in snake_pos:
        screen.blit(snake_surface, pos)  # comando pra "desenhar" a cobra na tela

    for i in range(len(snake_pos) - 1, 0, -1):  # começa da cauda
        if collision(snake_pos[0], snake_pos[i]):
            restart_game()
        snake_pos[i] = snake_pos[i - 1]  # substitui a ultima posição

    if off_limites(snake_pos[0]):
        restart_game()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    pygame.display.update()
