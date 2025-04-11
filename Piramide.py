from Columna import Columna
from Piedra import Piedra

class Piramide:
    def __init__(self, num_piedras):
        self.columna_origen = Columna("Origen")
        self.columna_auxiliar = Columna("Auxiliar")
        self.columna_destino = Columna("Destino")
        for tamaño in range(num_piedras, 0, -1):
            self.columna_origen.apilar(Piedra(tamaño))

    def mover_piedras(self, num_piedras, origen, destino, auxiliar):
        if num_piedras == 1:
            piedra = origen.desapilar()
            destino.apilar(piedra)
            print(f"Mover {piedra} de {origen.nombre} a {destino.nombre}")
        else:
            self.mover_piedras(num_piedras - 1, origen, auxiliar, destino)
            self.mover_piedras(1, origen, destino, auxiliar)
            self.mover_piedras(num_piedras - 1, auxiliar, destino, origen)