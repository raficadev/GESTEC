import pytest
from gestor_tareas import GestorTareas, Tarea

def test_agregar_tarea():
    gestor = GestorTareas()
    tarea_descripcion = "Nueva tarea de prueba"
    gestor.agregar_tarea(tarea_descripcion, prioridad=False)
    assert len(gestor.tareas) == 1
    assert gestor.tareas[0].descripcion == tarea_descripcion

def test_marcar_completada():
    gestor = GestorTareas()
    gestor.agregar_tarea("Tarea para completar", prioridad=False)
    gestor.marcar_completada(1)
    assert gestor.tareas[0].estado == True