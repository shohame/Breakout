import numpy as np
from vector import Vector
class Object:
    def __init__(self, xy, wh, color, type):
        self._xy = Vector(xy)    # x, y - middle of the brick
        self._wh = Vector(wh)    # width, height
        self._color = color
        self._type = type

    def get_xy(self):
        return self._xy

    def get_wh(self):
        return self._wh

    def get_type(self):
        return self._type



if __name__=="__main__":
    brick = Object((100, 200), (50, 20), (255, 0, 0), "normal")
    print(f'brick.get_xy() = {brick.get_xy()}')
    print(f'brick.get_wh() = {brick.get_wh()}')
    print(f'brick.get_type() = {brick.get_type()}')
