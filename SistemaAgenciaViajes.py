# ============================================
# SISTEMA DE GESTIÓN PARA AGENCIA DE VIAJES
# ============================================

# Diccionarios que almacenan los datos de clientes, tours, reservas y pagos.
# Estos diccionarios mantienen la información mientras se ejecuta el sistema.
clientes = {}
tours = {}
reservas = {}
pagos = {}

# =======================
# MÓDULO: CLIENTES
# =======================

# Función para agregar un cliente al sistema.
# Se ingresan datos como nombre, DNI y correo, y se guarda en el diccionario 'clientes'
def agregar_cliente():
    print("\n--- Registrar Cliente ---")
    cid = input("ID del cliente: ").strip()

    # Validación para evitar duplicados: si el ID ya existe, no permite agregarlo.
    if cid in clientes:
        print("ERROR: Ese ID ya existe.")
        return
    
    # Solicitar los datos del cliente
    nombre = input("Nombre completo: ")
    dni = input("DNI: ")
    correo = input("Correo: ")

    # Guardar los datos del cliente en el diccionario 'clientes' usando el ID como clave
    clientes[cid] = {
        "nombre": nombre,
        "dni": dni,
        "correo": correo
    }
    print("Cliente registrado con éxito.")

# Función para buscar un cliente por su ID.
def buscar_cliente():
    print("\n--- Buscar Cliente ---")
    cid = input("ID del cliente: ")
    
    # Verificación de existencia: si el cliente no está en el diccionario, muestra un mensaje.
    if cid in clientes:
        print(clientes[cid])
    else:
        print("No existe el cliente.")

# Función para actualizar los datos de un cliente existente.
def actualizar_cliente():
    print("\n--- Actualizar Cliente ---")
    cid = input("ID del cliente: ")

    # Verificar si el cliente existe
    if cid not in clientes:
        print("No existe ese cliente.")
        return

    print("Deje el campo vacío si no desea modificarlo.")
    nombre = input("Nuevo nombre: ")
    correo = input("Nuevo correo: ")

    # Solo actualizar campos llenos (si el usuario no dejó el campo vacío)
    if nombre.strip():
        clientes[cid]["nombre"] = nombre
    if correo.strip():
        clientes[cid]["correo"] = correo

    print("Cliente actualizado.")

# Función para eliminar un cliente.
def eliminar_cliente():
    print("\n--- Eliminar Cliente ---")
    cid = input("ID del cliente: ")

    # Eliminar el cliente si existe
    if cid in clientes:
        del clientes[cid]
        print("Cliente eliminado.")
    else:
        print("No existe el cliente.")

# Función para listar todos los clientes registrados.
def listar_clientes():
    print("\n--- Lista de Clientes ---")

    # Si no hay clientes registrados, se muestra un mensaje.
    if not clientes:
        print("No hay clientes registrados.")
        return
    
    # Mostrar todos los clientes registrados con su ID, nombre, DNI y correo
    for cid, data in clientes.items():
        print(f"{cid}: {data['nombre']} | DNI: {data['dni']} | Correo: {data['correo']}")

# =======================
# MÓDULO: TOURS
# =======================

# Función para agregar un nuevo tour.
def agregar_tour():
    print("\n--- Registrar Tour ---")
    tid = input("ID del tour: ")

    # Validación: verificar si el ID del tour ya existe
    if tid in tours:
        print("Ese tour ya existe.")
        return

    # Solicitar nombre y precio del tour
    nombre = input("Nombre del tour: ")
    precio = float(input("Precio: "))

    # Guardar el tour en el diccionario 'tours' usando el ID como clave
    tours[tid] = {"nombre": nombre, "precio": precio}
    print("Tour agregado.")

# Función para buscar un tour por su ID.
def buscar_tour():
    print("\n--- Buscar Tour ---")
    tid = input("ID del tour: ")

    # Verificación de existencia del tour
    if tid in tours:
        print(tours[tid])
    else:
        print("No existe el tour.")

# Función para actualizar los detalles de un tour.
def actualizar_tour():
    print("\n--- Actualizar Tour ---")
    tid = input("ID del tour: ")

    # Verificar si el tour existe
    if tid not in tours:
        print("Ese tour no existe.")
        return

    print("Deje el campo vacío si no desea modificarlo.")
    nombre = input("Nuevo nombre: ")
    precio = input("Nuevo precio: ")

    # Actualizar solo si los campos no están vacíos
    if nombre.strip():
        tours[tid]["nombre"] = nombre
    if precio.strip():
        tours[tid]["precio"] = float(precio)

    print("Tour actualizado.")

# Función para eliminar un tour del sistema.
def eliminar_tour():
    print("\n--- Eliminar Tour ---")
    tid = input("ID del tour: ")

    # Eliminar si el tour existe
    if tid in tours:
        del tours[tid]
        print("Tour eliminado.")
    else:
        print("No existe el tour.")

# Función para listar todos los tours registrados.
def listar_tours():
    print("\n--- Lista de Tours ---")

    # Si no hay tours registrados, se muestra un mensaje.
    if not tours:
        print("No hay tours registrados.")
        return
    
    # Mostrar todos los tours registrados con su ID, nombre y precio
    for tid, data in tours.items():
        print(f"{tid}: {data['nombre']} | Precio: {data['precio']}")

