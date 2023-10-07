
from ball import Ball
from paddle import Paddle
from wall import Wall
from brick import Brick
from globals import GameDimensions as g_dim

def get_objects():
    screen_w, screen_h = g_dim.SCREEN_WH

    balls = [Ball((400, 200), [-300,400])]
    paddle = Paddle((400, 200))
    wall_w = 10
    # Creating list of 3 walls, left, right and top:
    walls = [Wall([0, 0], [wall_w, screen_h]),
                Wall([screen_w-wall_w, 0], [wall_w, screen_h]),
                Wall([0, 0], [screen_w, wall_w])]

  #  bricks = [Block(x * BLOCK_WIDTH, y * BLOCK_HEIGHT) for y in range(BLOCK_ROWS) for x in range(BLOCK_COLS)]


    bricks = [Brick((50, 50)), Brick((150, 50))]
    return paddle, balls, walls, bricks


