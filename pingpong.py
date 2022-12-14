import pygame, sys

from pygame.locals import  *

pygame.init


###game screen and colors###
colorwh = (255, 255, 255)
coloror = (255, 165, 0)
colorbl = (0, 0, 0)
colorna = (0, 0, 128)
w = 1000
h = 1000
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("ping pong")



###variables###

y_movement1 = 265
y_movement2 = 265
x_velocity = 300
y_velocity = 300
gy = 25
sp2 = 585
sp1 = 15

###function###
def borders():
    pygame.draw.rect(screen, colorna, (0, 0, 600, gy) )
    pygame.draw.rect(screen, colorna, (0, 600, 600, -gy))

def objects():
    pygame.draw.rect(screen, coloror, (sp1, y_movement1, 10, 25))
    pygame.draw.rect(screen, coloror, (sp2, y_movement2, -10, 25))
    pygame.draw.rect(screen, colorwh, (x_velocity, y_velocity, 7.5, 7.5))

### main loop ###
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)

    event = pygame.event.get()
    borders()
    objects()

    x_velocity += 5
    y_velocity -= 5

    if y_velocity < gy:
        x_velocity += 5
        y_velocity += 5
    if x_velocity == 600:
        x_velocity = 300
        y_velocity = 300
    if x_velocity == 0:
        x_velocity = 300
        y_velocity = 300
    if x_velocity + 7.5 == sp2 and y_velocity < 300:
         x_velocity -= 5
         y_velocity += 5
    if x_velocity + 7.5 ==  sp2 and y_velocity > 300:
        x_velocity -= 5
        y_velocity -= 5
    if x_velocity == sp1 and y_velocity < 300:
        x_velocity += 5
        y_velocity += 5
    if x_velocity == sp1 and y_velocity > 300:
        x_velocity += 5
        y_velocity -= 5

        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and  y_movement1 > 25:
        y_movement1 -= 6
    if keys[pygame.K_s] and  y_movement1 < 575 - 25 -6 :
        y_movement1 += 6
    if keys[pygame.K_u] and y_movement2 > 25:
        y_movement2 -= 6
    if keys[pygame.K_j] and y_movement2 < 550 - 25 - 6:
        y_movement2 += 6

    screen.fill(colorbl)

    borders()
    objects()

    for event in event:
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        else:
            pygame.display.flip()

pygame.quit()








