


class Vector():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __init__(self, vector):
        self._x = vector._x
        self._y = vector._y

    def __init__(self, xy): # xy is a tuple (x, y)
        self._x = xy[0]
        self._y = xy[1]

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def get_xy(self):
        return self._x, self._y

    def set_xy(self, xy):
        self._x, self._y = xy

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, number):
        return Vector(self._x * number, self._y * number)

    def __rmul__(self, number):
        return Vector(self._x * number, self._y * number)

    def __sub__(self, other):
        return Vector(self._x - other._x, self._y - other._y)

    def __truediv__(self, number):
        return Vector(self._x / number, self._y / number)

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def __abs__(self):
        return Vector(abs(self._x), abs(self._y))

    def __neg__(self):
        return Vector(-self._x, -self._y)

    def __getitem__(self, index):
        if index == 0:
            return self._x
        elif index == 1:
            return self._y

    def __setitem__(self, index, value):
        if index == 0:
            self._x = value
        elif index == 1:
            self._y = value

    def __len__(self):
        return 2
    def copy(self):
        return Vector(self._x, self._y)


if __name__=="__main__":
    v1 = Vector(-1, 2)
    v2 = Vector(3, 4)
    v3 = v1.copy()
    v3.set_x(10)
    print(f'v1 = {v1}')
    print(f'v2 = {v2}')
    print(f'v3 = {v3}')
    print(f'v1 + v2 = {v1 + v2}')
    print(f'v1 * 2 = {v1 * 2}')
    print(f'2 * v1 = {2 * v1}')
    print(f'v1 - v2 = {v1 - v2}')
    print(f'v1 / 2 = {v1 / 2}')
    print(f'v1 == v2 = {v1 == v2}')
    print(f'abs(v1) = {abs(v1)}')
    print(f'-v1 = {-v1}')
    print(f'v1[0] = {v1[0]}')
    v1[0] = 100
    print(f'v1 = {v1}')
    print(f'len(v1) = {len(v1)}')
    print(f'v1[0] = {v1[0]}')
    print(f'v1[1] = {v1[1]}')
    print(f'v1[2] = {v1[2]}')
    v1[2] = 10
    print(f'v1 = {v1}')
