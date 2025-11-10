import sys
from mysql.connector import errors
from utils import *
from menus import menu_actualizar, menu_actualizar_produ, menu_actualizar_proveedor

class Cliente:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor
        
    def insertar_cliente(self):
        try:
            cleaner()
            while True:
                print('**NUEVO CLIENTE**')
                nombre = pedir_str_no_vacio('Introduzca el nombre del cliente: ')
                email = pedir_correo('Introduzca el correo electronico: ')
                edad = pedir_int('Introduzca su edad: ', 18, 75)
                sexo = pedir_sexo()

                print(f'Nombre: {nombre}')
                print(f'Correo: {email}')
                print(f'Edad: {edad}')
                print(f'Sexo: Masculino') if sexo == 'M' else print('Sexo: Femenino')
                option = pedir_int('Para confirmar presione 1. Para cancelar presione 2: ',1,2 )
                if option == 2:
                    print('***Operacion cancelada. ***')
                    return
                
                
                args = (nombre, email, edad, sexo, 0)
                
                result_args = self.cursor.callproc('sp_insertar_cliente', args)
                
                self.conn.commit()

                new_client_id = result_args[4]

                print(f'*** Cliente #{new_client_id} registrado con exito. ***')
                
                
                input()
                return
        except errors.DatabaseError as e:
            print(f"\n¡ERROR AL REGISTRAR CLIENTE!")
            print(f"Base de datos dice: {e.msg}")
            self.conn.rollback()
        except Exception as e:
            print(f'Error inesperado al insertar cliente: {e}')
            self.conn.rollback()
        finally:
            input('Presione cualquier tecla para volver al menu principal.')

    def actualizar_cliente(self, id_client):
        try:
            cleaner()
            print(f'** ACTUALIZAR CLIENTE #{id_client} **')

            sql_client = ('SELECT * FROM clientes WHERE id_cliente = %s')
            self.cursor.execute(sql_client, (id_client,))
            datos = self.cursor.fetchone()

            if not datos:
                print(f"Error: No se encontró ningún cliente con el ID {id_client}.")
                input('Presione enter para volver al menú principal...')
                return

            if self.validar_cliente(datos) == 2:
                input('Presione enter para volver al menu principal...')
                return

            cleaner()
            option = menu_actualizar()
            

            
            if option == 5:
                print('Cancelando modificación...')
                input('Presione enter para volver al menú principal...')
                return


            if option == 1:
                new_dato = pedir_str_no_vacio('Introduzca el nuevo nombre: ')
                args = (id_client, new_dato)
                self.cursor.callproc('sp_actualizar_cliente_nombre', args)
                
            elif option == 2:
                new_dato = pedir_correo('Introduzca el nuevo correo: ')
                args = (id_client, new_dato) 
                self.cursor.callproc('sp_actualizar_cliente_email', args)
                
            elif option == 3:
                new_dato = pedir_int('Introduce la nueva edad del cliente: ', 1, 75)
                args = (id_client, new_dato)
                self.cursor.callproc('sp_actualizar_cliente_edad', args)
                
            elif option == 4:
                new_dato = pedir_sexo()
                args = (id_client, new_dato)
                self.cursor.callproc('sp_actualizar_cliente_sexo', args)

            print('** Verificación de datos actualizados **')

            print('** Verificación de datos actualizados **')
            sql_client = ('SELECT * FROM clientes WHERE id_cliente = %s')
            self.cursor.execute(sql_client, (id_client,))
            datos_nuevos = self.cursor.fetchone()
            
            if self.validar_cliente(datos_nuevos) == 2:
                print('Deshaciendo último movimiento...')
                self.conn.rollback()
                input('Ultimo movimiento cancelado exitosamente...')
                return
            
            self.conn.commit()
            print(f'*** Usuario #{id_client} actualizado con exito. ***')
            input()
            return
            
        except errors.IntegrityError as e:
            print(f'Error: {e}')
            self.conn.rollback()
        except errors.DatabaseError as e:
            print(f'Error en la base de datos: {e}')
            self.conn.rollback()
        except Exception as e:
            print(f'Error inesperado al actualizar el cliente: {e}')
            self.conn.rollback()
        finally:
            input('Presione cualquier tecla para volver al menú principal.')

    def validar_cliente(self, datos)->int:
        try:
            print('Datos del cliente:')
            print(f'{"Id_Cliente":<15} {"Nombre":<15} {"Correo":<25} {"Edad":<10} {"Total_pedidos":<15} {"Sexo":<10}')
            print(f'{str(datos[0]):<15} | {str(datos[1]):<15} | {str(datos[2]):<25} | {str(datos[3]):<10} | {str(datos[4]):<15} | {str(datos[5]):<10}')
            print()

            option = pedir_int('Para confirmar presione 1. Para cancelar presione 2: ', 1, 2)
            if option == 2:
                print('*** Operación cancelada. ***')
            return option
        except Exception as e:
            print(f'Error en validar_cliente.: {e}')
            return 2

    def reporte_clientes(self):
        try:
            cleaner()
            print('*** REPORTE DE CLIENTES ACTIVOS ***')
            
            self.cursor.callproc('sp_reporte_clientes')
            datos = []
            headers = []

            for result in self.cursor.stored_results():
                headers = [desc[0] for desc in result.description] 
                datos = result.fetchall()


            if not datos:
                print("No hay clientes registrados.")
                return

            print(" | ".join(f"{h:<20}" for h in headers))
            print("-" * (len(headers) * 23))

            for row in datos:
                row_list = list(row)
                
                if row_list[6] is not None:
                    row_list[6] = f"${row_list[6]:.2f}"
                else:
                    row_list[6] = "$0.00"
                        
                print(" | ".join(f"{str(col):<20}" for col in row_list))

        except Exception as e:
            print('Error inesperado: ', e)
        finally:
            input("\nPresione cualquier tecla para volver al menú...")
            
