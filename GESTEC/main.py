# Aplicación de Terminal/Consola para gestionar tareas pendientes.

"""
Este código está bajo la licencia:
Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) 
creada por Rafel Castelló Fiol (raficadev) en 2024.

Puedes encontrar más información sobre la licencia en:
https://www.safecreative.org/work/2405097929940-gestec
"""

from gestor_tareas import GestorTareas
from colorama import Fore, Style, Back

def main():
    gestor_tareas = GestorTareas()
    gestor_tareas.cargar_tareas()
    
    while True:
        gestor_tareas.limpiar_consola()
        print(f"\n{Back.WHITE}{Fore.BLACK}=============================================")
        print(f"{Back.WHITE}{Fore.BLACK}==                 GESTEC                  ==")
        print(f"{Back.WHITE}{Fore.BLACK}==            Gestor de tareas             ==")
        print(f"{Back.WHITE}{Fore.BLACK}============================================={Style.RESET_ALL}")
        gestor_tareas.mostrar_tareas()
        print("\n---------------------------------------------\n")
        print(gestor_tareas.mensaje_accion)
        print("\n")
        gestor_tareas.mostrar_menu()
        opcion = input(f"\n -> {Fore.CYAN}{Style.BRIGHT}{gestor_tareas.nombre_usuario}{Style.RESET_ALL}: Quiero que realices la acción número: ")
        
        if opcion == "1":
            gestor_tareas.agregar_tarea()
        elif opcion == "2":
            gestor_tareas.operar_tarea("completar")
        elif opcion == "3":
            gestor_tareas.operar_tarea("modificar")
        elif opcion == "4":
            gestor_tareas.operar_tarea("eliminar")
        elif opcion == "5":
            gestor_tareas.guardar_tareas()
            print(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¡Ha sido un placer ayudarte {Fore.CYAN}{Style.BRIGHT}{gestor_tareas.nombre_usuario}{Style.RESET_ALL}, nos vemos pronto!\n \n > Desconectando...\n")
            break
        else:
            gestor_tareas.opcion_invalida()

if __name__ == "__main__":
    main()