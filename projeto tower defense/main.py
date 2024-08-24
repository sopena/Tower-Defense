import pyxel as px
from monster import Monster
from tower import Tower

# game informations
width = 400
height = 400
tam_monster = 8

tempo = 0
tempo_spaw = 2

route = [[50, 0], [50, 200], [140, 200], [140, 150], [250, 150], [250, 350], [350, 350], [350, 360], [390, 360]]

max_monsters_fase1 = 20

monsters = []
lista_torres = []

fps = 30

class App:
    def __init__(self, tempo,tempo_spaw, fps):
        self.tempo = tempo
        self.tempo_spaw = tempo_spaw
        self.fps = fps
        px.init(width, height, title="Tower Defense", fps = self.fps, quit_key=px.KEY_Q)
        px.run(self.update, self.draw)
    

    def update(self):
        px.mouse(visible=True)
        
        if px.btn(px.MOUSE_BUTTON_LEFT):
            lista_torres.append(Tower(px.mouse_x, px.mouse_y, 8, 3))

        self.spaw_monsters()
        self.tempo += 1

        for i in range(len(monsters)):
             monsters[i].move_monster(route)

        
           
    def draw(self):
        px.cls(0)

        self.desenha_hud()
        
        for i in range(len(lista_torres)):
            lista_torres[i].desenha_tower()

        for i in range(len(lista_torres)):
            for j in range(len(monsters)):
                colidiu = lista_torres[i].detectar_colisao(monsters[j])
                if colidiu:
                    lista_torres[i].colisao()
                    
        for i in range(len(monsters)):
             monsters[i].draw_monster()
    
    def spaw_monsters(self):
        if len(monsters) < max_monsters_fase1:
            if (self.tempo % (self.fps * self.tempo_spaw)) == 0:
                monsters.append(Monster(0, 0, 100, 1, 10, tam_monster))
            self.diminui_tempo()

    def diminui_tempo(self):
        if (self.tempo_spaw > 0.2): 
            if ((self.tempo % ((self.fps * self.tempo_spaw)*1)) == 0):
                self.tempo_spaw = round((self.tempo_spaw - 0.1),2)
        
    
    def desenha_hud(self):
        px.rectb(0, 370, 400, 30, 11)

        for i in range(7):
            px.line(40*(i+1), 370, 40*(i+1), 400, 11)
    


App(tempo, tempo_spaw, fps)