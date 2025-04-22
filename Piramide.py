import pygame

class Piramide:
    def __init__(self, num_piedras):
        self.num_piedras = num_piedras
        self.dp = {}

    def mover_piedras(self, num_piedras, origen, destino, auxiliar):
        if num_piedras == 0:
            return []
        if (num_piedras, origen, destino) in self.dp:
            return self.dp[(num_piedras, origen, destino)]

        movimientos = []
        movimientos += self.mover_piedras(num_piedras - 1, origen, auxiliar, destino)
        movimientos.append((origen, destino))
        movimientos += self.mover_piedras(num_piedras - 1, auxiliar, destino, origen)

        self.dp[(num_piedras, origen, destino)] = movimientos
        return movimientos

    def resolver(self):
        movimientos = self.mover_piedras(self.num_piedras, "Origen", "Destino", "Auxiliar")
        return movimientos

def dibujar_piramide(pantalla, columnas, ancho_piedra, alto_piedra):
    pantalla.fill((255, 255, 255))
    ancho_pantalla = pantalla.get_width()
    alto_pantalla = pantalla.get_height()
    espacio_columna = ancho_pantalla // 3

    for i, columna in enumerate(columnas):
        x_centro = espacio_columna * (i + 0.5)
        pygame.draw.rect(pantalla, (0, 0, 0), (x_centro - 5, alto_pantalla // 2, 10, alto_pantalla // 2))
        for j, piedra in enumerate(reversed(columna.piedras)):
            ancho = ancho_piedra * piedra.tamaño
            x = x_centro - ancho // 2
            y = alto_pantalla - (j + 1) * alto_piedra
            pygame.draw.rect(pantalla, (100, 100, 255), (x, y, ancho, alto_piedra))

    pygame.display.flip()
