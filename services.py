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
            input('Presione enter para volver al menu principal.')

    def actualizar_cliente(self):
        try:
            cleaner()
            print(f'** ACTUALIZAR CLIENTE **')

            client_id = pedir_int('Introduce el id del cliente: ', 1, sys.maxsize)


            sql_client = ('SELECT * FROM clientes WHERE id_cliente = %s')
            self.cursor.execute(sql_client, (client_id,))
            datos = self.cursor.fetchone()

            if not datos:
                print(f"Error: No se encontró ningún cliente con el ID {client_id}.")
                return

            if not self.validar_cliente(datos):
                return

            cleaner()
            option = menu_actualizar()
            
            if option == 0:
                print('Cancelando modificación...')
                return


            if option == 1:
                new_dato = pedir_str_no_vacio('Introduzca el nuevo nombre: ')
                args = (client_id, new_dato)
                self.cursor.callproc('sp_actualizar_cliente_nombre', args)
                
            elif option == 2:
                new_dato = pedir_correo('Introduzca el nuevo correo: ')
                args = (client_id, new_dato)
                self.cursor.callproc('sp_actualizar_cliente_email', args)
                
            elif option == 3:
                new_dato = pedir_int('Introduce la nueva edad del cliente: ', 1, 75)
                args = (client_id, new_dato)
                self.cursor.callproc('sp_actualizar_cliente_edad', args)
                
            elif option == 4:
                new_dato = pedir_sexo()
                args = (client_id, new_dato)
                self.cursor.callproc('sp_actualizar_cliente_sexo', args)

            print('** Verificación de datos actualizados **')
            sql_client = ('SELECT * FROM clientes WHERE id_cliente = %s')
            self.cursor.execute(sql_client, (client_id,))
            datos_nuevos = self.cursor.fetchone()
            
            if not self.validar_cliente(datos_nuevos):
                print('Deshaciendo último movimiento...')
                self.conn.rollback()
                print('Ultimo movimiento cancelado exitosamente...')
                return
            
            self.conn.commit()
            print(f'*** Usuario #{client_id} actualizado con exito. ***')
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
            input('Presione enter para volver al menú principal.')

    def validar_cliente(self, datos)->bool:
        try:
            print('Datos del cliente:')
            print(f'{"Id_Cliente":<15} {"Nombre":<15} {"Correo":<25} {"Edad":<10} {"Total_pedidos":<15} {"Sexo":<10}')
            print(f'{str(datos[0]):<15} | {str(datos[1]):<15} | {str(datos[2]):<25} | {str(datos[3]):<10} | {str(datos[4]):<15} | {str(datos[5]):<10}')
            print()

            option = pedir_int('estos son los datos correctos? \n(1: Confirmar, 2: Cancelar): ', 1, 2)
            if option == 2:
                print('*** Operación cancelada. ***')
                return False
            return True
        except Exception as e:
            print(f'Error en validar_cliente.: {e}')
            return False

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
            input("\nPresione enter para volver al menú...")
    
    def eliminar_cliente(self):
        try:
            cleaner()
            print(f'** ELIMINAR CLIENTE **')
            client_id = pedir_int('Introduce el id del cliente a eliminar: ', 1, sys.maxsize)

            sql_client = ('SELECT * FROM clientes WHERE id_cliente = %s')
            self.cursor.execute(sql_client, (client_id,))
            datos = self.cursor.fetchone()

            if not datos:
                print(f"Error: No se encontró ningún cliente con el ID {client_id}.")
                input('Presione enter para volver...')
                return

            print('Datos del cliente a eliminar:')
            print(f'{"Id_Cliente":<15} {"Nombre":<15} {"Correo":<25}')
            print(f'{str(datos[0]):<15} | {str(datos[1]):<15} | {str(datos[2]):<25}')
            print()

            if not pedir_confirmacion("¿ESTÁ SEGURO de que desea eliminar a este cliente? "):
                print('*** Operación cancelada. ***')
                return
            
            self.cursor.callproc('sp_eliminar_cliente', (client_id,))
            self.conn.commit()
            
            print(f'*** Cliente #{client_id} eliminado exitosamente. ***')

        except errors.DatabaseError as e:
            print(f'Error en la base de datos: {e.msg}')
            self.conn.rollback()
        except Exception as e:
            print(f'Error inesperado al eliminar cliente: {e}')
            self.conn.rollback()
        finally:
            input('Presione enter para volver al menú...')
            
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
                return
            
            print(f'Bienvenido {print_client(datos_client)} al sistema.')
            id_producto = pedir_int('Introduzca el codigo del producto> ', 1, sys.maxsize)
            
            sql_precio = 'SELECT nombre_producto, stock, precio FROM productos WHERE id_producto = %s'
            self.cursor.execute(sql_precio, (id_producto,))
            datos_articulo = self.cursor.fetchone()

            if not datos_articulo:
                print(f"Error: Artículo con ID {id_producto} no encontrado.")
                return
            
            nombre_articulo, stock_disponible, precio = datos_articulo
            print(f'Producto seleccionado: {nombre_articulo} (Precio sin IVA: ${precio:.2f})')
            
            if stock_disponible == 0:
                print(f"Error: No hay stock disponible para {nombre_articulo}.")
                input('Presione enter para volver al menu principal.')
                return

            cantidad:int = pedir_int(f'Introduzca el total de piezas (Disponibles: {stock_disponible}): ', 1, stock_disponible)
            
            sql_total = "SELECT fn_calcular_total_con_iva(%s, %s)"
            self.cursor.execute(sql_total, (precio, cantidad))
            total_real_con_iva = self.cursor.fetchone()[0]

            print(f'Seria un total de ${total_real_con_iva:.2f} (IVA incluido), ¿confirma la compra? [1.-Si / 2.-No]')
            agree = pedir_int('> ', 1, 2)
            if agree == 2:
                print('*** Venta Cancelada ***')
                input('Presione enter para volver...')
                return

            print('Procesando venta...')
            
            args = [id_client, id_producto, cantidad, 0]
            
            result_args = self.cursor.callproc('sp_crear_venta', args)
            
            self.conn.commit()
            new_sale_id = result_args[3]

            cleaner()
            print(f'*** VENTA #{new_sale_id} REALIZADA CON EXITO ***')
            print(f'Se compraron {cantidad} ud. de {nombre_articulo} por un total de ${total_real_con_iva:.2f}.')
        except errors.DatabaseError as e:
            print(f"\n¡ERROR AL PROCESAR LA VENTA!")
            print(f"Base de Datos dice: {e.msg}")
            
        except Exception as e:
            print(f'Error inesperado en Python: {e}')
            
        finally:
            input('Presione enter para volver al menu principal.')
        
        
    def reporte_ventas_cliente_fecha(self):
        try:
            cleaner()
            print('*** REPORTE DE VENTAS POR CLIENTE Y FECHA ***')
            
            id_client = pedir_int("Ingrese el id del cliente: ", 1, sys.maxsize)
            fecha_inicio = pedir_fecha("Ingrese la fecha de inicio (YYYY-MM-DD): ")

            self.cursor.callproc('sp_consultar_ventas_cliente_fecha', [id_client, fecha_inicio])

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
            input("\nPresione enter para volver al menú...")

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
            input("\nPresione enter para volver al menú...")
        

