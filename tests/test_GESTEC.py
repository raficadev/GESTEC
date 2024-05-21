import pytest
from datetime import datetime
from GESTEC import Tarea, GestorTareas

def test_crear_tarea():
    tarea = Tarea("Tarea de prueba", True)
    assert tarea.descripcion == "Tarea de prueba"
    assert tarea.prioridad == True
    assert isinstance(tarea.fecha_creacion, datetime)
    assert tarea.estado == False

def test_marcar_completada():
    tarea = Tarea("Tarea de prueba")
    tarea.marcar_completada()
    assert tarea.estado == True

def test_tarea_to_dict():
    tarea = Tarea("Tarea de prueba", True)
    tarea_dict = tarea.to_dict()
    assert tarea_dict["descripcion"] == "Tarea de prueba"
    assert tarea_dict["prioridad"] == True
    assert tarea_dict["estado"] == False
    assert "fecha_creacion" in tarea_dict

def test_tarea_from_dict():
    tarea_dict = {
        "descripcion": "Tarea de prueba",
        "prioridad": True,
        "fecha_creacion": datetime.now().isoformat(),
        "estado": False
    }
    tarea = Tarea.from_dict(tarea_dict)
    assert tarea.descripcion == tarea_dict["descripcion"]
    assert tarea.prioridad == tarea_dict["prioridad"]
    assert tarea.estado == tarea_dict["estado"]
    assert isinstance(tarea.fecha_creacion, datetime)

def test_agregar_tarea():
    gestor = GestorTareas(nombre_usuario="Test User")
    gestor.agregar_tarea("Tarea de prueba", False)
    assert len(gestor.tareas) == 1
    assert gestor.tareas[0].descripcion == "Tarea de prueba"
    assert not gestor.tareas[0].prioridad

def test_guardar_y_cargar_tareas(tmpdir):
    gestor = GestorTareas(nombre_usuario="Test User")
    gestor.carpeta_datos = tmpdir
    gestor.archivo_datos = str(tmpdir.join("tareas.json"))

    gestor.agregar_tarea("Tarea de prueba", False)
    assert len(gestor.tareas) == 1

    gestor.guardar_tareas()
    gestor.tareas = []  # Limpiar la lista de tareas
    gestor.cargar_tareas()
    assert len(gestor.tareas) == 1
    assert gestor.tareas[0].descripcion == "Tarea de prueba"
    assert not gestor.tareas[0].prioridad

def test_eliminar_tarea():
    gestor = GestorTareas(nombre_usuario="Test User")
    gestor.agregar_tarea("Tarea de prueba", False)
    assert len(gestor.tareas) == 1

    tarea = gestor.tareas[0]
    gestor.tareas.remove(tarea)  # Aquí se usa directamente el método remove para eliminar la tarea
    assert len(gestor.tareas) == 0