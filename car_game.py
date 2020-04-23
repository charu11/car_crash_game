import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = 0, 0, 0
white = 255, 255, 255

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

car_width = 73

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Racey')
clock = pygame.time.Clock()
car_img = pygame.image.load('racecar.png')


def things_dodged(count):
    font = pygame.font.sysFont(None, 25)
    text = font.render('Dodged:' + str(count), True, black)
    game_display.blit(text, (0, 0))


def things(thing_x, thing_y, thing_w, thing_h, color):
    pygame.draw.rect(game_display, color, [thing_x, thing_y, thing_w, thing_h])


def car(x, y):
    game_display.blit(car_img, (x, y))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 100)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    game_display.blit(text_surf, text_rect)

    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('you crashed')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    # car_speed = 0
    # defining the obstracles
    thing_start_x = random.randrange(0, display_width)
    thing_start_y = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 1001

    dodged = 0

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

    game_display.fill(white)

    # things(thing_x, thing_y, thing_w, thing_h, color)
    things(thing_start_x, thing_start_y, thing_width, thing_height, black)
    thing_start_y += thing_speed
    car(x, y)
    things_dodged(dodged)

    if x > display_width - car_width or x < 0:
        crash()

    if thing_start_y > display_height:
        thing_start_y = 0 - thing_height
        thing_start_x = random.randrange(0, display_width)
        dodged += 1
        thing_speed += 1
        thing_width += (dodged * 1.2)

        # defining the crashing
    if y < thing_start_y + thing_height:
        print('y crossover')

        if x > thing_start_x and x < thing_start_x + thing_width or x + car_width > thing_start_x:
            print('x crossover')
            crash()

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()

