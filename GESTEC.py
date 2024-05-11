# >>>> GESTEC <<<< Programa para gestionar tareas pendientes.

from datetime import datetime                   # Importa el módulo para trabajar con fechas y horas.
import pickle                                   # Importa el módulo para almacenar los objetos en un archivo.
import os                                       # Importa el módulo para interactuar con el sistema operativo.
import platform                                 # Importa el módulo para recuperar información sobre la plataforma.



class Tarea:    # Define una tarea con su descripción, estado de compleción y fecha de creación.
    
    
    def __init__(self, descripcion):            # Constructor de la clase que inicializa los atributos con la descripción proporcionada y la fecha y hora actual.
        self.descripcion = descripcion          # (str): Almacena la descripción textual de la tarea.
        self.fecha_creacion = datetime.now()    # (datetime): Registra la fecha y hora en que se creó la tarea.
        self.estado = False                     # (bool): Indica si la tarea está completada 'True' o pendiente 'False'.
     
        
    def marcar_completada(self):                # Cambia el estado de la tarea a completada 'True'.
        self.estado = True


    def __str__(self):                          # Define la representación en cadena de la tarea, mostrando la descripción, el estado y la fecha de creación formateada.
        estado = "Completada" if self.estado else "Pendiente"
        return f"- {self.descripcion} ({estado}) - {self.fecha_creacion.strftime('%d-%m-%Y %H:%M')}"



class GestorTareas:             # Gestiona una lista permitiendo añadir, completar y eliminar tareas.
    mensaje_accion = f"         ¡Me encanta que estés aquí!\n \n   Selecciona la acción que voy a realizar:"  # Se utilizará para almacenar mensajes de acciones realizadas.
    
    
    def __init__(self):
        self.tareas = []            # (list): Lista que almacena objetos de tipo 'Tarea'.
        
        
    def mostrar_tareas(self):       # Función para mostrar la lista de tareas.
        if not self.tareas:         # Comprueba si la lista de tareas está vacía.
            print("\n               ¡¡¡Hurraaa!!!\n \n        No tienes tareas pendientes.")
            return
        
        print("\n------------ LISTADO DE TAREAS: -------------\n")
        for i in range(len(self.tareas)):
            tarea = self.tareas[i]              # Recorre la lista de tareas
            print(f"{i + 1}. {tarea}")          # y las imprime en formato de texto claro.


    def agregar_tarea(self):                    # Función para agregar una nueva tarea a la lista.
        self.mensaje_accion = f""
        descripcion = input("\n -> GESTEC: ¿Qué nombre le pongo a la nueva tarea?\n \n -> YO: ") # Solicita al usuario la descripción de la tarea,
        if not descripcion.strip():                                                              # validación de descripción vacía o solo espacios en blanco.
            self.mensaje_accion = f"  ¡No has indicado ningún nombre para la tarea!"
            return
        
        nueva_tarea = Tarea(descripcion)                                                         # Crea un nuevo objeto 'Tarea',
        self.tareas.append(nueva_tarea)                                                          # y agrega el nuevo objeto a la lista de tareas.
        self.mensaje_accion = f"  ¡Ahora tienes una nueva tarea pendiente!"
        guardar_tareas(self, "tareas.dat")                                                       # Guarda las tareas en un archivo.
        return self.mensaje_accion


    def marcar_completada(self):                 # Función para marcar una tarea como completada.
        if not self.tareas:                      
            self.mensaje_accion = f"  ¡No tienes ninguna tarea pendiente!"
            return self.mensaje_accion

        try:
            posicion = int(input("\n -> GESTEC: ¿Cuál es la posición de la tarea que has completado?\n \n -> YO: "))    # Solicita al usuario la posición de la tarea completada.
            if 1 <= posicion <= len(self.tareas):                                       # Valida la posición introducida.
                self.tareas[posicion - 1].marcar_completada()                           # Marca la tarea en la posición indicada como completada utilizando el método 'marcar_completada()' del objeto 'Tarea'.
                self.mensaje_accion = f"  ¡Genial, ahora la tarea está completada!"
                guardar_tareas(self, "tareas.dat")
                return self.mensaje_accion
                
            else:                                                                      # Si la posición es inválida,
                self.mensaje_accion = f"  ¡La posición que has indicado es inválida!"  # imprime un mensaje indicando que la posición introducida es incorrecta.
                return self.mensaje_accion
                
        except ValueError as e:                   # Maneja la excepción 'ValueError' si la entrada no es un número entero.
            if isinstance(e, ValueError):
                self.mensaje_accion = f"  ¡Tienes que introducir un número entero!"
                return self.mensaje_accion
            else:
                raise                             # Propagar la excepción no relacionada con el valor


    def eliminar_tarea(self):                     # Función para eliminar una tarea de la lista.
        if not self.tareas:
            self.mensaje_accion = f"  ¡No tienes ninguna tarea pendiente!"
            return self.mensaje_accion

        try:
            posicion = int(input("\n -> GESTEC: ¿Cuál es la posición de la tarea que quieres eliminar?\n \n -> YO: "))
            if 1 <= posicion <= len(self.tareas):
                del self.tareas[posicion - 1]     # Elimina la tarea en la posición indicada de la lista utilizando la instrucción 'del'.
                self.mensaje_accion = f"  ¡Ya no debe preocuparte esa tarea, ha sido eliminada!"
                guardar_tareas(self, "tareas.dat")
                return self.mensaje_accion
            else:
                self.mensaje_accion = f"  ¡La posición que has indicado es inválida!"
                return self.mensaje_accion
                
        except ValueError as e:
            if isinstance(e, ValueError):
                self.mensaje_accion = f"  ¡Tienes que introducir un número entero!"
                return self.mensaje_accion
            else:
                raise


