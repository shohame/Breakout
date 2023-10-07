
import pygame

class GameSync():
    def __init__(self):
        self._time = pygame.time
        self._t_tick = self._time.get_ticks()

    def get_dt(self):
        t = self._time.get_ticks()
        dt = t - self._t_tick
        self._t_tick = t
        return dt/1000