#  SISTEMA DE RESERVAS TURÍSTICAS

# Diccionarios de clientes
clientes = {}    # id y nombres

# CRUD CLIENTES
def agregar_actualizar_cliente():
    cliente_id = input("ID Cliente: ").strip()
    nombre = input("Nombre del cliente: ").strip()
    clientes[cliente_id] = nombre
    print("OK →", cliente_id, "=", clientes[cliente_id])

def buscar_cliente():
    cliente_id = input("ID Cliente a buscar: ").strip()
    if cliente_id in clientes:
        print(cliente_id, "→", clientes[cliente_id])
    else:
        print("No existe")

def eliminar_cliente():
    cliente_id = input("ID Cliente a eliminar: ").strip()
    if cliente_id in clientes:
        del clientes[cliente_id]
        print("Eliminado")
    else:
        print("No existe")

def listar_clientes():
    if not clientes:
        print("(Sin clientes)")
    else:
        for k, v in clientes.items():
            print("-", k, ":", v)

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

menu_clientes()