import pyxel as px
import math
import constants
from monster import Monster


def detectar_colisao(obj1, obj2):
    distancia = math.sqrt((obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2)
    if distancia <= obj1.raio*8 + obj2.raio:
        return obj2
    else:
        return False


def desenha_hud():
    px.rectb(0, 370, 400, 30, 11)

    for i in range(7):
        px.line(40*(i+1), 370, 40*(i+1), 400, 11)


def diminui_tempo():
    if (constants.tempo_spaw > 0.1):
        if ((constants.tempo % ((constants.fps * constants.tempo_spaw)*1)) == 0):
            constants.tempo_spaw = round((constants.tempo_spaw - 0.1), 2)


def spaw_monsters():
    if len(constants.monsters) < constants.max_monsters_fase1:
        if (constants.tempo % (constants.fps * constants.tempo_spaw)) == 0:
            constants.monsters.append(Monster(0, 0, 100, 1, 10, constants.tam_monster))
        diminui_tempo()

def verificar_direcao(direcao):
    if direcao[0] == 0:
        direcao[0] = 1
    if direcao[0] > 0:
        direcao[0] = 1
    if direcao[0] < 0:
        direcao[0] = -1
    if direcao[1] == 0:
        direcao[1] = 1
    if direcao[1] > 0:
        direcao[1] = 1
    if direcao[1] < 0:
        direcao[1] = -1
    return direcao