from sys import exit
import pygame

# Initializing pygame engine
pygame.init()

# initializing display surface
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
# setting name for the game
pygame.display.set_caption("Jump King")

#initializing clock object to control time and framerate
clock = pygame.time.Clock()

# creating a image surface object 
sky_surface = pygame.image.load('graphics/bg/Layer_0010_1.png').convert_alpha()
tree_top = pygame.image.load('graphics/bg/Layer_0002_7.png').convert_alpha()
tree_trunk = pygame.image.load('graphics/bg/Layer_0003_6.png').convert_alpha()
tree_trunk_back = pygame.image.load('graphics/bg/Layer_0005_5.png').convert_alpha()
tree_trunk_back_back = pygame.image.load('graphics/bg/Layer_0006_4.png').convert_alpha()
tree_trunk_bg = pygame.image.load('graphics/bg/Layer_0009_2.png').convert_alpha()
ground_surface = pygame.image.load('graphics/bg/Layer_0001_8.png').convert_alpha()
dirt_surface = pygame.image.load('graphics/bg/layer_0000_9.png').convert_alpha()
light_surface = pygame.image.load('graphics/bg/Layer_0004_Lights.png').convert_alpha()
light_surface_back = pygame.image.load('graphics/bg/Layer_0007_Lights.png').convert_alpha()

# creating a text surface
test_font = pygame.font.Font('graphics/fonts/Pixeltype.ttf', 50)
text_surface = test_font.render('My world', False, 'Green')

# creating an image surface for skeleton creature
skeleton_idle_surface = pygame.image.load('graphics/creatures/Skeleton/Idle.png').convert_alpha()
skeleton_x_pos = 400


# Initializing infinite loop to run the game
while True:  
    # Checking for any player input in event loop
    for event in pygame.event.get():
        # checking whether player pressed quit button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all elements
    # update all events
    
    # displaying images surfaces on the display surface
    # first surfaces displayed are displayed in the back
    # later surfaces cover before surfaces
    screen.blit(sky_surface, (0, 0))
    screen.blit(tree_trunk_bg, (0,-100))    
    screen.blit(tree_top, (0, -100))
    screen.blit(light_surface_back, (0, -100))
    screen.blit(tree_trunk_back_back, (0, -100))
    screen.blit(tree_trunk_back, (0, -100))
    screen.blit(light_surface, (0, -100))
    screen.blit(tree_trunk,(0, -100))
    screen.blit(ground_surface, (0, -170))
    screen.blit(dirt_surface, (0, -170))

    # displaying text surface
    screen.blit(text_surface, (300, 10))

    # displaying skeleton image moving
    skeleton_x_pos -= 2
    if skeleton_x_pos < -500:
        skeleton_x_pos = 800
    screen.blit(skeleton_idle_surface, (skeleton_x_pos, 500))
    pygame.display.update()
    
    #setting the maximum framerate to 60fps
    clock.tick(60)
