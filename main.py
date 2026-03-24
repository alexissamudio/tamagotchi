"""
Punto de entrada del juego Tamagotchi.
Configura la consola en UTF-8 para soportar caracteres especiales en Windows
y arranca el juego instanciando Game.
"""

import sys
from game import Game

sys.stdout.reconfigure(encoding='utf-8')

if __name__ == "__main__":
    juego = Game()
    juego.iniciar()
