from utils import pedir_int, cleaner

def menu_principal()->int:
    cleaner()
    print('BIENVENIDO AL MENU PRINCIPAL DE INTERACCION CON ALFA')
    print('1. Ventas')
    print('2. Clientes')
    print('3. Inventario')
    print('4. Proveedores')
    print('5. Reportes')
    print('0. Salir')
    return pedir_int('Seleccione la opción deseada: ', 0, 5)

def menu_ventas()->int:
    cleaner()
    print('** GESTIÓN DE VENTAS **')
    print('1. Registrar Nueva Venta')
    print('0. Volver al Menú Principal')
    return pedir_int('Seleccione una opción: ', 0, 1)

def menu_clientes()->int:
    cleaner()
    print('** GESTIÓN DE CLIENTES **')
    print('1. Dar de alta cliente')
    print('2. Modificar cliente')
    print('3. Eliminar cliente')
    print('0. Volver al Menú Principal')
    return pedir_int('Seleccione una opción: ', 0, 3)

def menu_productos()->int:
    cleaner()
    print('** GESTIÓN DE INVENTARIO **')
    print('1. Modificar producto')
    print('2. Crear producto')
    print('3. Eliminar producto')
    print('0. Volver al menú principal')
    return pedir_int('Seleccione una opción: ', 0, 3)

def menu_proveedores()->int:
    cleaner()
    print('** GESTIÓN DE PROVEEDORES **')
    print('1. Dar de alta proveedor')
    print('2. Modificar proveedor')
    print('3. Eliminar proveedor')
    print('0. Volver al menú principal')
    return pedir_int('Seleccione una opción: ', 0, 3)

def menu_reportes()->int:
    cleaner()
    print('BIENVENIDO AL MENU DE REPORTES')
    print('1.-Reporte de ventas')
    print('2.-Reporte de clientes')
    print('3.-Reporte de inventario')
    print('4.-Reporte de proveedores')
    print('0.-Regresar al menu principal')
    return pedir_int('Seleccione la opción deseada: ', 0, 4)

def menu_actualizar()->int:
    cleaner()
    print('Seleccione apartado del cliente a modificar:')
    print('1.-Nombre')
    print('2.-Correo')
    print('3.-Edad')
    print('4.-Sexo')
    print('0.-Salir')
    return pedir_int('Introduzca la opción deseada: ', 0, 4)

def menu_actualizar_produ()->int:
    cleaner()
    print('Seleccione apartado del producto a modificar:')
    print('1.-Nombre del producto')
    print('2.-Stock')
    print('3.-Precio')
    print('4.-Proveedor')
    print('0.-Salir')
    return pedir_int('Introduzca la opción deseada: ', 0, 4)

def menu_actualizar_proveedor()->int:
    cleaner()
    print("""Seleccione el apartado del proveedor a modificar:
          1.-Telefono
          2.-Nombre
          0.-Salir""")
    return pedir_int("Introduzca la opción deseada: ", 0, 2)