class Ventas:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def new_venta(self):
        try:
            cleaner()
            print('** NUEVA VENTA **')
            
            id_client = pedir_int('Introduzca el Id del cliente: ', 1, sys.maxsize)

            sql_client = 'SELECT nombre, sexo FROM clientes WHERE id_cliente = %s'
            self.cursor.execute(sql_client, (id_client,))
            datos_client = self.cursor.fetchone()
            
            if not datos_client:
                print(f"Error: Cliente con ID {id_client} no encontrado.")
                input('Presione cualquier tecla para volver al menu principal.')
                return
            
            print(f'Bienvenido {print_client(datos_client)} al sistema.')
            
            id_producto = pedir_int('Introduzca el codigo del producto> ', 1, sys.maxsize)
            
            sql_precio = 'SELECT nombre_producto, stock, precio FROM productos WHERE id_producto = %s'
            self.cursor.execute(sql_precio, (id_producto,))
            datos_articulo = self.cursor.fetchone()

            if not datos_articulo:
                print(f"Error: Artículo con ID {id_producto} no encontrado.")
                input('Presione cualquier tecla para volver al menu principal.')
                return
            
            nombre_articulo, stock_disponible, precio = datos_articulo
            print(f'Producto seleccionado: {nombre_articulo} (Precio sin IVA: ${precio:.2f})')
            
            if stock_disponible == 0:
                print(f"Error: No hay stock disponible para {nombre_articulo}.")
                input('Presione cualquier tecla para volver al menu principal.')
                return

            cantidad:int = pedir_int(f'Introduzca el total de piezas (Disponibles: {stock_disponible}): ', 1, stock_disponible)
            
            sql_total = "SELECT fn_calcular_total_con_iva(%s, %s)"
            self.cursor.execute(sql_total, (precio, cantidad))
            total_real_con_iva = self.cursor.fetchone()[0]

            print(f'Seria un total de ${total_real_con_iva:.2f} (IVA incluido), ¿confirma la compra? [1.-Si / 2.-No]')
            agree = pedir_int('> ', 1, 2)
            if agree == 2:
                print('*** Venta Cancelada ***')
                input('Presione cualquier tecla para volver...')
                return

            print('Procesando venta...')
            
            args = [id_client, id_producto, cantidad, 0]
            
            result_args = self.cursor.callproc('sp_crear_venta', args)
            
            self.conn.commit()
            new_sale_id = result_args[3]

            print(f'*** VENTA #{new_sale_id} REALIZADA CON EXITO ***')
            print(f'Se compraron {cantidad} ud. de {nombre_articulo} por un total de ${total_real_con_iva:.2f}.')
        except errors.DatabaseError as e:
            print(f"\n¡ERROR AL PROCESAR LA VENTA!")
            print(f"Base de Datos dice: {e.msg}")
            
        except Exception as e:
            print(f'Error inesperado en Python: {e}')
            
        finally:
            input('Presione cualquier tecla para volver al menu principal.')
        
        
    def reporte_ventas_cliente_fecha(self):
        try:
            cleaner()
            print('*** REPORTE DE VENTAS POR CLIENTE Y FECHA ***')
            
            email = pedir_int("Ingrese el id del cliente: ", 1, sys.maxsize)
            fecha_inicio = pedir_fecha("Ingrese la fecha de inicio (YYYY-MM-DD): ")

            self.cursor.callproc('sp_consultar_ventas_cliente_fecha', [email, fecha_inicio])

            for result in self.cursor.stored_results():
                datos = result.fetchall()

                if not datos:
                    print("\nNo se encontraron ventas para ese cliente y fecha.")
                    return

                headers = ["ID Venta", "Producto", "Total Artículos", "Total Venta", "Fecha Venta"]
                print(" | ".join(f"{h:<20}" for h in headers))
                print("-" * (len(headers) * 22))

                for row in datos:
                    row_list = list(row)
                    row_list[3] = f"${row_list[3]:.2f}"
                    if row_list[4]:
                        row_list[4] = row_list[4].strftime('%Y-%m-%d %H:%M')
                    print(" | ".join(f"{str(col):<20}" for col in row_list))

        except Exception as e:
            print(f"\nError al generar reporte filtrado: {e}")
        finally:
            input("\nPresione cualquier tecla para volver al menú...")

    def reporte_ventas(self):
        try:
            cleaner()
            print('*** REPORTE DE VENTAS ***')

            if pedir_confirmacion("¿Desea filtrar por cliente y fecha?: "):
                self.reporte_ventas_cliente_fecha()
                return
            
            self.cursor.callproc('sp_reporte_ventas_general')
            
            datos = []
            headers = []

            for result in self.cursor.stored_results():
                headers = [desc[0] for desc in result.description] 
                datos = result.fetchall()
            

            if not datos:
                print("No hay ventas por el momento.")
                return
            
            print(" | ".join(f"{h:<20}" for h in headers))
            print("-" * (len(headers) * 22))

            for row in datos:
                row_list = list(row)
                row_list[4] = f"${row_list[4]:.2f}"
                if row_list[5]:
                    row_list[5] = row_list[5].strftime('%Y-%m-%d %H:%M')
                
                print(" | ".join(f"{str(col):<20}" for col in row_list))

        except Exception as e:
            print(f'Error inesperado al generar reporte: {e}')
        finally:
            input("\nPresione cualquier tecla para volver al menú...")

