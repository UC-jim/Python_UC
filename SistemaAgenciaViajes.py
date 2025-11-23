# ============================================
# SISTEMA DE GESTIÓN PARA AGENCIA DE VIAJES
# ============================================

clientes = {}
tours = {}
reservas = {}
pagos = {}

# =======================
# MÓDULO: CLIENTES
# =======================

def agregar_cliente():
    print("\n--- Registrar Cliente ---")
    cid = input("ID del cliente: ").strip()

    # Validación: evitar duplicados
    if cid in clientes:
        print("ERROR: Ese ID ya existe.")
        return
    
    nombre = input("Nombre completo: ")
    dni = input("DNI: ")
    correo = input("Correo: ")

    # Guardar datos del cliente
    clientes[cid] = {
        "nombre": nombre,
        "dni": dni,
        "correo": correo
    }
    print("Cliente registrado con éxito.")


def buscar_cliente():
    print("\n--- Buscar Cliente ---")
    cid = input("ID del cliente: ")
    
    # Verificación de existencia
    if cid in clientes:
        print(clientes[cid])
    else:
        print("No existe el cliente.")


def actualizar_cliente():
    print("\n--- Actualizar Cliente ---")
    cid = input("ID del cliente: ")

    if cid not in clientes:
        print("No existe ese cliente.")
        return

    print("Deje el campo vacío si no desea modificarlo.")
    nombre = input("Nuevo nombre: ")
    correo = input("Nuevo correo: ")

    # Solo actualizar campos llenos
    if nombre.strip():
        clientes[cid]["nombre"] = nombre
    if correo.strip():
        clientes[cid]["correo"] = correo

    print("Cliente actualizado.")


def eliminar_cliente():
    print("\n--- Eliminar Cliente ---")
    cid = input("ID del cliente: ")

    # Eliminar si existe
    if cid in clientes:
        del clientes[cid]
        print("Cliente eliminado.")
    else:
        print("No existe el cliente.")


def listar_clientes():
    print("\n--- Lista de Clientes ---")

    if not clientes:
        print("No hay clientes registrados.")
        return
    
    # Mostrar todos los clientes
    for cid, data in clientes.items():
        print(f"{cid}: {data['nombre']} | DNI: {data['dni']} | Correo: {data['correo']}")


# =======================
# MÓDULO: TOURS
# =======================

def agregar_tour():
    print("\n--- Registrar Tour ---")
    tid = input("ID del tour: ")

    if tid in tours:
        print("Ese tour ya existe.")
        return

    nombre = input("Nombre del tour: ")
    precio = float(input("Precio: "))

    # Guardar tour
    tours[tid] = {"nombre": nombre, "precio": precio}
    print("Tour agregado.")


def buscar_tour():
    print("\n--- Buscar Tour ---")
    tid = input("ID del tour: ")

    if tid in tours:
        print(tours[tid])
    else:
        print("No existe el tour.")


def actualizar_tour():
    print("\n--- Actualizar Tour ---")
    tid = input("ID del tour: ")

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


def eliminar_tour():
    print("\n--- Eliminar Tour ---")
    tid = input("ID del tour: ")

    if tid in tours:
        del tours[tid]
        print("Tour eliminado.")
    else:
        print("No existe el tour.")


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

def crear_reserva():
    print("\n--- Crear Reserva ---")
    rid = input("ID de la reserva: ")

    if rid in reservas:
        print("Ese ID ya existe.")
        return

    cid = input("ID del cliente: ")
    tid = input("ID del tour: ")

    # Validaciones
    if cid not in clientes:
        print("No existe el cliente.")
        return

    if tid not in tours:
        print("No existe el tour.")
        return

    reservas[rid] = {"cliente": cid, "tour": tid, "estado": "Pendiente"}
    print("Reserva creada correctamente.")


def cambiar_estado_reserva():
    print("\n--- Cambiar Estado de Reserva ---")
    rid = input("ID de la reserva: ")

    if rid not in reservas:
        print("No existe esa reserva.")
        return

    print("1) Pagado  2) Cancelado")
    op = input("Nuevo estado: ")

    if op == "1":
        reservas[rid]["estado"] = "Pagado"
    elif op == "2":
        reservas[rid]["estado"] = "Cancelado"
    else:
        print("Opción inválida.")
        return

    print("Estado actualizado.")


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

    pagos[pid] = {"reserva": rid, "monto": monto, "metodo": metodo}

    # Actualizar estado de reserva
    reservas[rid]["estado"] = "Pagado"

    print("Pago registrado.")


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

menu_principal()

