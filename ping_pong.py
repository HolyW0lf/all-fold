import pygame
from pygame.locals import *
pygame.init()


###variables 
w = 900
h = 900
y = 100
x = 100


screen = pygame.display.set_mode((w, h))
#icontitle=None
pygame.display.set_caption("din mamma ")
image = pygame.Surface.get_at((x, y))

y = 100
x = 100


velocity = 12

run = True
while run:
    screen.fill(0, 0, 0)    

    screen.blit(image, (x, y))

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
           pygame.quit
           quit()

         # Checking event key if the type
        # of the event is KEYDOWN i.e.
        # keyboard button is pressed
    if event.type == pygame.KEYDOWN:
  
            # Decreasing the x coordinate
            # if the button pressed is
            # Left arrow key
            if event.key == pygame.K_LEFT:
                x -= velocity
  
            # Increasing the x coordinate
            # if the button pressed is
            # Right arrow key
            if event.key == pygame.K_RIGHT:
                x += velocity
  
            # Decreasing the y coordinate
            # if the button pressed is
            # Up arrow key
            if event.key == pygame.K_UP:
                y -= velocity
  
            # Increasing the y coordinate
            # if the button pressed is
            # Down arrow key
            if event.key == pygame.K_DOWN:
                y += velocity
  
        # Draws the surface object to the screen.
    pygame.display.update()
