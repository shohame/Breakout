import pygame
from object import Object, ObjectType
from globals import GameColors, GameDimensions

class Brick(Object):
    def __init__(self, xy):
        wh = GameDimensions.BRICK_WH
        type = ObjectType.BRICK
        color = GameColors.BRICK
        super().__init__(xy, wh, color, type)

    def draw(self, screen):
        x, y = self._xy
        w, h = self._wh
        color = self._color
        pygame.draw.rect(screen, color, (x-w/2, y-h/2, w, h))



if __name__=="__main__":

    brick = Brick((400, 200), (255, 0, 0))
    print(f'brick.get_xy() = {brick.get_xy()}')
    print(f'brick.get_wh() = {brick.get_wh()}')
    print(f'brick.get_type() = {brick.get_type()}')
    print(f'brick.get_color() = {brick.get_color()}')
     # Print the name of the class:
    print(brick.__class__.__name__)
    # Print the name of the base class:
    print(brick.__class__.__base__.__name__)
