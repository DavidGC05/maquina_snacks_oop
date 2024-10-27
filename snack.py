class Snack:
    contador_snack = 0
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Snack.contador_snack += 1
        self.id_snack = Snack.contador_snack

    def __str__(self):
        return f'Id: {self.id_snack}, Nombre: {self.nombre}  Precio: ${self.precio}'