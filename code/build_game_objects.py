
from ball import Ball
from paddle import Paddle
from wall import Wall
from brick import Brick
from globals import GameDimensions as g_dim



def get_general_objects():
    screen_w, screen_h = g_dim.SCREEN_WH

    balls = [Ball((screen_w / 2, screen_h - 100), [100, -200])]
    paddel_w, paddel_h = g_dim.PADDLE_WH
    paddle = Paddle([screen_w / 2, screen_h - paddel_h- 20])
    wall_th = g_dim.WALL_THICKNESS
    # Creating list of 3 walls, left, right and top:
    walls = [Wall([0, 0], [wall_th, screen_h]),
                Wall([screen_w - wall_th, 0], [wall_th, screen_h]),
                Wall([0, 0], [screen_w, wall_th])]

#    walls.append(Wall([0, screen_h - wall_th], [screen_w, wall_th]))

    objects = {}
    objects['balls'] = balls
    objects['paddle'] = paddle
    objects['walls'] = walls

    return objects


def get_objects():
    objects = get_general_objects()


    screen_w, screen_h = g_dim.SCREEN_WH
    brick_w, brick_h = g_dim.BRICK_WH
    wall_th = g_dim.WALL_THICKNESS
    bricks_space = 20
    w = screen_w - 2 * wall_th
    wn = w // (brick_w + bricks_space)
    # Creating list of bricks in a line left to right
    number_of_lines = 5
    bricks = []

    for yi in range(number_of_lines):
        for xi in range(wn):
            x = 30 + (yi % 2) * (brick_w + bricks_space) // 2 + xi * (brick_w + bricks_space)
            y = 30 + yi * (brick_h + bricks_space)
            bricks.append(Brick([x, y]))

    objects['bricks'] = bricks

    return objects
