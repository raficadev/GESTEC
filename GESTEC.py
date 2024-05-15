# Programa de Terminal/Consola para gestionar tareas pendientes.

from datetime import datetime   # Importa el módulo para trabajar con fechas y horas.
import pickle                   # Importa el módulo para almacenar los objetos en un archivo.
import os                       # Importa el módulo para interactuar con el sistema operativo.
import platform                 # Importa el módulo para recuperar información sobre la plataforma.

class Tarea:
    """Define una tarea con su descripción, estado de compleción, prioridad y fecha de creación."""
    
    def __init__(self, descripcion, prioridad = False):
        """Constructor de la clase que inicializa los atributos con la
        descripción proporcionada, la prioridad y la fecha y hora actual."""
        self.descripcion = descripcion          # (str): Almacena la descripción textual de la tarea.
        self.fecha_creacion = datetime.now()    # (datetime): Registra la fecha y hora en la que se añadió la tarea.
        self.estado = False                     # (bool): Indica si está completada 'True' o pendiente 'False'.
        self.prioridad = prioridad              # (bool): Indica si la tarea es prioritaria o no.
    
    def marcar_completada(self):
        self.estado = True
    
    def __str__(self):
        """Define la representación en cadena de la tarea, mostrando la
        descripción, el estado y la fecha de creación."""
        estado = "Completada" if self.estado else "Pendiente"
        return f"- {self.descripcion} ({estado}) - {self.fecha_creacion.strftime('%d-%m-%Y %H:%M')}"


