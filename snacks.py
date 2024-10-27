from snack import Snack


class Snacks:
    # lista de snacks agregadas como objetos de Snack
    lista_snacks = [
        Snack('Papas', 70),
        Snack('Refresco', 50),
        Snack('Sandwich', 120)
    ]

    def agregar_snack(self, snack):
        Snacks.lista_snacks.append(snack)

    def __str__(self):
        snacks_str = ''
        for snack in Snacks.lista_snacks:
            snacks_str += '\n' + snack.__str__()


        return f'''*** Snacks en el inventario ***
        {snacks_str}'''

