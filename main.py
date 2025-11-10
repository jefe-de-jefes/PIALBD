import mysql.connector
from mysql.connector import errors
from controllers import ejecutar_menu_clientes, ejecutar_menu_proveedores, ejecutar_menu_productos, ejecutar_menu_ventas, ejecutar_menu_reportes
import sys

from menus import menu_principal
from services import Cliente, Ventas, Inventario, Proveedores
from utils import pedir_str_no_vacio, pedir_password, cleaner
def main():
    conn = None
    cursor = None
    while True:
        try:
            cleaner()
            print('*** BIENVENIDO A LA GESTION DE LA TIENDA ALFA ***')
            print('Por favor, inicie sesión son su usuario root de la base de datos para continuar.')
            user = pedir_str_no_vacio('Introduzca su usuario> ')
            password = pedir_password('Introduzca la contraseña> ')
            
            conn = mysql.connector.connect(
                host='localhost',
                port=3306,
                user=user,
                password=password,
                database='ALFA'
            )

            if conn.is_connected():
                print('Conectado a la BD')
                cursor = conn.cursor()
                cursor.execute("SELECT DATABASE();")
                record = cursor.fetchone()
                print(f"Conectado a: {record[0]}")
                input("Presione Enter para continuar...")
                break

        except errors.Error as e:
            if e.errno == 1044:
                print(f"Error: Acceso denegado para el usuario '{user}'@'localhost' a la base de datos 'ALFA'.")
            elif e.errno == 1045:
                print(f"Error: Acceso denegado. Revise su usuario ('{user}') y contraseña.")
            elif e.errno == 2003:
                print("Error: No se pudo conectar al servidor de MySQL. ¿Está encendido?")
            else:
                print(f'Error de base de datos inesperado: {e}')
            
            print("\nPor favor, intente de nuevo.")
            input("Presione Enter para continuar...")
        except Exception as e:
            print(f'Error general inesperado durante el login: {e}')
            print("\nPor favor, intente de nuevo.")
            input("Presione Enter para continuar...")

    try:
        venta_service = Ventas(conn, cursor)
        client_service = Cliente(conn, cursor)
        stock_service = Inventario(conn, cursor)
        proveedores_service = Proveedores(conn, cursor)

        option_menu = -1

        while option_menu != 0:
            option_menu = menu_principal()

            match option_menu:
                case 1:
                    ejecutar_menu_ventas(venta_service)
                case 2:
                    ejecutar_menu_clientes(client_service)
                case 3:
                    ejecutar_menu_productos(stock_service)
                case 4:
                    ejecutar_menu_proveedores(proveedores_service)
                case 5:
                    ejecutar_menu_reportes(venta_service, client_service, stock_service, proveedores_service)
                case 0:
                    print('Vuelva pronto.')
                    break
                case _:
                    print('Opción no válida, intente de nuevo.')

    except Exception as e:
        print(f'\n¡Ha ocurrido un error inesperado durante la ejecución!')
        print(f'Error: {e}')

    finally:
        if cursor is not None:
            cursor.close()
            print("\nCursor cerrado.")
        if conn is not None and conn.is_connected():
            conn.close()
            print("Conexión a la BD cerrada.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error fatal en la aplicación: {e}')
