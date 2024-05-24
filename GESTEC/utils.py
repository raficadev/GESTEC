# Aplicación de Terminal/Consola para gestionar tareas pendientes.

"""
Este código está bajo la licencia:
Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) 
creada por Rafel Castelló Fiol (raficadev) en 2024.

Puedes encontrar más información sobre la licencia en:
https://www.safecreative.org/work/2405097929940-gestec
"""

import os
import platform

def limpiar_consola():
    os.system('cls' if platform.system() == "Windows" else 'clear')