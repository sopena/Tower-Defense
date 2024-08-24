import pyxel as px
from math import sqrt

class Tower:
    def __init__(self, x, y, raio, color):
        self.x = x
        self.y = y
        self.raio = raio
        self.color = color
        self.color_raio = 13
    
    def desenha_tower(self):
        px.circ(self.x, self.y, self.raio, self.color)
        px.circb(self.x, self.y, self.raio*8, self.color_raio)
        self.color_raio = 13

    def colisao(self):
        self.color_raio = 8

    def detectar_colisao(self, inimigo):
        distancia = sqrt((self.x - inimigo.x)**2 + (self.y - inimigo.y)**2)
        if distancia <= self.raio*8 + inimigo.raio:
            return True
        else:
            return False