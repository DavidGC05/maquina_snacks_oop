from snack import Snack
from snacks import Snacks


# Lista de productos (vacia)
productos = []
# Imprimimos nuestra lista
print('**** Maquina de Snacks ****')
print('Snacks Disponibles:')
snacks = Snacks()
print(snacks)

# Creamos una funcion principal
def maquina_snacks(snacks, productos):
    salir = False
    while not salir:
        print(f'''Menu:
        1. Comprar Snack
        2. Mostrar Ticket
        3. Agregar Snack
        4. Salir''')
        opcion = int(input('Escoge una Opcion: '))
        if opcion == 1:
            comprar_producto(snacks, productos)
        elif opcion == 2:
            mostrar_ticket(productos)
        elif opcion == 3:
            agregar_snack(snacks)
        elif opcion == 4:
            print('Regrese pronto...')
            salir = True
        else:
            print('Opcion invalida, Selecciona otra opcion...')

def comprar_producto(snacks, productos):
    id_snack = int(input('Que snack quieres (id)?: '))
    # productos.append(snacks[id_snack])
    # print(f'Ok, snack agregado: {snacks[id_snack]}')

    # Recorrer la lista de snacks
    snack_encontrado = None
    for snack in snacks.lista_snacks:
        if id_snack == snack.id_snack:
            snack_encontrado = snack
            break
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'El id del snack es incorrecto: {id_snack}')

def mostrar_ticket(productos):
    ticket = f'\t*** Ticket de Venta ***'
    total = 0
    for producto in productos:
        ticket += f"\n\t - {producto.nombre} - ${producto.precio}"
        total += producto.precio
    ticket += f'\n\tTotal = ${total}'
    print(ticket)
def agregar_snack(snacks):
    nombre = input('Proporciona el nombre del nuevo snack: ')
    precio = int(input('Proporciona el precio del nuevo snack: '))
    nuevo_snack = Snack(nombre, precio)
    snacks.agregar_snack(nuevo_snack)
    print(f'Nuevo snack {nuevo_snack} se ha agregado correctamente!')
    print(snacks)

# LLamamos a la funcion de maquina_snacks
maquina_snacks(snacks, productos)