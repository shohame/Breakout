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

    def check_collision(self, obj):

        ball_x, ball_y = self.get_xy()
        ball_r = self._wh[0] / 2
        ball_cx, ball_cy = ball_x + ball_r, ball_y + ball_r

        obj_x, obj_y = obj.get_xy()
        obj_w, obj_h = obj.get_wh()

        # Compute brick's boundaries
        brick_left = obj_x
        brick_right = obj_x + obj_w
        brick_top = obj_y
        brick_bottom = obj_y + obj_h

        # Compute the closest point in the brick to the ball
        closest_x = max(brick_left, min(ball_cx, brick_right))
        closest_y = max(brick_top, min(ball_cy, brick_bottom))

        # Calculate the distance between the ball's center and this closest point
        distance_x = ball_cx - closest_x
        distance_y = ball_cy - closest_y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        # Check for collision
        if distance < ball_r:
            # Ball has collided with the brick

            # If ball hits top or bottom of brick, invert Y velocity
            if ball_cy <= brick_top or ball_cy >= brick_bottom:
                self.bounce('y')

            # If ball hits left or right of brick, invert X velocity
            if ball_cx <= brick_left or ball_cx >= brick_right:
                self.bounce('x')

            return True
        else:
            return False

    def check_all_collision(self, walls, paddle, blocks):

        for wall in walls:
            self.check_collision(wall)

        for block in blocks.copy():
            do_remove = self.check_collision(block)
            if do_remove:
                blocks.remove(block)

        self.check_collision(paddle)

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