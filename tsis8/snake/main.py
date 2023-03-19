import pygame, sys, random
from pygame.math import Vector2
from pygame import Rect
import time


fps = 60
cell_size = 20
cell_number = 20
screen_size = (cell_size * cell_number, cell_size * cell_number)


class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.randomize()

    # drawing snake
    def draw(self, surf): 
        surf.blit(self.image, self.rect)

    # randomly placing snake
    def randomize(self):
        self.pos = Vector2(random.randint(1, cell_number - 1), random.randint(1, cell_number - 1))
        self.image = pygame.transform.scale(pygame.image.load('./assets/cherry.png'), (cell_size, cell_size))
        # create rectangle
        self.rect = Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)



        
class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.pos_list = [Vector2(8, 10), Vector2(7, 10), Vector2(6, 10)]
        self.direction = Vector2(1,0)

        self.head_up = pygame.transform.scale(pygame.image.load("./assets/head.png"), (cell_size, cell_size))
        self.head_down = pygame.transform.scale(pygame.image.load("./assets/head_down.png"), (cell_size, cell_size))
        self.head_right = pygame.transform.scale(pygame.image.load("./assets/head_right.png"), (cell_size, cell_size))
        self.head_left = pygame.transform.scale(pygame.image.load("./assets/head_left.png"), (cell_size, cell_size))

        self.tail_up = pygame.transform.scale(pygame.image.load("./assets/tail.png"), (cell_size, cell_size))
        self.tail_down = pygame.transform.scale(pygame.image.load("./assets/tail_down.png"), (cell_size, cell_size))

        self.tail_right = pygame.transform.scale(pygame.image.load("./assets/tail_right.png"), (cell_size, cell_size))
        self.tail_left = pygame.transform.scale(pygame.image.load("./assets/tail_left.png"), (cell_size, cell_size))

        self.body_vertical = pygame.transform.scale(pygame.image.load("./assets/body_vrt.png"), (cell_size, cell_size))
        self.body_horizontal = pygame.transform.scale(pygame.image.load("./assets/body_hr.png"), (cell_size, cell_size))


        self.body_tr = pygame.transform.scale(pygame.image.load("./assets/body_tr.png"), (cell_size, cell_size))
        self.body_tl = pygame.transform.scale(pygame.image.load("./assets/body_tl.png"), (cell_size, cell_size))
        self.body_br = pygame.transform.scale(pygame.image.load("./assets/body_br.png"), (cell_size, cell_size))
        self.body_bl = pygame.transform.scale(pygame.image.load("./assets/body_bl.png"), (cell_size, cell_size))

        self.head = self.head_right
        self.tail = self.tail_right



       
    # drawing snake
    def draw(self, surf):
        for i, pos in enumerate(self.pos_list):   
            # Rect for positioning
            rect = Rect(int(pos.x * cell_size), int(pos.y * cell_size), cell_size, cell_size)
            # Direction of a head
            if i == 0:
                self.update_head_graphics()
                surf.blit(self.head, rect)
            elif i == len(self.pos_list) - 1:
                self.update_tail_graphics()
                surf.blit(self.tail, rect)
            else:
                prev_pos = self.pos_list[i+1] - pos
                next_pos = self.pos_list[i-1] - pos
                
                if prev_pos.y == next_pos.y:
                    surf.blit(self.body_vertical, rect)
                elif prev_pos.x == next_pos.x:
                    surf.blit(self.body_horizontal, rect)
                else:
                    if prev_pos.x == -1 and next_pos.y == -1 or prev_pos.y == -1 and next_pos.x == -1:
                        surf.blit(self.body_tl, rect)
                    if prev_pos.x == -1 and next_pos.y == 1 or prev_pos.y == 1 and next_pos.x == -1:
                        surf.blit(self.body_bl, rect)
                    if prev_pos.x == 1 and next_pos.y == -1 or prev_pos.y == -1 and next_pos.x == 1:
                        surf.blit(self.body_tr, rect)
                    if prev_pos.x == 1 and next_pos.y == 1 or prev_pos.y == 1 and next_pos.x == 1:
                        surf.blit(self.body_br, rect)


    # snake moving
    def move(self):
        pos_list_copy = self.pos_list[:-1]
        pos_list_copy.insert(0, pos_list_copy[0] + self.direction)
        self.pos_list = pos_list_copy

    # snake eating fruit and increasing its size by 1
    def eat(self):
        pos_list_copy = self.pos_list[:]
        pos_list_copy.insert(0, pos_list_copy[0] + self.direction)
        self.pos_list = pos_list_copy

    def update_head_graphics(self):
        if self.direction == Vector2(0, -1):
            self.head = self.head_up
        elif self.direction == Vector2(0, 1):
            self.head = self.head_down   
        elif self.direction == Vector2(1, 0):
            self.head = self.head_right    
        elif self.direction == Vector2(-1, 0):
            self.head = self.head_left

    def update_tail_graphics(self):
        tail_direction = self.pos_list[-2] - self.pos_list[-1]
        
        if tail_direction == Vector2(0, -1):
            self.tail = self.tail_up
        if tail_direction == Vector2(0, 1):
            self.tail = self.tail_down
        if tail_direction == Vector2(1, 0):
            self.tail = self.tail_right
        if tail_direction == Vector2(-1, 0):
            self.tail = self.tail_left
       


