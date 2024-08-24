import pyxel as px

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

    def draw_monster(self):
        px.circ(self.x, self.y, self.raio, self.color)

    def move_monster(self, route):
        if self.pontoAtual >= len(route):
            return

        self.direcao = [route[self.pontoAtual][0]-self.x,route[self.pontoAtual][1]-self.y]
        if self.direcao[0] == 0:
             self.direcao[0] = 1
        if self.direcao[1] == 0:
             self.direcao[1] = 1

        if self.direcao[0] > 0:
             self.direcao[0] = 1
        if self.direcao[0] < 0:
             self.direcao[0] = -1
        if self.direcao[1] > 0:
             self.direcao[1] = 1
        if self.direcao[1] < 0:
             self.direcao[1] = -1

        if self.x != route[self.pontoAtual][0]:
            self.x += (self.vel * self.direcao[0]) 

        if self.y != route[self.pontoAtual][1]:
            self.y += (self.vel * self.direcao[1]) 
        
        if self.x == route[self.pontoAtual][0] and self.y == route[self.pontoAtual][1]:
                self.pontoAtual += 1

        

            