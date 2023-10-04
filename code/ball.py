import pygame
from moving_object import MovingObject
from globals import GameColors, GameDimensions

class Ball(MovingObject):
    def __init__(self, xy, color, type, v_xy):
        wh = GameDimensions.BALL_WH
        super().__init__(xy, wh, color, type, v_xy)

    def draw(self, screen):
        # draw a circle
        x, y = self._xy
        w, h = self._wh
        color = self._color
        pygame.draw.circle(screen, color, (int(x), int(y)), int(w/2))

if __name__=="__main__":
    ball = Ball((400, 200), (255, 0, 0), "normal")
    print(f'ball.get_xy() = {ball.get_xy()}')
    print(f'ball.get_wh() = {ball.get_wh()}')
    print(f'ball.get_type() = {ball.get_type()}')
    print(f'ball.get_color() = {ball.get_color()}')
    print(f'ball.get_v_xy() = {ball.get_v_xy()}')
     # Print the name of the class:
    print(ball.__class__.__name__)
    # Print the name of the base class:
    print(ball.__class__.__base__.__name__)