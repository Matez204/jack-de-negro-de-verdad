from cartas import *
class Juego:
    def __init__(self):
        self.mazo = Mazo()
        self.casa = Mazo(True)
        self.jug = Mazo(True)
    def ini(self):
        for i in range(2):
            self.casa.agregar_carta(self.mazo.dar_carta())
            self.jug.agregar_carta(self.mazo.dar_carta())
    def mostrar_juego(self):
        print("jugador: ")
        self.jug.mostrar_cartas()
        print("casa: ")
        self.casa.mostrar_cartas()