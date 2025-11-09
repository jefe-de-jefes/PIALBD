import os
import sys
import re

def pedir_correo(messagge:str):
    formato_correo = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    while True:
        correo = input(messagge)
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
