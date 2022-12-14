import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

# white color
color = (255, 255, 255)
# light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (100, 100, 100)

width = screen.get_width()
height = screen.get_height()

smallfont = pygame.font.SysFont('Corbel', 35)

text = smallfont.render('quit', True, color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()

                # fills the screen with a color
    screen.fill((255, 128, 128))
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, (int(width / 2), int(height / 2), 140, 40))

    else:
        pygame.draw.rect(screen, color_dark, (int(width / 2), int(height / 2), 140, 40))

    screen.blit(text, (int(width / 2) + 50, int(height / 2)))
    pygame.display.update()