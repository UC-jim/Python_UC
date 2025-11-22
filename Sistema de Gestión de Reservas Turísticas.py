#  SISTEMA DE RESERVAS TURÍSTICAS

# Diccionarios
clientes = {
   "1": {
      "nombre": "Jimmy",
      "dni": "12345678",
      "correo": "jimmy@gmail.com"
   }
}
tours = {
   "1": {
      "nombre": "Tour machupicchu",
      "precio": 120.0
   }
}
# CRUD CLIENTES
def agregar_actualizar_cliente():
    print("\n--- Agregar / Actualizar Cliente ---")
    cliente_id = input("ID del cliente: ").strip()

    nombre = input("Nombre completo: ")
    dni = input("DNI: ")
    correo = input("Correo: ")

    # Si ya existe, actualiza solo lo que ingrese
    if cliente_id in clientes:
        if nombre.strip() != "":
            clientes[cliente_id]["nombre"] = nombre
        if dni.strip() != "":
            clientes[cliente_id]["dni"] = dni
        if correo.strip() != "":
            clientes[cliente_id]["correo"] = correo
        print("Cliente actualizado correctamente.")
    else:
        clientes[cliente_id] = {
            "nombre": nombre,
            "dni": dni,
            "correo": correo
        }
        print("Cliente agregado correctamente.")

def buscar_cliente():
    print("\n--- Buscar Cliente ---")
    cliente_id = input("ID del cliente: ")
    if cliente_id in clientes:
        print(cliente_id, "→", clientes[cliente_id])
    else:
        print("No existe el cliente.")

def eliminar_cliente():
    print("\n--- Eliminar Cliente ---")
    cliente_id = input("ID del cliente: ")
    if cliente_id in clientes:
        del clientes[cliente_id]
        print("Cliente eliminado.")
    else:
        print("No existe el cliente.")

def listar_clientes():
    print("\n--- Lista de Clientes ---")
    if not clientes:
        print("No hay clientes registrados.")
        return
    
    for cliente_id, data in clientes.items():
        print(f"{cliente_id}: {data['nombre']} | DNI: {data['dni']} | Correo: {data['correo']}")

# CRUD TOURS
def agregar_tour():
    print("\n--- Registrar Tour ---")
    tour_id = input("ID del tour: ")
    if tour_id in tours:
        print("Ese tour ya existe.")
        return

    nombre = input("Nombre del tour: ")
    precio = float(input("Precio: "))

    tours[tour_id] = {
        "nombre": nombre,
        "precio": precio
    }
    print("Tour agregado.")

def buscar_tour():
    print("\n--- Buscar Tour ---")
    tour_id = input("ID del tour: ")
    if tour_id in tours:
        print(tours[tour_id])
    else:
        print("No existe el tour.")

def actualizar_tour():
    print("\n--- Actualizar Tour ---")
    tour_id = input("ID del tour: ")

    if tour_id not in tours:
        print("No existe ese tour.")
        return

    print("Deje vacío para no modificar.")
    nombre = input("Nuevo nombre: ")
    precio = input("Nuevo precio: ")

    if nombre.strip() != "":
        tours[tour_id]["nombre"] = nombre
    if precio.strip() != "":
        tours[tour_id]["precio"] = float(precio)

    print("Tour actualizado.")

def eliminar_tour():
    print("\n--- Eliminar Tour ---")
    tour_id = input("ID del tour: ")
    if tour_id in tours:
        del tours[tour_id]
        print("Tour eliminado.")
    else:
        print("No existe el tour.")

def listar_tours():
    print("\n--- Lista de Tours ---")
    if not tours:
        print("No hay tours registrados.")
        return
    
    for tour_id, data in tours.items():
        print(f"{tour_id}: {data['nombre']} | Precio: {data['precio']}")


# SUBMENU CLIENTES.
def menu_clientes():
    while True:
        print("\n--- CLIENTES ---")
        print("1 Agregar/Actualizar  2 Buscar  3 Eliminar  4 Listar  0 Volver")
        op = input("Opción: ").strip()
        
        if op == "1": agregar_actualizar_cliente()
        elif op == "2": buscar_cliente()
        elif op == "3": eliminar_cliente()
        elif op == "4": listar_clientes()
        elif op == "0": break
        else: print("Opción inválida")

# SUBMENU TOUR
def menu_tours():
    while True:
        print("\n--- TOURS ---")
        print("1 Agregar  2 Buscar  3 Actualizar  4 Eliminar  5 Listar  0 Volver")
        op = input("Opción: ").strip()

        if op == "1": agregar_tour()
        elif op == "2": buscar_tour()
        elif op == "3": actualizar_tour()
        elif op == "4": eliminar_tour()
        elif op == "5": listar_tours()
        elif op == "0": break
        else: print("Opción inválida")


# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n=== SISTEMA DE RESERVAS TURÍSTICAS ===")
        print("1 Clientes  2 Tours  3 Reservas  4 Pagos  0 Salir")
        op = input("Opción: ").strip()

        if op == "1": menu_clientes()
        elif op == "2": menu_tours()
        elif op == "3": break
        elif op == "4": break
        elif op == "0": break
        else: print("Opción inválida")

menu()