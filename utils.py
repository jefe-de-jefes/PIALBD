import os
import sys
import re
import getpass

def pedir_correo(messagge:str):
    formato_correo = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    while True:
        correo = input(messagge).strip()
        if re.match(formato_correo, correo.lower()):
            return correo
        else:
            print('Formato de correo invalido.')

def cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_int(messagge:str, min_val:int, max_val:int) -> int:
    while True:
        try:
            value:int = int(input(messagge))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Por favor, introduzca un numero entre {min_val} y {max_val}")
        except ValueError:
            print(f"Por favor, introduzca un numero entero valido.")

def pedir_float(messagge:str, min_val:float, max_val:float) -> float:
    while True:
        try:
            value:float = float(input(messagge))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Por favor, introduzca un numero entre {min_val} y {max_val}")
        except ValueError:
            print(f"Por favor, introduzca un numero flotante valido.")

def print_client(datos_user)->str:
    if(datos_user[1] == 'M'):
        return f'Mr {datos_user[0].upper()}'
    else:
        return f'Msr {datos_user[0].upper()}'

def pedir_sexo():
    while True:
        sex = input('Introduzca el sexo del cliente [M o F]: ').upper()
        if sex in ['M', 'F']:
            return sex
        else:
            print('Opcion no valida. Intente nuevamente')

def pedir_str_no_vacio(message: str) -> str:

    while True:
        value = input(message)
        

        if value.strip():
            return value.strip()
        else:
            print("Error: Este campo no puede estar vacío. Intente de nuevo.")

def pedir_confirmacion(message: str) -> bool:
    while True:
        value = input(message + " (S/N): ").upper().strip()
        if value in ['S', 'N']:
            return value == 'S'
        else:
            print("Error: Por favor ingrese 'S' para Sí o 'N' para No.")

def pedir_fecha(message: str) -> str:
    formato_fecha = r'^\d{4}-\d{2}-\d{2}$'  # Formato YYYY-MM-DD
    while True:
        fecha = input(message).strip()
        if re.match(formato_fecha, fecha):
            return fecha
        else:
            print('Formato de fecha inválido. Use el formato YYYY-MM-DD.')

def pedir_telefono(message: str) -> str:
    formato_telefono = r'^\+?\d{7,15}$'  # Permite números con 7 a 15 dígitos, opcionalmente con +
    while True:
        telefono = input(message).strip()
        if re.match(formato_telefono, telefono):
            return telefono
        else:
            print('Formato de teléfono inválido. Ingrese solo dígitos, puede incluir un + al inicio.')

def pedir_password(message: str) -> str:
    """
    Pide una contraseña (ocultando la entrada) y valida que no esté vacía.
    """
    while True:
        # Usamos getpass.getpass() en lugar de input()
        value = getpass.getpass(message)

        # La contraseña puede tener espacios, así que solo revisamos si no es ""
        if value: 
            return value
        else:
            print("Error: La contraseña no puede estar vacía. Intente de nuevo.")
