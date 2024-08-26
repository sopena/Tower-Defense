import pyxel as px
import constants
import utils
from math import sqrt


class Tower:
    def __init__(self, x, y, raio, color):
        self.x = x
        self.y = y
        self.raio = raio
        self.color = color
        self.color_raio = 13
        self.monstros_dentro = []

    def update_tower(self):
        self.monster_dentro()
        self.draw_tower()
        print(self.monstros_dentro)
        self.monstros_dentro.clear()

    def draw_tower(self):
        px.circ(self.x, self.y, self.raio, self.color)
        px.circb(self.x, self.y, self.raio*8, self.color_raio)
        self.color_raio = 13

    def monster_dentro(self):
        for j in range(len(constants.monsters)):
            if  utils.detectar_colisao(self, constants.monsters[j]):
                self.color_raio = 8
                if not(constants.monsters[j] in self.monstros_dentro):
                    self.monstros_dentro.append(constants.monsters[j])
        
                