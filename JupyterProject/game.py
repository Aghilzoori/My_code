import random
import time
import pygame

pygame.init()
display_width = 800
display_height = 600


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Jupyter Project')
clock = pygame.time.Clock()

carimage = pygame.image.load('Untitled1 (4).png')

car_width = 55

xx = 350
yy = 500

def score(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(count), True, black)
    gameDisplay.blit(text, [0, 0])

def stuff(stuffx, stuffy, stuffw, stuffh, color):
    pygame.draw.rect(gameDisplay, color, [stuffx, stuffy, stuffw, stuffh])


def car(x, y):
    gameDisplay.blit(carimage, (x, y))

def taxt_objects(taxt, font):
    TextStyle = font.render(taxt, True, black)
    TextRect = TextStyle.get_rect()
    return TextStyle, TextRect

def massage_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TaxtRrct = taxt_objects(text, largeText)
    TaxtRrct.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TaxtRrct)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    massage_display('nott na not ')


def game_loop():
    xx = 350
    yy = 500
    x_Change = 0
    stuff_startx = random.randrange(0, display_width) and random.randrange(0, display_height)
    stuff_starty = -400
    stuff_speed = 7
    stuff_width = 100
    stuff_height = 100
    scoree = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_Change = -5
                elif event.key == pygame.K_RIGHT:
                    x_Change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_Change = 0

        xx += x_Change

        gameDisplay.fill(white)
        stuff(stuff_startx, stuff_starty, stuff_width, stuff_height, red)
        stuff_starty += stuff_speed
        score(scoree)
        car(xx, yy)


        if xx > display_width - car_width or xx < 0:
            crash()
        if stuff_starty > display_height:
            stuff_starty = 0 - stuff_height
            stuff_startx = random.randrange(0, display_width)
            scoree += 1

            if (scoree % 5 == 0):
                stuff_speed += 1

        if stuff_starty + stuff_height > yy:
            if (xx < stuff_startx + stuff_width) and (xx + car_width > stuff_startx):
                crash()

        pygame.display.update()
        clock.tick(100)


game_loop()
pygame.quit()
quit()