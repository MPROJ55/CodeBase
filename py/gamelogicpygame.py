import pygame

# imports pygame locals for easier access to key coordinates 
from pygame.locals import *
# define class for square objects
# gives methods to sprite.Sprite
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()

        self.surf = pygame.Surface((25, 25))

        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()
# intialiaze the game
pygame.init()
# gives the dimensions / border box for the gam
screen = pygame.display.set_mode((800, 600))
# game loop control variable that keeps game running
gameOn = True 
# populate square objects
square1 = Square()
square2 = Square()
square3 = Square()
square4 = Square()
# game loop that handles everything while game is running
while gameOn: 
    # prepares for player action / handles events
    for event in pygame.event.get():
        # key specfic event that looks for key down
        if event.type == KEYDOWN:

        # another key specfic event however sets the loop control variable to false
        # defines the event
            if event.key == K_BACKSPACE:
                gameOn = False
        # checks for event
        elif event.type == QUIT:
            gameOn = False
    # sets coordinates for square objects 
    screen.blit(square1.surf, (40, 40))
    screen.blit(square2.surf, (40, 530))
    screen.blit(square3.surf, (730, 40))
    screen.blit(square4.surf, (730, 530))
    # shows display with the flip function
    pygame.display.flip()

