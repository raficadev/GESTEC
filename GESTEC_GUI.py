from PyQt5 import QtWidgets, QtGui, QtCore
from datetime import datetime
import json
import os

class Tarea:
    def __init__(self, descripcion, prioridad=False, fecha_creacion=None, estado=False):
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.now()
        self.estado = estado
        self.prioridad = prioridad
    
    def marcar_completada(self):
        self.estado = True
    
    def __str__(self):
        estado = "Completada" if self.estado else "Pendiente"
        prioridad = "Prioridad Alta" if self.prioridad else "Prioridad Normal"
        return f"{self.descripcion} ({estado}, {prioridad}) - {self.fecha_creacion.strftime('%d-%m-%Y %H:%M')}"
    
    def to_dict(self):
        return {
            'descripcion': self.descripcion,
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'estado': self.estado,
            'prioridad': self.prioridad
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            descripcion=data['descripcion'],
            prioridad=data['prioridad'],
            fecha_creacion=datetime.fromisoformat(data['fecha_creacion']),
            estado=data['estado']
        )

class GestorTareas:
    carpeta_datos = os.path.join(os.path.expanduser("~"), "Gestec Archivos")
    archivo_datos = os.path.join(carpeta_datos, "tareas.json")
    archivo_usuario = os.path.join(carpeta_datos, "usuario.json")
    
    def __init__(self, nombre_usuario=""):
        self.tareas = []
        self.crear_carpeta_datos()
        self.nombre_usuario = nombre_usuario if nombre_usuario else self.cargar_usuario()
    
    def crear_carpeta_datos(self):
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)
    
    def cargar_usuario(self):
        if os.path.exists(self.archivo_usuario):
            with open(self.archivo_usuario, "r") as archivo:
                return json.load(archivo)['nombre']
        else:
            nombre = "Usuario"
            with open(self.archivo_usuario, "w") as archivo:
                json.dump({'nombre': nombre}, archivo)
            return nombre
    
    def guardar_tareas(self):
        with open(self.archivo_datos, "w") as archivo:
            json.dump([tarea.to_dict() for tarea in self.tareas], archivo)
    
    def cargar_tareas(self):
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, "r") as archivo:
                self.tareas = [Tarea.from_dict(data) for data in json.load(archivo)]

class HtmlListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, gestor):
        super().__init__()
        self.gestor = gestor
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Gestor de Tareas')
        self.setGeometry(100, 100, 600, 400)
        
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        
        self.label_usuario = QtWidgets.QLabel(f"¡Hola, {self.gestor.nombre_usuario}!")
        self.layout.addWidget(self.label_usuario)
        
        self.lista_tareas_alta = QtWidgets.QListWidget()
        self.layout.addWidget(self.lista_tareas_alta)
        
        self.lista_tareas_normal = QtWidgets.QListWidget()
        self.layout.addWidget(self.lista_tareas_normal)
        
        self.boton_anadir = QtWidgets.QPushButton('Añadir Tarea')
        self.boton_anadir.clicked.connect(self.anadir_tarea)
        self.layout.addWidget(self.boton_anadir)
        
        self.boton_completar = QtWidgets.QPushButton('Completar Tarea')
        self.boton_completar.clicked.connect(self.completar_tarea)
        self.layout.addWidget(self.boton_completar)
        
        self.boton_modificar = QtWidgets.QPushButton('Modificar Tarea')
        self.boton_modificar.clicked.connect(self.modificar_tarea)
        self.layout.addWidget(self.boton_modificar)
        
        self.boton_eliminar = QtWidgets.QPushButton('Eliminar Tarea')
        self.boton_eliminar.clicked.connect(self.eliminar_tarea)
        self.layout.addWidget(self.boton_eliminar)
        
        self.mensaje_accion = QtWidgets.QLabel("")
        self.layout.addWidget(self.mensaje_accion)
        
        self.cargar_lista_tareas()
    
    def cargar_lista_tareas(self):
        self.lista_tareas_alta.clear()
        self.lista_tareas_normal.clear()
        self.gestor.cargar_tareas()
        for tarea in self.gestor.tareas:
            estado_color = 'green' if tarea.estado else 'red'
            estado_texto = f"<span style='color:{estado_color}'>{'Completada' if tarea.estado else 'Pendiente'}</span>"
            item_texto = f"{tarea.descripcion} ({estado_texto}) - {tarea.fecha_creacion.strftime('%d-%m-%Y %H:%M')}"

            # Creamos un QLabel y establecemos el formato de texto en RichText
            label = QtWidgets.QLabel()
            label.setTextFormat(QtCore.Qt.RichText)
            label.setText(item_texto)
        
            # Creamos un QListWidgetItem y establecemos el widget del ítem como el QLabel
            list_widget_item = QtWidgets.QListWidgetItem()
            list_widget_item.setData(QtCore.Qt.UserRole, tarea)
            list_widget_item.setSizeHint(label.sizeHint())  # Establecemos el tamaño del ítem para que se ajuste al contenido
            self.lista_tareas_normal.addItem(list_widget_item) if not tarea.prioridad else self.lista_tareas_alta.addItem(list_widget_item)
            self.lista_tareas_normal.setItemWidget(list_widget_item, label) if not tarea.prioridad else self.lista_tareas_alta.setItemWidget(list_widget_item, label)
    
    def anadir_tarea(self):
        descripcion, ok = QtWidgets.QInputDialog.getText(self, 'Añadir Tarea', 'Descripción de la tarea:')
        if ok and descripcion:
            prioridad = QtWidgets.QMessageBox.question(self, 'Prioridad', '¿Es una tarea prioritaria?', 
                                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            prioridad = (prioridad == QtWidgets.QMessageBox.Yes)
            nueva_tarea = Tarea(descripcion, prioridad)
            self.gestor.tareas.append(nueva_tarea)
            self.gestor.guardar_tareas()
            self.cargar_lista_tareas()
            self.mensaje_accion.setText("¡Ahora tienes una nueva tarea pendiente!")
    
    def completar_tarea(self):
        item = self.lista_tareas_alta.currentItem() or self.lista_tareas_normal.currentItem()
        if item:
            tarea = item.data(QtCore.Qt.UserRole)
            tarea.marcar_completada()
            self.gestor.guardar_tareas()
            self.cargar_lista_tareas()
            self.mensaje_accion.setText("¡Genial, la tarea se ha completado!")
    
    def modificar_tarea(self):
        item = self.lista_tareas_alta.currentItem() or self.lista_tareas_normal.currentItem()
        if item:
            tarea = item.data(QtCore.Qt.UserRole)
            opciones = ["Modificar el nombre", "Modificar la prioridad"]
            opcion, ok = QtWidgets.QInputDialog.getItem(self, "Modificar Tarea", 
                                                        f"¿Qué quieres modificar de la tarea '{tarea.descripcion}'?", 
                                                        opciones, 0, False)
            if ok and opcion:
                if opcion == "Modificar el nombre":
                    nueva_descripcion, ok = QtWidgets.QInputDialog.getText(self, 'Modificar Tarea', 'Nuevo nombre de la tarea:')
                    if ok and nueva_descripcion.strip():
                        tarea.descripcion = nueva_descripcion
                        self.gestor.guardar_tareas()
                        self.cargar_lista_tareas()
                        self.mensaje_accion.setText("¡Se ha modificado el nombre de la tarea!")
                    else:
                        self.mensaje_accion.setText("¡No has indicado ningún nombre para la tarea! La tarea se mantendrá sin cambios.")
                elif opcion == "Modificar la prioridad":
                    nueva_prioridad = QtWidgets.QMessageBox.question(self, 'Modificar Tarea', '¿La tarea es prioritaria?', 
                                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                    tarea.prioridad = (nueva_prioridad == QtWidgets.QMessageBox.Yes)
                    self.gestor.guardar_tareas()
                    self.cargar_lista_tareas()
                    self.mensaje_accion.setText("¡Se ha modificado la prioridad de la tarea!")
    
    def eliminar_tarea(self):
        item = self.lista_tareas_alta.currentItem() or self.lista_tareas_normal.currentItem()
        if item:
            tarea = item.data(QtCore.Qt.UserRole)
            confirmacion = QtWidgets.QMessageBox.question(self, 'Eliminar Tarea', 
                                                          f"¿Estás seguro que quieres eliminar la tarea '{tarea.descripcion}'?", 
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if confirmacion == QtWidgets.QMessageBox.Yes:
                self.gestor.tareas.remove(tarea)
                self.gestor.guardar_tareas()
                self.cargar_lista_tareas()
                self.mensaje_accion.setText("¡Listo, la tarea ha sido eliminada!")
            else:
                self.mensaje_accion.setText("Se ha cancelado la eliminación de la tarea.")

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gestor = GestorTareas()
    gestor.cargar_tareas()
    ventana = VentanaPrincipal(gestor)
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()