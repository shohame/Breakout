
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

    bricks = []
    for y in range(30, g_dim.SCREEN_WH[1] - 300, 30):
        for x in range(50 + 25*(y%30), g_dim.SCREEN_WH[0] - 50, 80):

            bricks.append(Brick([x, y]))
    objects['bricks'] = bricks

    return objects
