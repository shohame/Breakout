import pygame
import random
from globals import GameDimensions as g_dim
from build_game_objects import get_objects
from game_sync import GameSync

# Initialize pygame
pygame.init()

# Screen and clock
screen = pygame.display.set_mode(g_dim.SCREEN_WH) #, pygame.DOUBLEBUF) # | pygame.FULLSCREEN)

pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()


# get_objects:
paddle, balls, walls, bricks = get_objects()

running = True

game_sync = GameSync()
i=0
t = pygame.time.get_ticks()
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.set_v_xy((-100, 0))
            if event.key == pygame.K_RIGHT:
                paddle.set_v_xy((100, 0))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle.set_v_xy((0, 0))

    dt = game_sync.get_dt()
    balls[0].move(dt)
    paddle.move(dt)

    balls[0].check_all_collision(walls, paddle, bricks)

    balls[0].draw(screen)
    paddle.draw(screen)
    for wall in walls:
        wall.draw(screen)

    for brick in bricks:
        brick.draw(screen)


    pygame.display.flip()
    clock.tick(60)
    i+=1
    if i%100==0:
        print (i)
pygame.quit()
