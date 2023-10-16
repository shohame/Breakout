import numpy as np

class ObjectType:
    BRICK = "brick"
    BALL = "ball"
    PADDLE = "paddle"
    WALL = "wall"



class Object:
    def __init__(self, xy, wh, color, type):
        self._xy = list(xy)    # x, y - middle of the brick
        self._wh = list(wh)    # width, height
        self._color = color
        self._type = type
    """
    @property
    def x(self):
        return self._xy[0]

    @x.setter
    def x(self, value):
        self._xy[0] = value

    @property
    def y(self):
        return self._xy[1]

    @y.setter
    def y(self, value):
        self._xy[1] = value
    @property
    def w(self):
        return self._wh[0]

    @w.setter
    def w(self, value):
        self._wh[0] = value

    @property
    def h(self):
        return self._wh[1]
    @h.setter
    def h(self, value):
        self._wh[1] = value
    """
    def draw(self, screen):
        pass

    def get_xy(self):
        return self._xy

    def set_xy(self, xy):
        self._xy = xy

    def get_wh(self):
        return self._wh

    def get_type(self):
        return self._type

    def get_color(self):
        return self._color



if __name__=="__main__":
    brick = Object((100, 200), (50, 20), (255, 0, 0), "normal")
    print(f'brick.get_xy() = {brick.get_xy()}')
    print(f'brick.get_wh() = {brick.get_wh()}')
    print(f'brick.get_type() = {brick.get_type()}')
