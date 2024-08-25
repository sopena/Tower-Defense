import pyxel as px
import constants
import utils
from monster import Monster
from tower import Tower
from tiro import Tiro


class App:
    def __init__(self, tempo, tempo_spaw, fps):
        self.tempo = tempo
        self.tempo_spaw = tempo_spaw
        self.fps = fps
        px.init(constants.width, constants.height, title="Tower Defense",
                fps=self.fps, quit_key=px.KEY_Q)
        px.run(self.update, self.draw)

    def update(self):
        px.mouse(visible=True)

        if px.btn(px.MOUSE_BUTTON_LEFT):
            constants.lista_torres.append(Tower(px.mouse_x, px.mouse_y, 8, 3))

        utils.spaw_monsters()
        constants.tempo += 1

        # rodar o update de cada classe
        for i in range(len(constants.monsters)):
            constants.monsters[i].update_monster()

        for i in range(len(constants.lista_torres)):
            constants.lista_torres[i].update_tower()

        for i in range(len(constants.lista_tiros)):
            constants.lista_tiros[i].update_tiro()

    def draw(self):
        px.cls(0)

        # desenha o hud
        utils.desenha_hud()

        # rodar o draw de cada classe
        for i in range(len(constants.lista_torres)):
            constants.lista_torres[i].draw_tower()

        for i in range(len(constants.monsters)):
            constants.monsters[i].draw_monster()


App(constants.tempo, constants.tempo_spaw, constants.fps)
