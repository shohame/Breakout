
import numpy as np


def d2r(degrees):
    return degrees * np.pi / 180


def r2d(radians):
    return radians * 180 / np.pi


def cosd(degrees):
    return np.cos(d2r(degrees))


def sind(degrees):
    return np.sin(d2r(degrees))


def tand(degrees):
    return np.tan(d2r(degrees))


def atan2d(x, y):
    return r2d(np.arctan2(y,x))


# All angles are in degrees:
def polar_to_cartesian(a, angle):
    x = a * cosd(angle)
    y = a * sind(angle)
    return x, y


def cartesian_to_polar(x, y):
    a = np.sqrt(x**2 + y**2)
    angle = atan2d(x, y)
    return a, angle