# Class with general logic of the game
class GameLogic:
    # initializing snake and fruit instances
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    # updating the state of the game
    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_fail_states()

    # drawing game elements
    def draw_elements(self, surf, font):
        self.snake.draw(surf)
        self.fruit.draw(surf)
        self.draw_score(surf, font)

    # checking for collision of snake with fruit
    def check_collision(self):
        if self.fruit.pos == self.snake.pos_list[0]:
            self.fruit.randomize()
            self.snake.eat()
    
    def game_over(self):
        pygame.quit()
        sys.exit()

    def check_fail_states(self):
        # checking if snake collides with walls
        if not 0 <= self.snake.pos_list[0].x < cell_number or not 0 <=  self.snake.pos_list[0].y < cell_number:
            self.game_over()

        # checking if snake head collides with itself
        for snake_part in self.snake.pos_list[1:]:
            if snake_part == self.snake.pos_list[0]:
                self.game_over()

    def draw_score(self, surf, font):
        score_text = str(len(self.snake.pos_list) - 3)
        score_surf = font.render(score_text, True, (56,76,12))
        score_surf_pos = (int(cell_size * cell_number - 40), int(cell_size * cell_number - 20))
        score_rect = score_surf.get_rect(center = score_surf_pos)
        surf.blit(score_surf, score_rect)
        apple = self.fruit.image
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        surf.blit(apple, apple_rect)



            

def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    
    snake_game = GameLogic()
    game_font = pygame.font.Font('./assets/Blessed.ttf', 20)


    screen_update = pygame.USEREVENT
    pygame.time.set_timer(screen_update, 150)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == screen_update:
                snake_game.update()
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        if snake_game.snake.direction != Vector2(0, 1):
                            snake_game.snake.direction = Vector2(0, -1)
                    case pygame.K_DOWN:
                        if snake_game.snake.direction != Vector2(0, -1):
                            snake_game.snake.direction = Vector2(0, 1)
                    case pygame.K_RIGHT:
                        if snake_game.snake.direction != Vector2(-1, 0):
                            snake_game.snake.direction = Vector2(1, 0)
                    case pygame.K_LEFT:
                        if snake_game.snake.direction != Vector2(1, 0):
                            snake_game.snake.direction = Vector2(-1, 0)
        
        screen.fill((255, 255, 255)) 
        snake_game.draw_elements(screen, game_font)
        pygame.display.update()
        clock.tick(fps)



if __name__ == "__main__":
    main()
