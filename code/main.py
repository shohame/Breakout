import pygame
import random
from globals import GameDimensions as g_dim
from build_game_objects import get_objects
from game_sync import GameSync
import math
# Initialize pygame
pygame.init()

# Screen and clock
screen = pygame.display.set_mode(g_dim.SCREEN_WH, pygame.DOUBLEBUF) # | pygame.FULLSCREEN)

pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

objects = get_objects()

balls = objects['balls']
paddle = objects['paddle']
walls = objects['walls']
bricks = objects['bricks']

running = True
game_sync = GameSync()
i=0
t = pygame.time.get_ticks()
pygame.event.set_grab(True)
pygame.mouse.set_visible(True)
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.set_v_xy((-100, 0))
            if event.key == pygame.K_RIGHT:
                paddle.set_v_xy((100, 0))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle.set_v_xy((0, 0))
    """
    mouse_x, mouse_y = pygame.mouse.get_pos()
    paddle.set_xy((mouse_x - paddle._wh[0]/2, paddle.get_xy()[1]))
    if mouse_y < 5:
        pygame.event.set_grab(False)
    else:
        pygame.event.set_grab(True)

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

    vall_vx, ball_vy = balls[0].get_v_xy()
    ball_v_angle = math.atan2(ball_vy, vall_vx)
    print (ball_v_angle / math.pi * 180)
    pygame.display.flip()
    clock.tick(60)
    i+=1
    if i%100==0:
        print (i)
pygame.quit()
