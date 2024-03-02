""" Importaciones """
from string import ascii_lowercase # Importamos las letras minúsculas del alfabeto
import sys # Importacion sys
import getpass # importacion getpass

""" Variables """
intentos = 0

"""  Solicitamos la contraseña al usuario """
contrasena_oculta = getpass.getpass("Ingrese la contraseña: ").lower()

""" Fuerza Bruta """
for letra in contrasena_oculta:
    for elemento in ascii_lowercase:
        if letra == elemento:
            intentos += 1
            break
        else:
            intentos += 1

"""  Mostramos el resultado """
print(f"La contraseña fue forzada en {intentos} intentos")