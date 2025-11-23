# ============================================
# SISTEMA DE GESTIÓN PARA AGENCIA DE VIAJES
# ============================================

# Diccionarios para almacenar la información de clientes, tours, reservas y pagos.
clientes = {}
tours = {}
reservas = {}
pagos = {}

# =======================
# MÓDULO: CLIENTES
# =======================

# Función para agregar un nuevo cliente
def agregar_cliente():
    print("\n--- Registrar Cliente ---")
    cid = input("ID del cliente: ").strip()  # Solicitar ID del cliente

    # Validación para evitar duplicados en los IDs de clientes
    if cid in clientes:
        print("ERROR: Ese ID ya existe.")
        return
    
    # Solicitar el nombre, DNI y correo del cliente
    nombre = input("Nombre completo: ")
    dni = input("DNI: ")
    correo = input("Correo: ")

    # Almacenar los datos del cliente en el diccionario 'clientes'
    clientes[cid] = {
        "nombre": nombre,
        "dni": dni,
        "correo": correo
    }
    print("Cliente registrado con éxito.")

# Función para buscar un cliente por su ID
def buscar_cliente():
    print("\n--- Buscar Cliente ---")
    cid = input("ID del cliente: ")  # Solicitar ID

    # Verificar si el cliente existe en la base de datos
    if cid in clientes:
        print(clientes[cid])  # Mostrar los datos del cliente
    else:
        print("No existe el cliente.")

# Función para actualizar los datos de un cliente
def actualizar_cliente():
    print("\n--- Actualizar Cliente ---")
    cid = input("ID del cliente: ")  # Solicitar ID

    if cid not in clientes:
        print("No existe ese cliente.")
        return

    print("Deje el campo vacío si no desea modificarlo.")
    nombre = input("Nuevo nombre: ")
    correo = input("Nuevo correo: ")

    # Solo actualizar los campos que no estén vacíos
    if nombre.strip():
        clientes[cid]["nombre"] = nombre
    if correo.strip():
        clientes[cid]["correo"] = correo

    print("Cliente actualizado.")

# Función para eliminar un cliente de la base de datos
def eliminar_cliente():
    print("\n--- Eliminar Cliente ---")
    cid = input("ID del cliente: ")

    # Eliminar al cliente si existe
    if cid in clientes:
        del clientes[cid]
        print("Cliente eliminado.")
    else:
        print("No existe el cliente.")

# Función para listar todos los clientes registrados
def listar_clientes():
    print("\n--- Lista de Clientes ---")

    if not clientes:
        print("No hay clientes registrados.")
        return
    
    # Mostrar los datos de cada cliente
    for cid, data in clientes.items():
        print(f"{cid}: {data['nombre']} | DNI: {data['dni']} | Correo: {data['correo']}")

# =======================
# MÓDULO: TOURS
# =======================

# Función para agregar un nuevo tour
def agregar_tour():
    print("\n--- Registrar Tour ---")
    tid = input("ID del tour: ")  # Solicitar ID del tour

    if tid in tours:
        print("Ese tour ya existe.")
        return

    nombre = input("Nombre del tour: ")
    precio = float(input("Precio: "))  # Solicitar precio del tour

    # Almacenar el tour en el diccionario 'tours'
    tours[tid] = {"nombre": nombre, "precio": precio}
    print("Tour agregado.")

# Función para buscar un tour por su ID
def buscar_tour():
    print("\n--- Buscar Tour ---")
    tid = input("ID del tour: ")  # Solicitar ID

    if tid in tours:
        print(tours[tid])  # Mostrar los datos del tour
    else:
        print("No existe el tour.")

# Función para actualizar los detalles de un tour
def actualizar_tour():
    print("\n--- Actualizar Tour ---")
    tid = input("ID del tour: ")  # Solicitar ID

    if tid not in tours:
        print("Ese tour no existe.")
        return

    print("Deje el campo vacío si no desea modificarlo.")
    nombre = input("Nuevo nombre: ")
    precio = input("Nuevo precio: ")

    if nombre.strip():
        tours[tid]["nombre"] = nombre
    if precio.strip():
        tours[tid]["precio"] = float(precio)

    print("Tour actualizado.")

