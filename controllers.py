from menus import menu_principal, menu_ventas, menu_clientes, menu_productos, menu_proveedores, menu_reportes

def ejecutar_menu_reportes(venta_service, client_service, stock_service, proveedores_service):
    while True:
        op_reportes = menu_reportes()
        match op_reportes:
            case 1:
                venta_service.reporte_ventas()
            case 2:
                client_service.reporte_clientes()
            case 3:
                stock_service.reporte_stock()
            case 4:
                proveedores_service.reporte_proveedores()
            case 0:
                print('Regresando al menú principal...')
                break
            case _:
                print('Opción no válida, intente de nuevo.')

def ejecutar_menu_ventas(venta_service):
    while True:
        op = menu_ventas()
        if op == 1:
            venta_service.new_venta()
        elif op == 0:
            print('Regresando al menú principal...')
            break

def ejecutar_menu_clientes(client_service):
    while True:
        op = menu_clientes()
        if op == 1:
            client_service.insertar_cliente()
        elif op == 2:
            client_service.actualizar_cliente()
        elif op == 3:
            client_service.eliminar_cliente()
        elif op == 0:
            print('Regresando al menú principal...')
            break

def ejecutar_menu_productos(stock_service):
    while True:
        op = menu_productos()
        if op == 1:
            stock_service.actualizar_stock()
        elif op == 2:
            stock_service.crear_producto()
        elif op == 3:
            stock_service.eliminar_producto()
        elif op == 0:
            print('Regresando al menú principal...')
            break

def ejecutar_menu_proveedores(proveedores_service):
    while True:
        op = menu_proveedores()
        if op == 1:
            proveedores_service.insertar_proveedor()
        elif op == 2:
            proveedores_service.actualizar_proveedor()
        elif op == 3:
            proveedores_service.eliminar_proveedor()
        elif op == 0:
            print('Regresando al menú principal...')
            break