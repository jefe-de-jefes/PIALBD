from utils import pedir_int, cleaner

def menu_principal()->int:
    cleaner()
    print('BIENVENIDO AL MENU PRINCIPAL DE INTERACCION CON ALFA')
    print('1.-Nueva venta')
    print('2.-Dar de alta cliente')
    print('3.-Modificar cliente')
    print('4.-Actualizar stock')
    print('5.-Dar de alta proveedor')
    print('6.-Modificar proveedor')
    print('7.-Reportes')
    print('8.-Salir')
    return pedir_int('Seleccione la opción deseada: ', 1, 8)

def menu_reportes()->int:
    cleaner()
    print('BIENVENIDO AL MENU DE REPORTES')
    print('1.-Reporte de ventas')
    print('2.-Reporte de clientes')
    print('3.-Reporte de inventario')
    print('4.-Reporte de proveedores')
    print('5.-Regresar al menu principal')
    return pedir_int('Seleccione la opción deseada: ', 1, 5)

def menu_actualizar()->int:
    cleaner()
    print('Seleccione apartado del cliente a modificar:')
    print('1.-Nombre')
    print('2.-Correo')
    print('3.-Edad')
    print('4.-Sexo')
    print('5.-Salir')
    return pedir_int('Introduzca la opción deseada: ', 1, 5)

def menu_actualizar_produ()->int:
    cleaner()
    print('Seleccione apartado del producto a modificar:')
    print('1.-Nombre del producto')
    print('2.-Stock')
    print('3.-Precio')
    print('4.-Salir')
    return pedir_int('Introduzca la opción deseada: ', 1, 4)

def menu_actualizar_proveedor()->int:
    cleaner()
    print("""Seleccione el apartado del proveedor a modificar:
          1.-Telefono
          2.-Nombre
          3.-Salir""")
    return pedir_int("Introduzca la opción deseada: ", 1, 3)

