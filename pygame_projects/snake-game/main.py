import pygame
import os
import random
pygame.font.init()

WIDTH, HEIGHT = 800, 400

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

run =  True

BLACK = (0, 0, 0)
YELLOW = (255, 207, 44)
GREEN = (161, 255, 164)
RED = (255, 0, 0)
BROWN = (102, 35, 35)

LEFT_WALL = pygame.Rect(0, 0, 10, HEIGHT)
RIGHT_WALL = pygame.Rect(WIDTH-10, 0, 10, HEIGHT)
TOP_WALL = pygame.Rect(0, 0, WIDTH, 10)
BOTTOM_WALL = pygame.Rect(0, HEIGHT-10, WIDTH, 10)

SCORE_FONT = pygame.font.SysFont('comicsans', 20)

FPS = 10

class Snake: 
    
    def __init__(self):
        self.dirs = {'RIGHT':False, 'LEFT':False, 'UP':False, 'DOWN':False}
        self.vel = 20
        self.head = pygame.Rect(50, 50, 20, 20)
        self.body = []
        self.score = 0
        
    def set_dir(self, keys_pressed):
    
        if keys_pressed[pygame.K_RIGHT] and self.dirs['LEFT'] == False:
            for dir in self.dirs:
                self.dirs[dir] = False
            self.dirs['RIGHT'] = True
            
        elif keys_pressed[pygame.K_LEFT] and self.dirs['RIGHT'] == False:
            for dir in self.dirs:
                self.dirs[dir] = False
            self.dirs['LEFT'] = True
            
        elif keys_pressed[pygame.K_UP] and self.dirs['DOWN'] == False:
            for dir in self.dirs:
                self.dirs[dir] = False
            self.dirs['UP'] = True
            
        elif keys_pressed[pygame.K_DOWN] and self.dirs['UP'] == False:
            for dir in self.dirs:
                self.dirs[dir] = False
            self.dirs['DOWN'] = True
    
    def snake_handle_movement(self):
        follow_y, follow_x = self.head.y, self.head.x
        if self.body != [] : atlas = self.body[0]
        
        if self.dirs['RIGHT'] == True:
            self.head.x += self.vel
            if self.body != []:
                follow_y, follow_x = atlas.y, atlas.x
                
                atlas.x = self.head.x - atlas.width
                atlas.y = self.head.y
                
        if self.dirs['LEFT'] == True:
            self.head.x -= self.vel
            if self.body != []:
                follow_y, follow_x = atlas.y, atlas.x
                
                atlas.x = self.head.x + atlas.width
                self.body[0].y = self.head.y
                
        if self.dirs['UP'] == True:
            self.head.y -= self.vel
            if self.body != []:
                follow_y, follow_x = atlas.y, atlas.x
                
                atlas.y = self.head.y + atlas.width
                self.body[0].x = self.head.x
                
        if self.dirs['DOWN'] == True:
            self.head.y += self.vel
            if self.body != []:
                follow_y, follow_x = atlas.y, atlas.x
                
                atlas.y = self.head.y - atlas.width
                atlas.x = self.head.x
        
        if self.body != []:
            for vertebra in self.body[1:]:
                follow2_y, follow2_x = vertebra.y, vertebra.x
                vertebra.y = follow_y
                vertebra.x = follow_x
                follow_y, follow_x = follow2_y, follow2_x
                
                if vertebra.colliderect(self.head):
                    pygame.draw.rect(WIN, (0, 0, 0), vertebra)
                    pygame.display.update()
                    game_over()
    
    def handle_collision(self):
        if snake.head.colliderect(RIGHT_WALL):
            game_over()
        if snake.head.colliderect(LEFT_WALL):
            game_over()
        if snake.head.colliderect(TOP_WALL):
            game_over()
        if snake.head.colliderect(BOTTOM_WALL):
            game_over()
    
class Food:
    def __init__(self):
        self.seed = pygame.Rect(66, 66, 10, 10)  
    
    def render_seed(self):
        self.seed.x = random.randint(20, WIDTH - 20)
        self.seed.y = random.randint(20, HEIGHT - 20)
        
    def handle_seed(self, snake):
        if snake.head.colliderect(self.seed):
            self.render_seed()
            snake.body.append(pygame.Rect(50, 50, 20, 20))
            snake.score += 1
            
snake = Snake()
seed = Food()

def game_over():
    global run
    pygame.time.delay(5000)
    run = False

def draw_window():
    WIN.fill(GREEN)
    
    score_text = SCORE_FONT.render(f"SCORE: {snake.score-1}", 1, BLACK)
    WIN.blit(score_text, (12, HEIGHT - 40))
    
    pygame.draw.rect(WIN, BROWN, RIGHT_WALL)
    pygame.draw.rect(WIN, BROWN, LEFT_WALL)
    pygame.draw.rect(WIN, BROWN, TOP_WALL)
    pygame.draw.rect(WIN, BROWN, BOTTOM_WALL)
    pygame.draw.rect(WIN, RED, seed.seed)
    pygame.draw.rect(WIN, YELLOW, snake.head)
    
    for vertebra in snake.body:
        pygame.draw.rect(WIN, YELLOW, vertebra)

    pygame.display.update()

def main():
    global run
    
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        seed.handle_seed(snake)
        snake.set_dir(keys_pressed)
        snake.snake_handle_movement()
        snake.handle_collision()
        draw_window()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()