class GestorTareas:
    """Gestiona una lista permitiendo añadir, completar y eliminar tareas."""
    carpeta_datos = os.path.join(os.path.expanduser("~"), "Gestec Archivos")
    archivo_datos = os.path.join(carpeta_datos, "tareas.dat")
    archivo_usuario = os.path.join(carpeta_datos, "usuario.txt")
    mensaje_accion = ""
    
    def __init__(self):
        self.tareas = []    # (list): Lista que almacena objetos de tipo 'Tarea'.
        self.crear_carpeta_datos()
        self.nombre_usuario = self.cargar_usuario()
        self.mensaje_accion = f"      ¡Me encanta que estés aquí {self.nombre_usuario}!\n \n   Selecciona la acción que voy a realizar:"
    
    def crear_carpeta_datos(self):
        """Crea la carpeta para almacenar las tareas si no existe."""
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)
    
    def cargar_usuario(self):
        """Carga el nombre de usuario desde un archivo o lo solicita si no existe."""
        if os.path.exists(self.archivo_usuario):
            with open(self.archivo_usuario, "r") as archivo:
                return archivo.read().strip()
        else:
            nombre = input(" -> GESTEC: ¿Cómo te llamas?\n -> ???: ")
            with open(self.archivo_usuario, "w") as archivo:
                archivo.write(nombre)
            return nombre
    
    def mostrar_tareas(self):
        if not self.tareas: # Comprueba si la lista de tareas está vacía.
            print(f"\n          ¡¡¡Hurraaa {self.nombre_usuario}!!!\n \n        No tienes tareas pendientes.")
            return
        
        # Separa las tareas en dos listas: alta_prioridad y normal_prioridad
        alta_prioridad = [tarea for tarea in self.tareas if tarea.prioridad]
        normal_prioridad = [tarea for tarea in self.tareas if not tarea.prioridad]
        
        print("\n------------ LISTADO DE TAREAS: -------------")
        if alta_prioridad:
            print("\n >> PRIORIDAD ALTA:\n")
            for i, tarea in enumerate(alta_prioridad, start=1):
                print(f"{i}. {tarea}")
        if normal_prioridad:
            print("\n \n >> PRIORIDAD NORMAL:\n")
            for i, tarea in enumerate(normal_prioridad, start=len(alta_prioridad) + 1):
                print(f"{i}. {tarea}")
    
    def agregar_tarea(self):
        descripcion = input(f"\n -> GESTEC: ¿Cómo quieres que se llame la nueva tarea?\n \n -> {self.nombre_usuario}: ")
        if not descripcion.strip(): # Validación de descripción vacía o solo espacios en blanco.
            self.mensaje_accion = "  ¡No has indicado ningún nombre para la tarea!"
            return
        
        respuesta_prioritaria = input(f"\n -> GESTEC: ¿Es una tarea prioritaria? (s/n)\n \n -> {self.nombre_usuario}: ").lower()
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
            posicion = int(input(f"\n -> GESTEC: ¿Cuál es la posición de la tarea que has completado?\n \n -> {self.nombre_usuario}: "))
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
            posicion = int(input(f"\n -> GESTEC: ¿Cuál es la posición de la tarea que quieres eliminar?\n \n -> {self.nombre_usuario}: "))
            if 1 <= posicion <= len(self.tareas):
                confirmacion = input(f"\n -> GESTEC: ¿Estás seguro que quieres eliminar la tarea '{self.tareas[posicion - 1].descripcion}'? (s/n)\n \n -> {self.nombre_usuario}: ").lower()
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
            posicion = int(input(f"\n -> GESTEC: ¿Cuál es la posición de la tarea que quieres modificar?\n \n -> {self.nombre_usuario}: "))
            if 1 <= posicion <= len(self.tareas):
                print(f"\n -> GESTEC: ¿Qué deseas modificar de la tarea '{self.tareas[posicion - 1].descripcion}'?")
                print("    1. Descripción")
                print("    2. Prioridad")
                opcion = input(f"\n -> {self.nombre_usuario}: ")
                if opcion == "1":
                    nueva_descripcion = input(f"\n -> GESTEC: La tarea '{self.tareas[posicion - 1].descripcion}' a partir de ahora ¿cómo se llamará?\n \n -> {self.nombre_usuario}: ")
                    if nueva_descripcion.strip():
                        self.tareas[posicion - 1].descripcion = nueva_descripcion
                        self.guardar_tareas()
                        self.mensaje_accion = "  ¡Se ha modificado el nombre de la tarea!"
                    else:
                        self.mensaje_accion = "  ¡No has indicado ningún nombre para la tarea! La tarea se mantendrá sin cambios."
                elif opcion == "2":
                    nueva_prioridad = input(f"\n -> GESTEC: ¿La tarea '{self.tareas[posicion - 1].descripcion}' es prioritaria? (s/n)\n \n -> {self.nombre_usuario}: ").lower() == 's'
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
        with open(self.archivo_datos, "wb") as archivo:
            pickle.dump(self.tareas, archivo)
        """Abre el archivo especificado en modo escritura binaria ("wb").
        Escribe en el archivo abierto utilizando el método 'dump()'."""
    
    def cargar_tareas(self):
        try:
            with open(self.archivo_datos, "rb") as archivo:
                self.tareas = pickle.load(archivo)
            """Intenta abrir el archivo especificado en modo lectura binaria ("rb")."""
        except FileNotFoundError:   # Maneja la excepción que se produce si el archivo no existe.
            pass                    # En este caso, no se realiza ninguna acción y se ignora la excepción.
        except Exception as e:
            print(f"  ¡Ha ocurrido un error al cargar las tareas: {e}")

def limpiar_consola():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def mostrar_menu():
    print("---------------- ACCIONES: ------------------\n")
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
        print("\n=============================================")
        print("======   > Gestor de tareas GESTEC <   ======")
        print("=============================================")
        gestor_tareas.mostrar_tareas()
        print("\n---------------------------------------------\n")
        print(gestor_tareas.mensaje_accion)
        print("\n")
        mostrar_menu()
        opcion = input(f"\n -> {gestor_tareas.nombre_usuario}: Quiero que realices la acción número: ")
        
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
            print(f"\n -> GESTEC: ¡Ha sido un placer ayudarte {gestor_tareas.nombre_usuario}, nos vemos pronto!\n \n > Desconectando...\n")
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
    