# Función para eliminar un tour
def eliminar_tour():
    print("\n--- Eliminar Tour ---")
    tid = input("ID del tour: ")  # Solicitar ID

    if tid in tours:
        del tours[tid]  # Eliminar el tour del diccionario
        print("Tour eliminado.")
    else:
        print("No existe el tour.")

# Función para listar todos los tours registrados
def listar_tours():
    print("\n--- Lista de Tours ---")

    if not tours:
        print("No hay tours registrados.")
        return
    
    for tid, data in tours.items():
        print(f"{tid}: {data['nombre']} | Precio: {data['precio']}")

# =======================
# MÓDULO: RESERVAS
# =======================

# Función para crear una nueva reserva
def crear_reserva():
    print("\n--- Crear Reserva ---")
    rid = input("ID de la reserva: ")

    if rid in reservas:
        print("Ese ID ya existe.")
        return

    cid = input("ID del cliente: ")
    tid = input("ID del tour: ")

    # Validaciones: comprobar si el cliente y el tour existen
    if cid not in clientes:
        print("No existe el cliente.")
        return

    if tid not in tours:
        print("No existe el tour.")
        return

    reservas[rid] = {"cliente": cid, "tour": tid, "estado": "Pendiente"}  # Crear la reserva
    print("Reserva creada correctamente.")

# Función para cambiar el estado de una reserva (Pagado o Cancelado)
def cambiar_estado_reserva():
    print("\n--- Cambiar Estado de Reserva ---")
    rid = input("ID de la reserva: ")

    if rid not in reservas:
        print("No existe esa reserva.")
        return

    print("1) Pagado  2) Cancelado")
    op = input("Nuevo estado: ")

    # Actualizar el estado de la reserva según la opción elegida
    if op == "1":
        reservas[rid]["estado"] = "Pagado"
    elif op == "2":
        reservas[rid]["estado"] = "Cancelado"
    else:
        print("Opción inválida.")
        return

    print("Estado actualizado.")

# Función para listar todas las reservas
def listar_reservas():
    print("\n--- Lista de Reservas ---")

    if not reservas:
        print("No hay reservas.")
        return
    
    for rid, data in reservas.items():
        print(f"{rid}: Cliente {data['cliente']} | Tour {data['tour']} | Estado: {data['estado']}")

# =======================
# MÓDULO: PAGOS
# =======================

# Función para registrar un pago
def registrar_pago():
    print("\n--- Registrar Pago ---")
    pid = input("ID del pago: ")

    if pid in pagos:
        print("Ese ID ya existe.")
        return

    rid = input("ID de la reserva: ")

    if rid not in reservas:
        print("Esa reserva no existe.")
        return

    monto = float(input("Monto: "))
    metodo = input("Método de pago: ")

    pagos[pid] = {"reserva": rid, "monto": monto, "metodo": metodo}  # Registrar el pago

    # Cambiar el estado de la reserva a "Pagado"
    reservas[rid]["estado"] = "Pagado"

    print("Pago registrado.")

# Función para listar todos los pagos
def listar_pagos():
    print("\n--- Lista de Pagos ---")

    if not pagos:
        print("No hay pagos registrados.")
        return
    
    for pid, data in pagos.items():
        print(f"{pid}: Reserva {data['reserva']} | Monto: {data['monto']} | Método: {data['metodo']}")

# =======================
# MENÚS
# =======================
# Funciones que muestran menús y permiten al usuario interactuar con el sistema.

# Menú para gestionar clientes
def menu_clientes():
    while True:
        print("\n--- MENÚ CLIENTES ---")
        print("1) Agregar\n2) Buscar\n3) Actualizar\n4) Eliminar\n5) Listar\n0) Volver")
        op = input("Opción: ")

        if op == "1": agregar_cliente()
        elif op == "2": buscar_cliente()
        elif op == "3": actualizar_cliente()
        elif op == "4": eliminar_cliente()
        elif op == "5": listar_clientes()
        elif op == "0": break
        else: print("Opción inválida.")

# Menú para gestionar tours
def menu_tours():
    while True:
        print("\n--- MENÚ TOURS ---")
        print("1) Ag
