#!/usr/bin/env python

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

# these calls are slow
font_text = pygame.font.SysFont(None, 200)
font_timer = pygame.font.SysFont(None, 300)

color1 = (30, 70, 255)  # blueish
color2 = (255, 30, 50)  # redish

done = False

program1 = [
    # wait
    {
        'text': 'starting in...',
        'timer': 15
    },

    # minute 1
    {
        'text': 'push ups',
        'timer': 20
    },
    {
        'text': 'plank HOLD',
        'timer': 10
    },
    {
        'text': 'plank 2 elbow',
        'timer': 20
    },
    {
        'text': 'plank HOLD',
        'timer': 10
    },
    # minute 2
    {
        'text': 'push ups',
        'timer': 20
    },
    {
        'text': 'plank HOLD',
        'timer': 10
    },
    {
        'text': 'plank 2 elbow',
        'timer': 20
    },
    {
        'text': 'plank HOLD',
        'timer': 10
    },
    # minute 3
    {
        'text': 'push ups',
        'timer': 20
    },
    {
        'text': 'plank HOLD',
        'timer': 10
    },
    {
        'text': 'plank 2 elbow',
        'timer': 20
    },
    {
        'text': 'plank HOLD',
        'timer': 10
    },
    # minute 4
    {
        'text': 'push ups',
        'timer': 20
    },
    {
        'text': 'plank HOLD',
        'timer': 10
    },
    {
        'text': 'plank 2 elbow',
        'timer': 20
    },
    {
        'text': 'plank HOLD',
        'timer': 10
    },

    # end
    {
        'text': 'you\'re done',
        'timer': 10
    },
]

program2 = [
    # wait
    {
        'text': 'starting in...',
        'timer': 15
    },

    # minute 1
    {
        'text': 'squat hold',
        'timer': 20
    },
    {
        'text': 'REST',
        'timer': 10
    },
    {
        'text': 'squat hold',
        'timer': 20
    },
    {
        'text': 'REST',
        'timer': 10
    },
    # minute 2
    {
        'text': 'squat hold',
        'timer': 20
    },
    {
        'text': 'REST',
        'timer': 10
    },
    {
        'text': 'squat hold',
        'timer': 20
    },
    {
        'text': 'REST',
        'timer': 10
    },
    # minute 3
    {
        'text': 'squat hold',
        'timer': 20
    },
    {
        'text': 'REST',
        'timer': 10
    },
    {
        'text': 'squat hold',
        'timer': 20
    },
    {
        'text': 'REST',
        'timer': 10
    },
    # minute 4
    {
        'text': 'squat hold',
        'timer': 20
    },
    {
        'text': 'REST',
        'timer': 10
    },
    {
        'text': 'squat hold',
        'timer': 20
    },
    {
        'text': 'REST',
        'timer': 10
    },

    # end
    {
        'text': 'you\'re done',
        'timer': 10
    },
]

# which program to display
program = program2

current_step = None

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    if current_step is None:
        if not program:
            time.sleep(5)
            break
        current_step = program.pop(0)

    img_text = font_text.render(str(current_step['text']), True, color1)
    img_timer = font_timer.render(str(current_step['timer']), True, color2)

    current_step['timer'] = current_step['timer'] - 1

    if current_step['timer'] == -1:
        color_temp = color1
        color1 = color2
        color2 = color_temp
        current_step = None

    # 1 frame per second - this makes app fairly unresponsive, should refactor
    clock.tick(1)

    screen.blit(img_text, (60, 120))
    screen.blit(img_timer, (220, 320))
    pygame.display.update()

pygame.quit()
