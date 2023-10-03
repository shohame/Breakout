from object import Object

class Brick(Object):
    def __init__(self, xy, wh, color, type, v_xy=(0, 0)):
        super().__init__(xy, wh, color, type)
        self._v_xy = v_xy


    def get_v_xy(self):
        return self._v_xy

    def set_v_xy(self, v_xy):
        self._v_xy = v_xy

    def move(self, dt):
        x, y = self._xy
        vx, vy = self._v_xy
        self._xy = (x + vx * dt, y + vy * dt)