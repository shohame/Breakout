import pygame
from object import  ObjectType
from moving_object import MovingObject
from globals import GameColors, GameDimensions
from globals import GameDimensions as g_dim

class Paddle(MovingObject):
    def __init__(self, xy):
        type = ObjectType.PADDLE
        wh = GameDimensions.PADDLE_WH
        color = GameColors.PADDLE
        v_xy = (0, 0)
        super().__init__(xy, wh, color, type, v_xy)

    def draw(self, screen):
        x, y = self._xy
        w, h = self._wh
        color = self._color
        pygame.draw.rect(screen, color, (x, y, w, h))

    def move(self, dt):
        super().move(dt)
        self._xy[0] = max(0, min(g_dim.SCREEN_WH[0] - g_dim.PADDLE_WH[0], self._xy[0]))

if __name__=="__main__":
    ball = Paddle((400, 200), (255, 0, 0))
    print(f'ball.get_xy() = {ball.get_xy()}')
    print(f'ball.get_wh() = {ball.get_wh()}')
    print(f'ball.get_type() = {ball.get_type()}')
    print(f'ball.get_color() = {ball.get_color()}')
    print(f'ball.get_v_xy() = {ball.get_v_xy()}')
     # Print the name of the class:
    print(ball.__class__.__name__)
    # Print the name of the base class:
    print(ball.__class__.__base__.__name__)