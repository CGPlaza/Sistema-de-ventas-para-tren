#main.py
#Sistema de Ventas EFE Trenes de Chile
#Integracion menu + validaciones

from modelos.cliente import Cliente
from modelos.sistema_ventas import SistemaVentas

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Funciones de validacion (aportadas por integrante 3)
def validar_rut(rut: str) -> bool:
    """Valida RUT de forma basica: no vacio y al menos 8 caracteres."""
    return isinstance(rut, str) and len(rut.strip()) >= 8

def validar_email(email: str) -> bool:
    """Valida correo de forma basica: debe contener '@' y '.'."""
    return isinstance(email, str) and "@" in email and "." in email

def validar_entero_positivo(valor_str: str):
    """Convierte string a entero si es > 0, en caso contrario retorna None."""
    try:
        val = int(valor_str)
        return val if val > 0 else None
    except:
        return None

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Menu del sistema
def mostrar_menu():
    print("\n                            GRUPO")
    print("                             EFE")
    print("             *** MENU DE OPCIONES ***")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("[1] -> Venta de boletos por categoria")
    print("[2] -> Devolucion de boletos")
    print("[3] -> Consulta de boletos")
    print("[4] -> Totalizacion de ventas por categoria")
    print("[5] -> % de ventas por categoria y Cierre de Caja")
    print("[6] -> Salir del sistema")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Cuerpo principal
def main():
    sistema = SistemaVentas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            # === Venta de boletos ===
            print("\n   Venta de Boleto   ")
            nombre = input("Nombre del cliente: ")
            apellido = input("Apellido del cliente: ")
            rut = input("RUT del cliente: ")
            correo = input("Correo del cliente: ")

            # Validaciones 
            if not validar_rut(rut):
                print("Error: RUT invalido (debe tener al menos 8 caracteres).")
                continue
            if not validar_email(correo):
                print("Error: Correo invalido (debe contener '@' y '.').")
                continue

            print("Categorias disponibles: Primera, Segunda, Economica")
            categoria = input("Seleccione categoria: ").capitalize()
            if categoria not in ["Primera", "Segunda", "Economica"]:
                print("Error: Categoria invalida.")
                continue

            cantidad_str = input("Cantidad de boletos a comprar: ")
            cantidad = validar_entero_positivo(cantidad_str)
            if cantidad is None:
                print("Error: La cantidad debe ser un numero entero positivo.")
                continue

            cliente = Cliente(nombre, apellido, rut, correo)
            boletos = sistema.vender(cliente, categoria, cantidad)

            if boletos:
                for b in boletos:
                    print(f"Boleto vendido con ID: {b.id}")
            else:
                print("Error: No quedan asientos disponibles.")

        elif opcion == "2":
            # Devolucion de boletos
            print("\n   Devolucion de Boleto   ")
            id_boleto = input("Ingrese ID del boleto a devolver: ")
            # Se elimina la conversion a entero porque los IDs son strings (UUID)
            
            exito = sistema.devolver(id_boleto)
            if exito:
                print("Devolucion realizada con éxito.")
            else:
                print("Error: No se encontro el boleto.")

        elif opcion == "3":
            # Consulta de boletos 
            print("\n--- Consulta de Boletos ---")
            sistema.consultar_boletos()

        elif opcion == "4":
            # Totalizacion de ventas
            print("\n--- Totalizacion de Ventas por Categoria ---")
            sistema.totalizar_ventas()

        elif opcion == "5":
            # Porcentaje de ventas y cierre de caja
            print("\n--- % de Ventas y Cierre de Caja ---")
            sistema.porcentaje_ventas()
            sistema.cierre_caja()

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("Error: opcion invalida. Intente nuevamente.")

if __name__ == "__main__":
    main()
