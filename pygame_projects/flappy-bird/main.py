import pygame
import os
from random import randint
pygame.font.init()

run = True

WIDTH, HEIGHT = 400, 600
 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Flappy Bird")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

HIDDEN_BARRIER = pygame.Rect(-100, 0, 30, HEIGHT)

WALL_RENDER = pygame.USEREVENT + 0

SCORE_FONT = pygame.font.SysFont('leelawadeeuisemilight', 20)
GAME_OVER_FONT = pygame.font.SysFont('arialblack', 40)

FPS = 60


class Bird:
    
    def __init__(self):
        self.body = pygame.Rect(70, 200, 25, 25)
        self.is_jumping = 0
        self.delay = 0
        self.score = 0
        
    def bird_handle_gravity(self):
        
        if self.is_jumping == 0:
            self.body.y += 4
            
        elif self.is_jumping > 0:
            self.body.y -= 4
            bird.is_jumping -= 1
        
    def jump(self, power):

        self.is_jumping = power

class Wall:
    
    def __init__(self, place, height):
        if place == 'UP':
            self.body = pygame.Rect(WIDTH, 0, 30, height)
        elif place == 'DOWN':
            self.body = pygame.Rect(WIDTH, HEIGHT - height, 30, height)

    def move(self):
        self.body.x -= 3
        
    
bird = Bird()
walls = []
hidden_walls = []

def handle_walls(timer):
    if timer == 100:
        pygame.event.post(pygame.event.Event(WALL_RENDER))
    for wall in walls:
        if wall.body.colliderect(HIDDEN_BARRIER):
            walls.remove(wall)
        elif wall.body.colliderect(bird.body):
            game_over()
        elif bird.body.y >= HEIGHT - bird.body.height or bird.body.y <= 0:
            game_over()
        else:
            wall.move()
    
    for wall in hidden_walls:
        if bird.body.x == wall.body.x + wall.body.width:
            bird.score += 1
            hidden_walls.remove(wall)
        else:
            wall.move()

def game_over():
    global run
    clock = pygame.time.Clock()
    
    while hidden_walls != []:
        wall = hidden_walls[-1]
        hidden_walls.remove(wall)
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and bird.body.y >= HEIGHT - bird.body.height:
                    while walls != []:
                        wall = walls[-1]
                        walls.remove(wall)
                    begin_window()

        if bird.body.y <= HEIGHT - bird.body.height:
            bird.body.y += 8
            draw_window()
        
        lose_text = GAME_OVER_FONT.render("GAME OVER", 1, RED)
        WIN.blit(lose_text, ((WIDTH - lose_text.get_width())//2 , 150)) 
        pygame.display.update() 
    
    
    pygame.quit()
    
    
    
def begin_window():
    global run
    bird.score = 0
    bird.body.y = 200
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump(20)
                    main()
        
        draw_window()
        
    pygame.quit() 


def draw_window():
    WIN.fill(WHITE)
    
    score_text = SCORE_FONT.render(f"SCORE : {bird.score}", 1, BLACK)
    WIN.blit(score_text, (5, 5))
    
    pygame.draw.rect(WIN, BLACK, bird.body)
    
    for wall in walls:
        pygame.draw.rect(WIN, BLACK, wall.body)
    
    pygame.display.update()

def main():
    global run
    timer = 0
    clock = pygame.time.Clock()
    while run:
        down_wall_h = randint(150, 350)
        up_wall_h = 500 - down_wall_h 
        clock.tick(FPS)
        timer += 1
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump(20)
            
            if event.type == WALL_RENDER:
                walls.append(Wall('DOWN', down_wall_h))
                walls.append(Wall('UP', up_wall_h))
                hidden_walls.append(Wall('DOWN', HEIGHT))
                timer = 0 
        
        handle_walls(timer)  
        draw_window()
        bird.bird_handle_gravity()
    
    pygame.quit()
        
    
if __name__ == "__main__":
    begin_window()