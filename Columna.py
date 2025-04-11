class Columna:
    def __init__(self, nombre):
        self.nombre = nombre
        self.piedras = []

    def apilar(self, piedra):
        if self.piedras and self.piedras[-1].tamaño < piedra.tamaño:
            raise ValueError("No se puede colocar una piedra más grande sobre una más pequeña.")
        self.piedras.append(piedra)

    def desapilar(self):
        if not self.piedras:
            raise ValueError("No hay piedras para mover.")
        return self.piedras.pop()

    def __repr__(self):
        return f"{self.nombre}: {self.piedras}"