class Inventario:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def actualizar_stock(self, id_produ):
            try:
                cleaner()
                while True:
                    print(f'** ACTUALIZAR PRODUCTO #{id_produ} **')

                    sql_produ = ('SELECT * FROM productos WHERE id_producto = %s')
                    self.cursor.execute(sql_produ, (id_produ,))
                    datos_produ = self.cursor.fetchone()
                    
                    if not datos_produ:
                        print(f"Error: No se encontro producto con ID {id_produ}")
                        input('Presione enter para volver al menu principal...')
                        return

                    if self.validar_produ(datos_produ) == 2:
                        input('Presione enter para volver al menu principal...')
                        return

                    cleaner()
                    option = menu_actualizar_produ()

                    if option == 4:
                        print('Cancelando modificacion...')
                        input('Presione enter para volver al menu principal...')
                        return
                    

                    if option == 1:
                        new_dato = pedir_str_no_vacio('Introduzca el nuevo nombre: ')
                        self.cursor.callproc('sp_actualizar_producto_nombre', (id_produ, new_dato))
                    elif option == 2:
                        new_dato = pedir_int('Introduzca la nueva cantidad en inventario: ', 0, sys.maxsize)
                        self.cursor.callproc('sp_actualizar_producto_stock', (id_produ, new_dato))
                    elif option == 3:
                        new_dato = pedir_float('Introduce el nuevo precio del producto: ', 0.01, float('inf'))
                        self.cursor.callproc('sp_actualizar_producto_precio', (id_produ, new_dato))

                    print('** Verificación de Datos actualizados **')
                    sql_produ = ('SELECT * FROM productos WHERE id_producto = %s')
                    self.cursor.execute(sql_produ, (id_produ,))
                    datos_nuevos = self.cursor.fetchone()
                    
                    if self.validar_produ(datos_nuevos) == 2:
                        print('Deshaciendo ultimo movimiento...')
                        self.conn.rollback() # Correcto: Python maneja el rollback
                        input('Ultimo movimiento eliminado exitosamente...')
                        return
                    
                    self.conn.commit() # Correcto: Python maneja el commit
                    print(f'*** Producto #{id_produ} actualizado con exito. ***')
                    input()
                    return
            except errors.IntegrityError as e:
                print(f'Error: {e}')
                self.conn.rollback()
            except errors.DatabaseError as e:
                print(f'Error en la base de datos: {e}')
                self.conn.rollback()
            except Exception as e:
                print(f'Error inesperado al actualizar producto: {e}')
                self.conn.rollback()
            finally:
                input('Presione cualquier tecla para volver al menu principal.')

    def validar_produ(self, datos)->int:
        try:
            print('Datos del producto:')
            print(f'{"Id_Articulo":<15} {"Nombre":<20} {"Stock":<10} {"Precio":<15}')
            
            precio_formateado = f"${datos[3]:.2f}"
            print(f'{str(datos[0]):<15} | {str(datos[1]):<20} | {str(datos[2]):<10} | {precio_formateado:<15}')
            print()

            option = pedir_int('Para confirmar producto a modificar presione 1. Para cancelar presione 2: ', 1, 2)
            if option == 2:
                print('*** Operacion cancelada. ***')
            return option
        except Exception as e:
            print(f'Error en validar_produ.: {e}')
            return 2

    def reporte_stock(self):
        try:
            cleaner()
            print('*** REPORTE DE INVENTARIO ***')
            
            self.cursor.callproc('sp_reporte_stock')
            datos = []
            for result in self.cursor.stored_results():
                datos = result.fetchall()

            if not datos:
                print("No hay inventario.")
                return

            headers = [desc[0] for desc in self.cursor.description]
            print(" | ".join(f"{h:<20}" for h in headers))
            print("-" * (len(headers) * 23))

            for row in datos:
                print(" | ".join(f"{str(col):<20}" for col in row))

        except Exception as e:
            print('Error inesperado: ', e)
        finally:
            input("\nPresione cualquier tecla para volver al menú...")

