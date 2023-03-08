import pygame
from datetime import datetime
import math


def blit_rotate_center(surf, image, pos, orig_pos, angle):
    image_rect = image.get_rect(center = (pos[0] - orig_pos[0], pos[1] - orig_pos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    surf.blit(rotated_image, rotated_image_rect)
    pygame.draw.rect(surf, (255, 0, 0), rotated_image_rect, 2)



def blitRotate(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = image.get_rect(topleft = pos).center)

    surf.blit(rotated_image, rotated_image_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), rotated_image_rect, 2)


def main():

    # pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    # get the current time
    curr_time = datetime.now()

    # dict for minutes and seconds of a clock
    clock60 = dict(zip(range(60), range(0, 360, 6)))

    # loading the images 
    clock_image = pygame.transform.scale(pygame.image.load('./images/mickeyclock.jpeg'), (800, 600))
    seconds_hand_image = pygame.transform.scale(pygame.image.load('./images/seconds.png'), (150, 80))
    minutes_hand_image = pygame.transform.scale(pygame.image.load('./images/minutes.png'), (130, 70))

    angle = 0
    seconds_pos = (clock_image.get_width() / 2, clock_image.get_height() / 2)
    minutes_pos = (screen.get_width() / 2, screen.get_height() / 2)
    w, h = seconds_hand_image.get_size()
    isRunning = True

    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        screen.fill(0)
        pos = seconds_pos

        screen.blit(clock_image, (0, 0))
        blit_rotate_center(screen, seconds_hand_image, seconds_pos, (w/2, h/2), angle) 
        angle += 1
                

        pygame.display.flip()

        clock.tick(24)


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
