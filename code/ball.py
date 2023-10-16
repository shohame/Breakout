import pygame
from object import  ObjectType
from moving_object import MovingObject
from globals import GameColors, GameDimensions
import math
import numpy as np

class Ball(MovingObject):
    def __init__(self, xy, v_xy):
        type = ObjectType.BALL
        wh = GameDimensions.BALL_WH
        color = GameColors.BALL
        super().__init__(xy, wh, color, type, v_xy)

    def draw(self, screen):
        x, y = self._xy
        r = self._wh[0] / 2
        xc = x + r
        yc = y + r
        color = self._color
        pygame.draw.circle(screen, color, (int(xc), int(yc)), int(r))

    def bounce(self, axis):  # TODO: Think about moving this to MovingObject
        if axis == 'x':
            self._v_xy[0] = -self._v_xy[0]
        elif axis == 'y':
            self._v_xy[1] = -self._v_xy[1]
    def bounce_paddle(self, paddle):  # TODO: Think about moving this to MovingObject
        paddle_cx = paddle.get_xy()[0] + paddle.get_wh()[0] / 2
        paddle_w = paddle.get_wh()[0]
        ball_cx = self.get_xy()[0] + self._wh[0] / 2
        paddle_hw = paddle_w / 2
        self.bounce('y')
        vall_vx, ball_vy = self.get_v_xy()
        ball_v_angle = math.atan2(ball_vy, vall_vx)
        ball_v_size = math.sqrt(ball_vy ** 2 + vall_vx ** 2)
        ball_v_angle = ball_v_angle + (ball_cx - paddle_cx) / paddle_hw * math.pi / 3
        ball_v_angle = np.clip(ball_v_angle, -math.pi / 3, math.pi / 3)
        ang2rad = math.pi / 180
        max_angle = -30 * ang2rad
        min_angle = (-180 + 30) * ang2rad
     #   ball_v_angle = np.clip(ball_v_angle, min_angle, max_angle)
        self.set_v_xy([ball_v_size * math.cos(ball_v_angle), ball_v_size * math.sin(ball_v_angle)])


    def check_collision(self, obj):

        ball_x, ball_y = self.get_xy()
        ball_r = self._wh[0] / 2
        ball_cx, ball_cy = ball_x + ball_r, ball_y + ball_r

        obj_x, obj_y = obj.get_xy()
        obj_w, obj_h = obj.get_wh()

        # Compute brick's boundaries
        object_left = obj_x
        object_right = obj_x + obj_w
        object_top = obj_y
        object_bottom = obj_y + obj_h

        # Compute the closest point in the brick to the ball
        closest_x = max(object_left, min(ball_cx, object_right))
        closest_y = max(object_top, min(ball_cy, object_bottom))

        # Calculate the distance between the ball's center and this closest point
        distance_x = ball_cx - closest_x
        distance_y = ball_cy - closest_y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        # Check for collision
        if distance < ball_r:
            # Ball has collided with the brick

            dy = max( object_top - ball_cy, ball_cy - object_bottom)
            dx = max( object_left - ball_cx, ball_cx - object_right)

            if dx > dy:
                return 'x'
            else:
                return 'y'

        else:
            return ''

    def check_all_collision(self, walls, paddle, blocks):

        for wall in walls:
            hit = self.check_collision(wall)
            if hit == 'x' or hit == 'y':
                self.bounce(hit)

        for block in blocks.copy():
            hit = self.check_collision(block)
            if hit == 'x' or hit == 'y':
                self.bounce(hit)
                blocks.remove(block)

        hit = self.check_collision(paddle)
        if hit == 'y':
            if self._v_xy[1] > 0:
                self.bounce_paddle(paddle)


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