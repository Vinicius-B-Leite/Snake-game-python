import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

x_tela = 600
y_tela = 400
tela = pygame.display.set_mode((x_tela, y_tela))
clock = pygame.time.Clock()

game_over = False

class Cobra:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.velocidadeX = 3
        self.velocidadeY = 0
        self.limite = 100
        self.corpo = []
        self.cabeca = []

        #self.desenha_corpo = pygame.draw.rect(tela, (0, 255, 0), (0, 0, 20, 20))
        self.cobra = pygame.draw.rect(tela, (0, 255, 0), (self.x, self.y, 20, 20))

    def reset(self):
        self.x = 100
        self.y = 100
        self.velocidadeX = 3
        self.velocidadeY = 0
        self.limite = 5
        self.corpo = []
        self.cobra = pygame.draw.rect(tela, (0, 255, 0), (self.x, self.y, 20, 20))


    def update(self):
        self.y += self.velocidadeY
        self.x += self.velocidadeX
        self.cabeca = []
        self.cabeca.append(self.x)
        self.cabeca.append(self.y)

        if len(self.corpo) >= self.limite:
            del self.corpo[0]

        self.corpo.append(self.cabeca)

        for XeY in self.corpo:
            self.desenha_corpo = pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

        self.cobra = pygame.draw.rect(tela, (0, 255, 0), (self.x, self.y, 20, 20))


class Maca:
    def __init__(self):
        self.XeY = []
        self.x = randint(50, x_tela - 50)
        self.y = randint(50, y_tela - 50)
        self.maca = pygame.draw.rect(tela, (255, 0, 0), (self.x, self.y, 20, 20))


    def update(self):
        self.XeY = [self.x, self.y]
        for xsys in self.XeY:
            if xsys in snake.corpo:
                self.x = randint(50, x_tela - 50)
                self.y = randint(50, y_tela - 50)
        self.maca = pygame.draw.rect(tela, (255, 0, 0), (self.x, self.y, 20, 20))

    def reset(self):
        self.x = randint(50, x_tela - 50)
        self.y = randint(50, y_tela - 50)
        self.maca = pygame.draw.rect(tela, (255, 0, 0), (self.x, self.y, 20, 20))


maca = Maca()
snake = Cobra()
font = pygame.font.SysFont('arial', 30, True, True)
start = True
pontos = 0
while True:
    while start:
        tela.fill((0, 0, 0))
        m = 'Press Keybord'
        t = font.render(m, True, (255, 255, 255))
        tela.blit(t, (170, 100))
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                start = False
            if e.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

    msg = "Game over press  SPACE to reset"
    msg2 = f'{pontos}'
    txt = font.render(msg, True, (255, 255, 255))
    txt3 = font.render(msg2, True, (255, 255, 255))
    tela.fill((0, 0, 0))
    clock.tick(50)

    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
            exit()

        if ev.type == KEYDOWN:
            if ev.key == K_UP or ev.key == K_w:
                if snake.velocidadeY == 3:
                    pass
                else:
                    snake.velocidadeX = 0
                    snake.velocidadeY = -3

            if ev.key == K_DOWN or ev.key == K_s:
                if snake.velocidadeY == -3:
                    pass
                else:
                    snake.velocidadeX = 0
                    snake.velocidadeY = 3

            if ev.key == K_RIGHT or ev.key == K_d:
                if snake.velocidadeX == -3:
                    pass
                else:
                    snake.velocidadeX = 3
                    snake.velocidadeY = 0

            if ev.key == K_LEFT or ev.key == K_a:
                if snake.velocidadeX == 3:
                    pass
                else:
                    snake.velocidadeX = -3
                    snake.velocidadeY = 0

    if snake.cobra.colliderect(maca.maca):
        pontos += 1
        snake.limite += 5
        maca.x = randint(50, x_tela - 50)
        maca.y = randint(50, y_tela - 50)


    if snake.x >= x_tela or snake.y >= y_tela or snake.x <= 0 or snake.y <= 0 or snake.corpo.count(snake.cabeca) > 1:
        game_over = True
        while game_over:
            tela.blit(txt, (80, 100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        maca.reset()
                        snake.reset()
                        pontos = 0
                        game_over = False
            pygame.display.flip()

    maca.update()
    snake.update()
    tela.blit(txt3, (x_tela - 100, 10))
    pygame.display.flip()
