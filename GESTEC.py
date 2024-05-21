# Aplicación de Terminal/Consola para gestionar tareas pendientes.

from datetime import datetime   # Importa el módulo para trabajar con fechas y horas.
import json                     # Importa el módulo para almacenar los objetos en un archivo.
import os                       # Importa el módulo para interactuar con el sistema operativo.
import platform                 # Importa el módulo para recuperar información sobre la plataforma.
from colorama import init, Fore, Back, Style

init(autoreset=True)  # Inicializar Colorama para que los colores se reseteen después de cada uso

class Tarea:
    """Define una tarea con su descripción, estado de compleción, prioridad y fecha de creación."""
    
    def __init__(self, descripcion, prioridad = False, fecha_creacion=None, estado=False):
        """Constructor de la clase que inicializa los atributos con la
        descripción proporcionada, la prioridad y la fecha y hora actual."""
        self.descripcion = descripcion      # (str): Almacena la descripción textual de la tarea.
        self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.now()      # (datetime): Registra la fecha y hora en la que se añadió la tarea.
        self.estado = estado                # (bool): Indica si está completada 'True' o pendiente 'False'.
        self.prioridad = prioridad          # (bool): Indica si la tarea es prioritaria o no.
    
    def marcar_completada(self):
        self.estado = True
    
    def __str__(self):
        """Define la representación en cadena de la tarea, mostrando la
        descripción, el estado y la fecha de creación."""
        estado = f"{Fore.GREEN}Completada{Style.RESET_ALL}" if self.estado else f"{Fore.RED}Pendiente{Style.RESET_ALL}"
        return f"- {self.descripcion} ({estado}) - {self.fecha_creacion.strftime('%d-%m-%Y %H:%M')}"
    
    def to_dict(self):
        """Convierte la tarea a un diccionario para almacenamiento en JSON."""
        return {
            'descripcion': self.descripcion,
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'estado': self.estado,
            'prioridad': self.prioridad
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea una instancia de Tarea desde un diccionario."""
        return cls(
            descripcion=data['descripcion'],
            prioridad=data['prioridad'],
            fecha_creacion=datetime.fromisoformat(data['fecha_creacion']),
            estado=data['estado']
        )


class GestorTareas:
    """Gestiona una lista permitiendo añadir, completar y eliminar tareas."""
    carpeta_datos = os.path.join(os.path.expanduser("~"), "Gestec Archivos")
    archivo_datos = os.path.join(carpeta_datos, "tareas.json")
    archivo_usuario = os.path.join(carpeta_datos, "usuario.json")
    mensaje_accion = ""
    
    def __init__(self, nombre_usuario=""):
        self.tareas = []    # (list): Lista que almacena objetos de tipo 'Tarea'.
        self.crear_carpeta_datos()
        self.nombre_usuario = nombre_usuario if nombre_usuario else self.cargar_usuario()
        self.mensaje_accion = f"      ¡Me encanta que estés aquí {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}!\n \n   Selecciona la acción que voy a realizar:"
    
    def crear_carpeta_datos(self):
        """Crea la carpeta para almacenar las tareas si no existe."""
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)
    
    def cargar_usuario(self):
        """Carga el nombre de usuario desde un archivo o lo solicita si no existe."""
        if os.path.exists(self.archivo_usuario):
            with open(self.archivo_usuario, "r") as archivo:
                return json.load(archivo)['nombre']
        else:
            nombre = input(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: Soy {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}, y es un placer para mi darte la bienvenida a tu nuevo Gestor de Tareas.\n            ¿Puedes indicarme tu nombre?\n \n -> {Fore.CYAN}{Style.BRIGHT}???{Style.RESET_ALL}: ")
            with open(self.archivo_usuario, "w") as archivo:
                json.dump({'nombre': nombre}, archivo)
            return nombre
    
    def mostrar_tareas(self):
        if not self.tareas: # Comprueba si la lista de tareas está vacía.
            print(f"\n          ¡¡¡Hurraaa {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}!!!\n \n        No tienes tareas pendientes.")
            return
        
        # Separa las tareas en dos listas: alta_prioridad y normal_prioridad
        alta_prioridad = [tarea for tarea in self.tareas if tarea.prioridad]
        normal_prioridad = [tarea for tarea in self.tareas if not tarea.prioridad]
        
        print(f"\n{Style.BRIGHT}------------ LISTADO DE TAREAS: -------------{Style.RESET_ALL}")
        if alta_prioridad:
            print(f"\n{Fore.YELLOW}{Style.BRIGHT} >> PRIORIDAD ALTA:\n{Style.RESET_ALL}")
            for i, tarea in enumerate(alta_prioridad, start=1):
                print(f"{i}. {tarea}")
        if normal_prioridad:
            print(f"\n \n{Style.BRIGHT} >> PRIORIDAD NORMAL:\n{Style.RESET_ALL}")
            for i, tarea in enumerate(normal_prioridad, start=len(alta_prioridad) + 1):
                print(f"{i}. {tarea}")
    
    def agregar_tarea(self):
        descripcion = input(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¿Cómo quieres que se llame la nueva tarea?\n \n -> {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}: ")
        if not descripcion.strip(): # Validación de descripción vacía o solo espacios en blanco.
            self.mensaje_accion = "  ¡No has indicado ningún nombre para la tarea!"
            return
        
        respuesta_prioritaria = input(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¿Es una tarea prioritaria? (s/n)\n \n -> {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}: ").lower()
        if respuesta_prioritaria == 's':
            es_prioritaria = True
        elif respuesta_prioritaria == 'n':
            es_prioritaria = False
        else:
            self.mensaje_accion = "  ¡Respuesta inválida! Por favor, responde 's' para sí o 'n' para no."
            return
        
        nueva_tarea = Tarea(descripcion, es_prioritaria)    # Crea un nuevo objeto 'Tarea',
        self.tareas.append(nueva_tarea)     # y agrega el nuevo objeto a la lista de tareas.
        self.guardar_tareas()  # Guarda las tareas en un archivo.
        self.mensaje_accion = "  ¡Ahora tienes una nueva tarea pendiente!"
    
    def marcar_completada(self):
        if not self.tareas:                      
            self.mensaje_accion = "  ¡No tienes ninguna tarea pendiente!"
            return
        
        try:
            posicion = int(input(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¿Cuál es la posición de la tarea que has completado?\n \n -> {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}: "))
            if 1 <= posicion <= len(self.tareas):   # Valida la posición introducida.
                self.tareas[posicion - 1].marcar_completada()   # Marca la tarea en la posición indicada como completada utilizando el método 'marcar_completada()' del objeto 'Tarea'.
                self.guardar_tareas()
                self.mensaje_accion = "  ¡Genial, la tarea se ha completado!"
            else:
                self.mensaje_accion = "  ¡La posición que has indicado es inválida!"
        except ValueError: # Maneja la excepción 'ValueError' si la entrada no es un número entero.
                self.mensaje_accion = "  ¡Tienes que introducir un número entero!"
    
    def eliminar_tarea(self):
        if not self.tareas:
            self.mensaje_accion = "  ¡No tienes ninguna tarea pendiente!"
            return
        
        try:
            posicion = int(input(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¿Cuál es la posición de la tarea que quieres eliminar?\n \n -> {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}: "))
            if 1 <= posicion <= len(self.tareas):
                confirmacion = input(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¿Estás seguro que quieres eliminar la tarea '{self.tareas[posicion - 1].descripcion}'? (s/n)\n \n -> {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}: ").lower()
                if confirmacion == 's':
                    del self.tareas[posicion - 1]   # Elimina la tarea en la posición indicada de la lista utilizando la instrucción 'del'.
                    self.guardar_tareas()
                    self.mensaje_accion = "  ¡Listo, la tarea ha sido eliminada!"
                elif confirmacion == 'n':
                    self.mensaje_accion = "  Se ha cancelado la eliminación de la tarea."
                else:
                    self.mensaje_accion = "  El carácter introducido es inválido. Por favor, introduce 's' para eliminar o 'n' para cancelar."
            else:
                self.mensaje_accion = "  ¡La posición que has indicado es inválida!"        
        except ValueError:
                self.mensaje_accion = "  ¡Tienes que introducir un número entero!"
    
    def modificar_tarea(self):
        if not self.tareas:
            self.mensaje_accion = "  ¡No tienes ninguna tarea pendiente!"
            return
        
        try:
            posicion = int(input(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¿Cuál es la posición de la tarea que quieres modificar?\n \n -> {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}: "))
            if 1 <= posicion <= len(self.tareas):
                print(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¿Qué modificación quieres hacer de la tarea '{self.tareas[posicion - 1].descripcion}'?")
                print("\n > 1 - Modificar el nombre.")
                print(" > 2 - Modificar la prioridad.")
                opcion = input(f"\n -> {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}: ")
                if opcion == "1":
                    nueva_descripcion = input(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¿Cómo quieres renombrar a la tarea '{self.tareas[posicion - 1].descripcion}'?\n \n -> {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}: ")
                    if nueva_descripcion.strip():
                        self.tareas[posicion - 1].descripcion = nueva_descripcion
                        self.guardar_tareas()
                        self.mensaje_accion = "  ¡Se ha modificado el nombre de la tarea!"
                    else:
                        self.mensaje_accion = "  ¡No has indicado ningún nombre para la tarea! La tarea se mantendrá sin cambios."
                elif opcion == "2":
                    nueva_prioridad = input(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¿La tarea '{self.tareas[posicion - 1].descripcion}' es de prioridad alta? (s/n)\n \n -> {Fore.CYAN}{Style.BRIGHT}{self.nombre_usuario}{Style.RESET_ALL}: ").lower() == 's'
                    self.tareas[posicion - 1].prioridad = nueva_prioridad
                    self.guardar_tareas()
                    self.mensaje_accion = "  ¡Se ha modificado la prioridad de la tarea!"
                else:
                    self.mensaje_accion = "  ¡Opción inválida! Por favor, elige '1' para modificar el nombre o '2' para modificar la prioridad."
            else:
                self.mensaje_accion = "  ¡La posición que has indicado es inválida!"
        except ValueError:
            self.mensaje_accion = "  ¡Tienes que introducir un número entero!"
    
    def opcion_invalida(self):
        self.mensaje_accion = "  ¡No existe ninguna acción para el carácter introducido!\n \n  > * Elige un número de acción del 1 al 5. * <"
    
    def guardar_tareas(self):
        with open(self.archivo_datos, "w") as archivo:
            json.dump([tarea.to_dict() for tarea in self.tareas], archivo)
        """Abre el archivo especificado en modo escritura binaria ("wb").
        Escribe en el archivo abierto utilizando el método 'dump()'."""
    
    def cargar_tareas(self):
        try:
            with open(self.archivo_datos, "r") as archivo:
                datos = json.load(archivo)
                self.tareas = [Tarea.from_dict(data) for data in datos]
            """Intenta abrir el archivo especificado en modo lectura binaria ("rb")."""
        except FileNotFoundError:   # Maneja la excepción que se produce si el archivo no existe.
            pass                    # En este caso, no se realiza ninguna acción y se ignora la excepción.
        except Exception as e:
            print(f"  ¡Ha ocurrido un error al cargar las tareas: {e}")

def limpiar_consola():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def mostrar_menu():
    print(f"{Style.BRIGHT}---------------- ACCIONES: ------------------\n{Style.RESET_ALL}")
    print(" > 1 - Añadir una tarea nueva.")
    print(" > 2 - Marcar una tarea como completada.")
    print(" > 3 - Modificar una tarea existente.")
    print(" > 4 - Eliminar una tarea existente.")
    print(" > 5 - Salir del programa.")

def main():
    gestor_tareas = GestorTareas()  # Crea una instancia del gestor de tareas
    gestor_tareas.cargar_tareas()  # Carga las tareas guardadas al iniciar el programa.
    
    while True: # Bucle principal que se ejecuta hasta que el usuario selecciona la opción "Salir".      
        limpiar_consola()
        print(f"\n{Back.WHITE}{Fore.BLACK}=============================================")
        print(f"{Back.WHITE}{Fore.BLACK}==                 GESTEC                  ==")
        print(f"{Back.WHITE}{Fore.BLACK}==            Gestor de tareas             ==")
        print(f"{Back.WHITE}{Fore.BLACK}============================================={Style.RESET_ALL}")
        gestor_tareas.mostrar_tareas()
        print("\n---------------------------------------------\n")
        print(gestor_tareas.mensaje_accion)
        print("\n")
        mostrar_menu()
        opcion = input(f"\n -> {Fore.CYAN}{Style.BRIGHT}{gestor_tareas.nombre_usuario}{Style.RESET_ALL}: Quiero que realices la acción número: ")
        
        if opcion == "1":
            gestor_tareas.agregar_tarea()
        elif opcion == "2":
            gestor_tareas.marcar_completada()
        elif opcion == "3":
            gestor_tareas.modificar_tarea()
        elif opcion == "4":
            gestor_tareas.eliminar_tarea()
        elif opcion == "5":
            gestor_tareas.guardar_tareas()
            print(f"\n -> {Fore.MAGENTA}{Style.BRIGHT}GESTEC{Style.RESET_ALL}: ¡Ha sido un placer ayudarte {Fore.CYAN}{Style.BRIGHT}{gestor_tareas.nombre_usuario}{Style.RESET_ALL}, nos vemos pronto!\n \n > Desconectando...\n")
            break
        else:
            gestor_tareas.opcion_invalida()

if __name__ == "__main__":
    main()

    """Este código está bajo la licencia 
    Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) 
    creada por Rafel Castelló Fiol (raficadev) en 2024.
    
    Puedes encontrar más información sobre la licencia en:
    https://www.safecreative.org/work/2405097929940-gestec"""
    