class Proveedores:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor
        
    def insertar_proveedor(self):
        try:
            cleaner()
            while True:
                print("** NUEVO PROVEEDOR ***")
                telefono_proveedor = pedir_telefono("Introduzca el telefono del proveedor: ")
                nombre_proveedor = pedir_str_no_vacio("Introduzca el nombre del proveedor: ")
                print(f'Telefono: {telefono_proveedor}')
                print(f'Nombre: {nombre_proveedor}')
                option = pedir_int('Para confirmar presione 1. Para cancelar presione 2: ',1,2 )
                if option == 2:
                    print('*** Operacion cancelada. ***')
                    return
                
                args = (telefono_proveedor, nombre_proveedor, 0)
                result_args = self.cursor.callproc('sp_insertar_proveedor', args)
                self.conn.commit()
                new_id = result_args[2]
                
                print(f'*** Proveedor #{new_id} registrado con exito. ***')

                input()
                return
        except errors.DatabaseError as e: 
            print(f"\n¡ERROR AL REGISTRAR PROVEEDOR!")
            print(f"Base de Datos dice: {e.msg}")
            self.conn.rollback()
        except Exception as e:
            print(f'Error inesperado al insertar proveedor: {e}')
            self.conn.rollback()
        finally:
            input('Presione cualquier tecla para volver al menu principal.')
 
    
    def actualizar_proveedor(self, id_proveedor):
        try:
            cleaner()
            print(f"** ACTUALIZAR PROVEEDOR #{id_proveedor} **")   
            
            sql_proveedor = ('SELECT * FROM proveedores WHERE id_proveedor = %s')
            self.cursor.execute(sql_proveedor, (id_proveedor,))
            datos = self.cursor.fetchone()
            
            if not datos:
                print(f"Error: No se encontró ningún proveedor con el ID {id_proveedor}.")
                input('Presione enter para volver al menú principal...')
                return
            
            if self.validar_proveedor(datos) == 2:
                input('Presione enter para volver al menu principal...')
                return
            
            cleaner()
            option = menu_actualizar_proveedor()
            
            if option == 3:
                print("Cancelando modificación...")
                input("Presione enter para volver al menú principal...")
                return
            
            if option == 1:
                new_dato = pedir_telefono("Introduzca el nuevo telefono: ")
                self.cursor.callproc('sp_actualizar_proveedor_telefono', (id_proveedor, new_dato))
            elif option == 2: 
                new_dato = pedir_str_no_vacio("Introduzca el nuevo nombre: ")
                self.cursor.callproc('sp_actualizar_proveedor_nombre', (id_proveedor, new_dato))
                
            print("** Verificación de datos actualizados **")
            sql_proveedor = ('SELECT * FROM proveedores WHERE id_proveedor = %s')
            self.cursor.execute(sql_proveedor, (id_proveedor,))
            datos_nuevos = self.cursor.fetchone()
            
            if self.validar_proveedor(datos_nuevos) == 2: 
                print("Deshaciendo último movimiento...")
                self.conn.rollback()
                input("Ultimo movimiento cancelado exitosamente...")
                return
            
            self.conn.commit()
            print(f"*** Proveedor #{id_proveedor} actualizado con exito. ***")
            input()
            return
        
        except errors.IntegrityError as e:
            print(f"Error: {e}")
            self.conn.rollback()
        except errors.DatabaseError as e:
            print(f"Error en la base de datos: {e}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error inesperado al actualizar el proveedor: {e}")
            self.conn.rollback()
        finally:
            input("Presione cualquier tecla para vovler al menú principal.")
        
    def validar_proveedor(self, datos) -> int:
        try:
            print("Datos del proveedor")
            print(f"{"Id_Proveedor":<15} {"Telefono":<15} {"Nombre":<15}")
            print(f"{str(datos[0]):<15} | {str(datos[1]):15} | {str(datos[2]):<15}")
            print()
            
            option = pedir_int("Para confirmar presione 1. Para cancelar presione 2: ", 1, 2)
            if option == 2:
                print("***Operación cancelada. ***")
            return option
        except Exception as e:
            print(f"Error en validar_cliente.: {e}")
            return 2
        
    def reporte_proveedores(self):
        try:
            cleaner()
            print("*** REPORTE DE PROVEEDORES ACTIVOS ***")
            
            self.cursor.callproc('sp_reporte_proveedores')
            datos = []
            for result in self.cursor.stored_results():
                datos = result.fetchall()
            
            if not datos:
                print("No hay proveedores registrados.")
                return

            headers = [desc[0] for desc in self.cursor.description]
            print(" | ".join(f"{h:<20}" for h in headers))
            print("-" * (len(headers) * 23))
            
            for row in datos:
                print(" | ".join(f"{str(col):<20}" for col in row))
                
        except Exception as e:
            print("Error inesperado: ", e)
        finally:
            input("\nPresione cualquier tecla para volver al menú...")