# =======================
# MÓDULO: RESERVAS
# =======================

# Función para crear una nueva reserva.
def crear_reserva():
    print("\n--- Crear Reserva ---")
    rid = input("ID de la reserva: ")

    # Validación: evitar ID de reserva duplicado
    if rid in reservas:
        print("Ese ID ya existe.")
        return

    # Solicitar ID de cliente y tour
    cid = input("ID del cliente: ")
    tid = input("ID del tour: ")

    # Validaciones: verificar que el cliente y el tour existan en sus respectivos diccionarios
    if cid not in clientes:
        print("No existe el cliente.")
        return

    if tid not in tours:
        print("No existe el tour.")
        return

    # Registrar la reserva con estado 'Pendiente'
    reservas[rid] = {"cliente": cid, "tour": tid, "estado": "Pendiente"}
    print("Reserva creada correctamente.")

# Función para cambiar el estado de una reserva.
def cambiar_estado_reserva():
    print("\n--- Cambiar Estado de Reserva ---")
    rid = input("ID de la reserva: ")

    # Verificar si la reserva existe
    if rid not in reservas:
        print("No existe esa reserva.")
        return

    print("1) Pagado  2) Cancelado")
    op = input("Nuevo estado: ")

    # Cambiar el estado según la opción seleccionada
    if op == "1":
        reservas[rid]["estado"] = "Pagado"
    elif op == "2":
        reservas[rid]["estado"] = "Cancelado"
    else:
        print("Opción inválida.")
        return

    print("Estado actualizado.")

# Función para listar todas las reservas.
def listar_reservas():
    print("\n--- Lista de Reservas ---")

    # Si no hay reservas registradas, se muestra un mensaje.
    if not reservas:
        print("No hay reservas.")
        return
    
    # Mostrar todas las reservas registradas con el ID de cliente, ID de tour y estado
    for rid, data in reservas.items():
        print(f"{rid}: Cliente {data['cliente']} | Tour {data['tour']} | Estado: {data['estado']}")

# =======================
# MÓDULO: PAGOS
# =======================

# Función para registrar un pago realizado.
def registrar_pago():
    print("\n--- Registrar Pago ---")
    pid = input("ID del pago: ")

    # Verificar si el ID de pago ya existe
    if pid in pagos:
        print("Ese ID ya existe.")
        return

    # Solicitar el ID de la reserva y el monto del pago
    rid = input("ID de la reserva: ")

    # Verificar si la reserva existe
    if rid not in reservas:
        print("Esa reserva no existe.")
        return

    monto = float(input("Monto: "))
    metodo = input("Método de pago: ")

    # Registrar el pago
    pagos[pid] = {"reserva": rid, "monto": monto, "metodo": metodo}

    # Actualizar el estado de la reserva a "Pagado"
    reservas[rid]["estado"] = "Pagado"

    print("Pago registrado.")

# Función para listar todos los pagos realizados.
def listar_pagos():
    print("\n--- Lista de Pagos ---")

    # Si no hay pagos registrados, se muestra un mensaje.
    if not pagos:
        print("No hay pagos registrados.")
        return
    
    # Mostrar todos los pagos realizados, con la reserva relacionada, monto y método de pago
    for pid, data in pagos.items():
        print(f"{pid}: Reserva {data['reserva']} | Monto: {data['monto']} | Método: {data['metodo']}")

# =======================
# MENÚS
# =======================

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
        print("1) Agregar\n2) Buscar\n3) Actualizar\n4) Eliminar\n5) Listar\n0) Volver")
        op = input("Opción: ")

        if op == "1": agregar_tour()
        elif op == "2": buscar_tour()
        elif op == "3": actualizar_tour()
        elif op == "4": eliminar_tour()
        elif op == "5": listar_tours()
        elif op == "0": break
        else: print("Opción inválida.")

# Menú para gestionar reservas
def menu_reservas():
    while True:
        print("\n--- MENÚ RESERVAS ---")
        print("1) Crear reserva\n2) Cambiar estado\n3) Listar\n0) Volver")
        op = input("Opción: ")

        if op == "1": crear_reserva()
        elif op == "2": cambiar_estado_reserva()
        elif op == "3": listar_reservas()
        elif op == "0": break
        else: print("Opción inválida.")

# Menú para gestionar pagos
def menu_pagos():
    while True:
        print("\n--- MENÚ PAGOS ---")
        print("1) Registrar pago\n2) Listar pagos\n0) Volver")
        op = input("Opción: ")

        if op == "1": registrar_pago()
        elif op == "2": listar_pagos()
        elif op == "0": break
        else: print("Opción inválida.")

# =======================
# MENÚ PRINCIPAL
# =======================

# Menú principal que muestra todas las opciones de módulos
def menu_principal():
    while True:
        print("\n======= SISTEMA DE AGENCIA DE VIAJES =======")
        print("1) Clientes\n2) Tours\n3) Reservas\n4) Pagos\n0) Salir")
        op = input("Opción: ")

        if op == "1": menu_clientes()
        elif op == "2": menu_tours()
        elif op == "3": menu_reservas()
        elif op == "4": menu_pagos()
        elif op == "0": break
        else:
            print("Opción inválida.")

# Iniciar el menú principal
menu_principal()