class Inventario:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def crear_producto(self):
        try:
            cleaner()
            print('** NUEVO PRODUCTO **')
            nombre = pedir_str_no_vacio('Introduzca el nombre del producto: ')
            stock = pedir_int('Introduzca el stock inicial: ', 0, sys.maxsize)
            precio = pedir_float('Introduzca el precio: ', 0.01, float('inf'))
            id_prov = pedir_int('Introduzca el ID del proveedor (0 para ninguno): ', 0, sys.maxsize)

            cleaner()
            print("Verifique los datos del nuevo producto:")
            print(f"Nombre: {nombre}")
            print(f"Stock: {stock}")
            print(f"Precio: ${precio:.2f}")
            print(f"ID Proveedor: {id_prov if id_prov > 0 else 'N/A'}")
            
            if not pedir_confirmacion("¿Son correctos los datos? (S/N): "):
                print('*** Operación cancelada. ***')
                return

            args = (nombre, stock, precio, id_prov, 0)
            result_args = self.cursor.callproc('sp_insertar_producto', args)
            self.conn.commit()

            new_id = result_args[4]
            print(f'*** Producto #{new_id} ({nombre}) creado con exito. ***')

        except errors.DatabaseError as e:
            print(f"\n¡ERROR AL CREAR PRODUCTO!")
            print(f"Base de Datos dice: {e.msg}")
            self.conn.rollback()
        except Exception as e:
            print(f'Error inesperado al crear producto: {e}')
            self.conn.rollback()
        finally:
            input('Presione enter para volver al menú.')

    def eliminar_producto(self):
        try:
            cleaner()
            print(f'** ELIMINAR PRODUCTO **')
            produ_id = pedir_int('Introduce el id del producto a eliminar: ', 1, sys.maxsize)

            sql_produ = ('SELECT * FROM productos WHERE id_producto = %s')
            self.cursor.execute(sql_produ, (produ_id,))
            datos = self.cursor.fetchone()

            if not datos:
                print(f"Error: No se encontró ningún producto con el ID {produ_id}.")
                return

            if not self.validar_produ(datos):
                return
            
            if not pedir_confirmacion("esta seguro de que desea eliminar este producto?"):
                print('*** Operación cancelada. ***')
                return
            
            self.cursor.callproc('sp_eliminar_producto', (produ_id,))
            self.conn.commit()
            
            print(f'*** Producto #{produ_id} eliminado exitosamente. ***')

        except errors.DatabaseError as e:
            print(f'Error en la base de datos: {e.msg}')
            self.conn.rollback()
        except Exception as e:
            print(f'Error inesperado al eliminar producto: {e}')
            self.conn.rollback()
        finally:
            input('Presione enter para volver al menú.')

    def actualizar_stock(self):
            try:
                cleaner()
                while True:
                    print(f'** ACTUALIZAR PRODUCTO **')

                    produ_id = pedir_int('Introduce el id del producto: ', 1, sys.maxsize)


                    sql_produ = ('SELECT * FROM productos WHERE id_producto = %s')
                    self.cursor.execute(sql_produ, (produ_id,))
                    datos_produ = self.cursor.fetchone()
                    
                    if not datos_produ:
                        print(f"Error: No se encontro producto con ID {produ_id}")
                        return

                    if not self.validar_produ(datos_produ):
                        return

                    cleaner()
                    option = menu_actualizar_produ()

                    if option == 0:
                        print('Cancelando modificacion...')
                        return
                    

                    if option == 1:
                        new_dato = pedir_str_no_vacio('Introduzca el nuevo nombre: ')
                        self.cursor.callproc('sp_actualizar_producto_nombre', (produ_id, new_dato))
                    elif option == 2:
                        new_dato = pedir_int('Introduzca la nueva cantidad en inventario: ', 0, sys.maxsize)
                        self.cursor.callproc('sp_actualizar_producto_stock', (produ_id, new_dato))
                    elif option == 3:
                        new_dato = pedir_float('Introduce el nuevo precio del producto: ', 0.01, float('inf'))
                        self.cursor.callproc('sp_actualizar_producto_precio', (produ_id, new_dato))
                    elif option == 4:
                        new_dato = pedir_int('Introduzca el nuevo ID del proveedor (0 para ninguno): ', 0, sys.maxsize)
                        self.cursor.callproc('sp_actualizar_producto_proveedor', (produ_id, new_dato))

                    print('** Verificación de Datos actualizados **')
                    sql_produ = ('SELECT * FROM productos WHERE id_producto = %s')
                    self.cursor.execute(sql_produ, (produ_id,))
                    datos_nuevos = self.cursor.fetchone()
                    
                    if not self.validar_produ(datos_nuevos):
                        print('Deshaciendo ultimo movimiento...')
                        self.conn.rollback()
                        print('Ultimo movimiento eliminado exitosamente...')
                        return
                    
                    self.conn.commit()
                    print(f'*** Producto #{produ_id} actualizado con exito. ***')
                    return
                    
            except errors.IntegrityError as e:
                print(f'Error de integridad: {e}')
                self.conn.rollback()
            except errors.DatabaseError as e:
                print(f'Error en la base de datos: {e.msg}')
                self.conn.rollback()
            except Exception as e:
                print(f'Error inesperado al actualizar producto: {e}')
                self.conn.rollback()
            finally:
                input('Presione enter para volver al menu principal.')

    def validar_produ(self, datos)->bool:
        try:
            print('Datos del producto:')
            print(f'{"Id_Articulo":<15} {"Nombre":<20} {"Stock":<10} {"Precio":<15} {"Id_Proveedor":<15}')
            
            precio_formateado = f"${datos[3]:.2f}"
            id_proveedor = datos[4] if datos[4] is not None else "N/A"

            print(f'{str(datos[0]):<15} | {str(datos[1]):<20} | {str(datos[2]):<10} | {precio_formateado:<15} | {str(id_proveedor):<15}')
            print()

            option = pedir_int('estos son los datos correctos? \n(1: Confirmar, 2: Cancelar): ', 1, 2)
            if option == 2:
                print('*** Operacion cancelada. ***')
                return False
            return True
        except Exception as e:
            print(f'Error en validar_produ: {e}')
            return False

    def reporte_stock(self):
        try:
            cleaner()
            print('*** REPORTE DE INVENTARIO ***')
            
            self.cursor.callproc('sp_reporte_stock')
            if not self.cursor:
                print("No hay productos en inventario.")
                return
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
                print(" | ".join(f"{str(col):<20}" for col in row))

        except Exception as e:
            print('Error inesperado: ', e)
        finally:
            input("\nPresione enter para volver al menú...")

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
                return
        except errors.DatabaseError as e: 
            print(f"\n¡ERROR AL REGISTRAR PROVEEDOR!")
            print(f"Base de Datos dice: {e.msg}")
            self.conn.rollback()
        except Exception as e:
            print(f'Error inesperado al insertar proveedor: {e}')
            self.conn.rollback()
        finally:
            input('Presione enter para volver al menu principal.')
 
    
    def actualizar_proveedor(self):
        try:
            cleaner()
            print(f"** ACTUALIZAR PROVEEDOR **")   
            proveedor_id = pedir_int('Introduce el id del proveedor: ', 1, sys.maxsize)
            sql_proveedor = ('SELECT * FROM proveedores WHERE id_proveedor = %s')
            self.cursor.execute(sql_proveedor, (proveedor_id,))
            datos = self.cursor.fetchone()
            
            if not datos:
                print(f"Error: No se encontró ningún proveedor con el ID {proveedor_id}.")
                return
            
            if not self.validar_proveedor(datos):
                return
            
            cleaner()
            option = menu_actualizar_proveedor()
            
            if option == 0:
                print("Cancelando modificación...")
                return
            
            if option == 1:
                new_dato = pedir_telefono("Introduzca el nuevo telefono: ")
                self.cursor.callproc('sp_actualizar_proveedor_telefono', (proveedor_id, new_dato))
            elif option == 2:
                new_dato = pedir_str_no_vacio("Introduzca el nuevo nombre: ")
                self.cursor.callproc('sp_actualizar_proveedor_nombre', (proveedor_id, new_dato))

            print("** Verificación de datos actualizados **")
            sql_proveedor = ('SELECT * FROM proveedores WHERE id_proveedor = %s')
            self.cursor.execute(sql_proveedor, (proveedor_id,))
            datos_nuevos = self.cursor.fetchone()
            
            if not self.validar_proveedor(datos_nuevos): 
                print("Deshaciendo último movimiento...")
                self.conn.rollback()
                input("Ultimo movimiento cancelado exitosamente...")
                return
            
            self.conn.commit()
            print(f"*** Proveedor #{proveedor_id} actualizado con exito. ***")
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
            input("Presione enter para volver al menú principal.")
        
    def validar_proveedor(self, datos) -> bool:
        try:
            print("Datos del proveedor")
            print(f"{"Id_Proveedor":<15} {"Telefono":<15} {"Nombre":<15}")
            print(f"{str(datos[0]):<15} | {str(datos[1]):15} | {str(datos[2]):<15}")
            print()
            
            option = pedir_int('estos son los datos correctos? \n(1: Confirmar, 2: Cancelar): ', 1, 2)
            if option == 2:
                print("***Operación cancelada. ***")
                return False
            return True
        except Exception as e:
            print(f"Error en validar_cliente.: {e}")
            return False

    def eliminar_proveedor(self):
        try:
            cleaner()
            print(f'** ELIMINAR PROVEEDOR **')
            proveedor_id = pedir_int('Introduce el id del proveedor a eliminar: ', 1, sys.maxsize)

            sql_proveedor = ('SELECT * FROM proveedores WHERE id_proveedor = %s')
            self.cursor.execute(sql_proveedor, (proveedor_id,))
            datos = self.cursor.fetchone()

            if not datos:
                print(f"Error: No se encontró ningún proveedor con el ID {proveedor_id}.")
                return

            if not self.validar_proveedor(datos):
                print('*** Operación cancelada. ***')
                return
            
            if not pedir_confirmacion("¿ESTÁ SEGURO de que desea eliminar este proveedor?"):
                print('*** Operación cancelada. ***')
                return
            
            self.cursor.callproc('sp_eliminar_proveedor', (proveedor_id,))
            self.conn.commit()
            
            print(f'*** Proveedor #{proveedor_id} eliminado exitosamente. ***')
        
        except errors.IntegrityError as e:
            print(f'Error de integridad: No se puede eliminar el proveedor.')
            print(f'Asegúrese de que ningún producto esté asignado a este proveedor primero.')
            self.conn.rollback()
        except errors.DatabaseError as e:
            print(f'Error en la base de datos: {e.msg}')
            self.conn.rollback()
        except Exception as e:
            print(f'Error inesperado al eliminar proveedor: {e}')
            self.conn.rollback()
        finally:
            input('Presione enter para volver al menú.')
        
    def reporte_proveedores(self):
        try:
            cleaner()
            print("*** REPORTE DE PROVEEDORES ACTIVOS ***")
            
            self.cursor.callproc('sp_reporte_proveedores')
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
                print(" | ".join(f"{str(col):<20}" for col in row))
                
        except Exception as e:
            print("Error inesperado: ", e)
        finally:
            input("\nPresione enter para volver al menú...")