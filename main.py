import mysql.connector
from mysql.connector import errors
import sys

from menus import menu_principal, menu_reportes
from services import Cliente, Ventas, Inventario, Proveedores
from utils import pedir_int, pedir_str_no_vacio, pedir_password, cleaner
def main():
    conn = None
    cursor = None
    try:
        cleaner()
        print('=== BIENVENIDO A LA GESTION DE LA TIENDA ALFA ===')
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


        venta_service = Ventas(conn, cursor)
        client_service = Cliente(conn, cursor)
        stock_service = Inventario(conn, cursor)
        proveedores_service = Proveedores(conn, cursor)

        option_menu:int = 0

        while(option_menu != 8):
            option_menu = menu_principal()
            
            if option_menu == 1:
                venta_service.new_venta()
                
            elif option_menu == 2:
                client_service.insertar_cliente()
                
            elif option_menu == 3:
                client_id = pedir_int('Introduce el id del cliente: ', 1, sys.maxsize)
                client_service.actualizar_cliente(client_id)
                
            elif option_menu == 4:
                produ_id = pedir_int('Introduce el id del producto: ', 1, sys.maxsize)
                stock_service.actualizar_stock(produ_id)
                
            elif option_menu == 5:
                proveedores_service.insertar_proveedor()
            
            elif option_menu == 6:
                proveedor_id = pedir_int("Introduce el id del proveedor: ", 1, sys.maxsize)
                proveedores_service.actualizar_proveedor(proveedor_id)
                
            elif option_menu == 7:
                op_reportes = menu_reportes()
                if op_reportes == 1:
                    venta_service.reporte_ventas()
                elif op_reportes == 2:
                    client_service.reporte_clientes()
                elif op_reportes == 3:
                    stock_service.reporte_stock()
                elif op_reportes == 4:
                    proveedores_service.reporte_proveedores()
                elif op_reportes == 5:
                    print('Regresando al menu principal...')
                    
            elif option_menu == 8:
                print('Vuelva pronto.')
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

    except Exception as e:
        print(f'Error general inesperado: {e}')

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
