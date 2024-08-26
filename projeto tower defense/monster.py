import pyxel as px
import constants
import utils
class Monster:
    i = 0
    def __init__(self, x, y, life, vel, color, raio):
        self.x = x
        self.y = y
        self.life = life
        self.vel = vel
        self.pontoAtual = 0
        self.color = color
        self.raio = raio

    def update_monster(self):
        self.move_monster(constants.route)
        self.draw_monster()
        
    def draw_monster(self):
        px.circ(self.x, self.y, self.raio, self.color)

    def move_monster(self, route):
        if self.pontoAtual >= len(route):
            return

        self.direcao = [route[self.pontoAtual][0]-self.x,route[self.pontoAtual][1]-self.y]
        self.direcao = utils.verificar_direcao(self.direcao)

        if self.x != route[self.pontoAtual][0]:
            self.x += (self.vel * self.direcao[0]) 

        if self.y != route[self.pontoAtual][1]:
            self.y += (self.vel * self.direcao[1]) 
        
        if self.x == route[self.pontoAtual][0] and self.y == route[self.pontoAtual][1]:
                self.pontoAtual += 1

        

            