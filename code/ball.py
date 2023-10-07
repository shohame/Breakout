import pygame
from object import  ObjectType
from moving_object import MovingObject
from globals import GameColors, GameDimensions

class Ball(MovingObject):
    def __init__(self, xy, v_xy):
        type = ObjectType.BALL
        wh = GameDimensions.BALL_WH
        color = GameColors.BALL
        super().__init__(xy, wh, color, type, v_xy)

    def draw(self, screen):
        # draw a circle
        x, y = self._xy
        w, h = self._wh
        color = self._color
        pygame.draw.circle(screen, color, (int(x), int(y)), int(w/2))

    def bounce(self, axis):  # TODO: Think about moving this to MovingObject
        if axis == 'x':
            self._v_xy[0] = -self._v_xy[0]
        elif axis == 'y':
            self._v_xy[1] = -self._v_xy[1]

    def check_collision(self, walls, paddle, blocks):
        # Check collision with paddle
        pad_x, pad_y = paddle.get_xy()
        pad_w, pad_h = paddle.get_wh()
        self_x, self_y = self.get_xy()
        self_w, self_h = self.get_wh()
        if (pad_x <= self_x <= pad_x + pad_w) and (pad_y <= self_x + self_w / 2 <= pad_y + pad_h):
            self.bounce('y')

        # Check collision with blocks
        for block in blocks.copy():
            blk_x, blk_y = block.get_xy()
            blk_w, blk_h = block.get_wh()

            if (self_x <= self_x <= self_x + self_w) and (
                    blk_y <= self_y - self_w <= blk_y + blk_h or
                    blk_y <= self_y + self_w <= blk_y + blk_h):
                blocks.remove(block)
                self.bounce('y')
                break


if __name__=="__main__":
    ball = Ball((400, 200), (-3,4))
    print(f'ball.get_xy() = {ball.get_xy()}')
    print(f'ball.get_wh() = {ball.get_wh()}')
    print(f'ball.get_type() = {ball.get_type()}')
    print(f'ball.get_color() = {ball.get_color()}')
    print(f'ball.get_v_xy() = {ball.get_v_xy()}')
     # Print the name of the class:
    print(ball.__class__.__name__)
    # Print the name of the base class:
    print(ball.__class__.__base__.__name__)