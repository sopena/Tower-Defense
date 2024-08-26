import pyxel as px
import constants
import utils
from math import sqrt

class Tiro:
    def __init__(self, x, y, raio, color, vel_tiro):
        self.x = x
        self.y = y
        self.raio = raio
        self.color = color
        self.vel_tiro = vel_tiro
        self.acertou = False

    def update_tiro(self):
        if self.acertou == False:
            pass
                

    def draw_tiro(self):
        px.circ(self.x, self.y, self.raio, self.color)
