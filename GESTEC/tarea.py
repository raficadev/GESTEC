# Aplicación de Terminal/Consola para gestionar tareas pendientes.

"""
Este código está bajo la licencia:
Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) 
creada por Rafel Castelló Fiol (raficadev) en 2024.

Puedes encontrar más información sobre la licencia en:
https://www.safecreative.org/work/2405097929940-gestec
"""

from datetime import datetime
from colorama import Fore, Style

class Tarea:
    """Define una tarea con su descripción, estado de compleción, prioridad y fecha de creación."""
    
    def __init__(self, descripcion, prioridad=False, fecha_creacion=None, estado=False):
        """Constructor de la clase que inicializa los atributos con la descripción proporcionada, la prioridad y la fecha y hora actual."""
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.now()
        self.estado = estado
        self.prioridad = prioridad
    
    def marcar_completada(self):
        self.estado = True
    
    def __str__(self):
        """Define la representación en cadena de la tarea, mostrando la descripción, el estado y la fecha de creación."""
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