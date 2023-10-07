from object import Object

class MovingObject(Object):
    def __init__(self, xy, wh, color, type, v_xy=(0, 0)):
        super().__init__(xy, wh, color, type)
        self._v_xy = list(v_xy)

    def get_v_xy(self):
        return self._v_xy

    def set_v_xy(self, v_xy):
        self._v_xy = v_xy

    def move(self, dt):
        x, y = self._xy
        vx, vy = self._v_xy
        self._xy = [x + vx * dt, y + vy * dt]

    def bounce(self, axis):
        vx, vy = self._v_xy
        if axis == 'x':
            self._v_xy = [-vx, vy]
        elif axis == 'y':
            self._v_xy = [vx, -vy]
        else:
            raise ValueError(f'axis must be x or y, not {axis}')
    def hit_wall(self):
        x, y = self._xy
        vx, vy = self._v_xy
        w, h = self._wh
        return x - w/2 <= 0 or x + w/2 >= 100 # TODO: change to SCREEN_WIDTH
    @property
    def vx(self):
        return self._v_xy[0]
    @vx.setter
    def vx(self, value):
        self._v_xy[0] = value
    @property
    def vy(self):
        return self._v_xy[1]
    @vy.setter
    def vy(self, value):
        self._v_xy[1] = value

if __name__=="__main__":
    # testing MovingObject:
    brick = MovingObject((100, 200), (50, 20), (255, 0, 0), "normal", (1, 2))
    print(f'brick.get_xy() = {brick.get_xy()}')
    print(f'brick.get_wh() = {brick.get_wh()}')
    print(f'brick.get_type() = {brick.get_type()}')
    print(f'brick.get_v_xy() = {brick.get_v_xy()}')
    brick.move(dt=0.1)
    print(f'brick.get_xy() = {brick.get_xy()}')
    brick.bounce(axis='x')
    print(f'brick.get_v_xy() = {brick.get_v_xy()}')
    print(f'brick.hit_wall() = {brick.hit_wall()}')
    brick.move(dt=100)
    print(f'brick.get_xy() = {brick.get_xy()}')
    print(f'brick.hit_wall() = {brick.hit_wall()}')
    brick.bounce(axis='y')
    print(f'brick.get_v_xy() = {brick.get_v_xy()}')
