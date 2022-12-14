import pygame
import time
import random
 #inporting is fun idk how it works but it thas 
pygame.init()
#activating the pygame 
snake_speed = 10
#difain 
window_x = 720
window_y = 480
# difain the size of the window 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
 #color using rbg color coding 
pygame.display.set_caption('fuck Snakes your mom shit is not good looking!!!!')
game_window = pygame.display.set_mode((window_x, window_y))
 #
fps = pygame.time.Clock()
 
snake_position = [100, 50]
 
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]


fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
direction = 'RIGHT'
change_to = direction
 
score = 0
 

def show_score(choice, color, font, size):
   
    score_font = pygame.font.SysFont(font, size)
     
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    score_rect = score_surface.get_rect()
     
    game_window.blit(score_surface, score_rect)
 
def game_over():

   
    my_font = pygame.font.SysFont('times new roman', 50)
     
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    game_over_rect = game_over_surface.get_rect()
     
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    time.sleep(0.60)
    

    
    pygame.quit()
     
    quit()
 

#this difans the movenet of the snake witch is good 
while True:
     
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 # and this cople of line of code makes the body grow when eating the "fruit"
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         #
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
#whis ubove the ´` fills the window / game backround witch a previsely difand colors 
#and the one under thet draw 
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 # the meaning of the code below means  is thet if the snake trys to go of screen ore the hit the adg?? speling it will resalt in a game over 
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 #idk 
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    show_score(1, white, 'times new roman', 20)
 #this is an inportent code for game making with pygame in visuels studios thas alow to update the screen. so if this wos not in hare we wold-
 #the window starts but thare will not bea eny of the stuf we reote haha ore if we put this line of code up this will resalt in falier to yay
    pygame.display.update()
 #fps tick sets the fps sped 
    fps.tick(snake_speed)