def guardar_tareas(gestor_tareas, nombre_archivo):          # Función para guardar la lista de tareas en un archivo.
    with open(nombre_archivo, "wb") as archivo:             # Abre el archivo especificado en modo escritura binaria ("wb").
        pickle.dump(gestor_tareas.tareas, archivo)          # Serializa la lista de tareas almacenada en el atributo 'tareas' del objeto 'gestor_tareas' utilizando el módulo 'pickle'.
                                                            # El objeto serializado se escribe en el archivo abierto utilizando el método 'dump()'.


def cargar_tareas(gestor_tareas, nombre_archivo):           # Función para cargar la lista de tareas de un archivo.
    try:
        with open(nombre_archivo, "rb") as archivo:         # Intenta abrir el archivo especificado en modo lectura binaria ("rb").
            gestor_tareas.tareas = pickle.load(archivo)     # Deserializa el contenido del archivo abierto utilizando el módulo 'pickle'.
                                                            # El objeto deserializado se carga en el atributo 'tareas' del objeto 'gestor_tareas', reemplazando su contenido anterior.           
    except FileNotFoundError:       # Maneja la excepción que se produce si el archivo no existe.
        pass                        # En este caso, no se realiza ninguna acción y se ignora la excepción.
    except Exception as e:          # Manejo de otras excepciones.
        print(f"  ¡Ha ocurrido un error al cargar las tareas: {e}")


def limpiar_consola():                              # Función para limpiar la pantalla de la consola.
    sistema_operativo = platform.system()           # Detecta el sistema operativo del usuario y ejecuta el comando de limpieza adecuado. 
    if sistema_operativo == "Windows":              # Si el sistema operativo es Windows,
        os.system('cls')                            # ejecuta el comando 'cls' para limpiar la pantalla.
    elif sistema_operativo in ("Linux", "Darwin"):  # Si el sistema operativo es Linux o macOS,
        os.system('clear')                          # ejecuta el comando 'clear' para limpiar la pantalla.
    else:
        print("\n  --- Limpiando la consola... ---")
    

def mostrar_menu():                                 # Función para mostrar el menú principal de la aplicación.
    print("---------------- ACCIONES: ------------------\n")
    print(" > 1 - Añadir una tarea nueva.")
    print(" > 2 - Marcar una tarea completada.")
    print(" > 3 - Eliminar una tarea.")
    print(" > 4 - Salir del programa.")


def main():                                         # Función principal del programa.
    gestor_tareas = GestorTareas()                  # Crea una instancia del gestor de tareas
    cargar_tareas(gestor_tareas, "tareas.dat")      # Carga las tareas guardadas al iniciar el programa.
    
    
    while True:                                     # Bucle principal que se ejecuta hasta que el usuario selecciona la opción "Salir".      
        limpiar_consola()                                                    # En cada iteración, se limpia la consola,
        print("\n=============================================")
        print("======   > Gestor de tareas GESTEC <   ======")               # se muestra el encabezado del programa,
        print("=============================================")
        gestor_tareas.mostrar_tareas()                                       # se muestran las tareas pendientes,
        print("\n---------------------------------------------\n")
        mensaje_accion = gestor_tareas.mensaje_accion
        print(mensaje_accion)
        print("\n")
        mostrar_menu()                                                       # se muestra el menú de opciones,
        opcion = input("\n -> YO: Quiero que realices la acción número: ")   # se solicita la entrada de datos al usuario,
        
        match opcion:                                                        # se evalúa la opción seleccionada y se ejecuta la acción correspondiente.
            case "1":
                gestor_tareas.agregar_tarea()               
            case "2":
                gestor_tareas.marcar_completada()            
            case "3":
                gestor_tareas.eliminar_tarea()       
            case "4":
                guardar_tareas(gestor_tareas, "tareas.dat")                  # Guarda las tareas antes de salir.
                print(f"\n -> GESTEC: ¡Ha sido un placer ayudarte, nos vemos pronto!\n \n > Desconectando...\n")
                break                                                        # Fuerza la salida del bucle.

if __name__ == "__main__":
    main()
    
    """
    # LICENCIA:
    
        Este código está bajo la licencia Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) creada por Rafel Castelló Fiol (raficadev) en 2024.

        Puedes encontrar más información sobre la licencia en: https://www.safecreative.org/work/2405097929940-gestec
    """