import pygame
import sys
from Piramide import Piramide
from Columna import Columna
from Piedra import Piedra
from Piramide import dibujar_piramide
def main():
    try:
        num_piedras = int(input("Ingrese el número de piedras en la pirámide: "))
        if num_piedras <= 0:
            raise ValueError("El número de piedras debe ser mayor que cero.")
        
        piramide = Piramide(num_piedras)
        movimientos = piramide.resolver()

        # Inicializar columnas
        columnas = [Columna("Origen"), Columna("Auxiliar"), Columna("Destino")]
        for tamaño in range(num_piedras, 0, -1):
            columnas[0].apilar(Piedra(tamaño))

        # Inicializar pygame
        pygame.init()
        ancho_pantalla = 800
        alto_pantalla = 600
        pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
        pygame.display.set_caption("Torre de Hanoi")
        ancho_piedra = ancho_pantalla // (2 * num_piedras)
        alto_piedra = 20

        dibujar_piramide(pantalla, columnas, ancho_piedra, alto_piedra)

        # Ejecutar movimientos
        for origen, destino in movimientos:
            pygame.time.delay(500)
            piedra = columnas[{"Origen": 0, "Auxiliar": 1, "Destino": 2}[origen]].desapilar()
            columnas[{"Origen": 0, "Auxiliar": 1, "Destino": 2}[destino]].apilar(piedra)
            dibujar_piramide(pantalla, columnas, ancho_piedra, alto_piedra)

        # Esperar a que el usuario cierre la ventana
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    except ValueError as e:
        print(f"Error: {e}")
