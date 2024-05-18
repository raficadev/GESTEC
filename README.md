# GESTEC - Gestor de Tareas
GESTEC es una aplicación desarrollada en lenguaje Python que, haciendo uso de la interfaz de línea de comandos (CLI), permite al usuario a través de la Terminal/Consola del Sistema Operativo (SO) gestionar una lista de tareas pendientes. 

De manera sencilla permite añadir, completar, modificar y eliminar tareas. Las tareas son almacenadas en un archivo `tareas.dat` al igual que el nombre de usuario `usuario.txt` en la carpeta `Gestec Archivos` para su conservación y posterior cargado al volver a acceder a la aplicación.

---
## Tabla de Contenidos
1. [Características](#características)
2. [Hoja de Ruta](#hojaderuta)
3. [Instalación](#instalación)
4. [Uso](#uso)
5. [Contribuir](#contribuir)
6. [Licencia](#licencia)
7. [Autor](#autor)
8. [Agradecimientos](#agradecimientos)
   
---
## Características
**Entre las principales características podemos destacar las siguientes:**
- Añadir nuevas tareas con nombre y prioridad.
- Marcar las tareas existentes como completadas.
- Modificar el nombre y/o la prioridad de las tareas existentes.
- Eliminar las tareas existentes.
- Almacenamiento de tareas en disco.

---
## Hoja de Ruta
Esta hoja de ruta detalla las etapas del desarrollo de GESTEC. Las fechas y características pueden ajustarse según las necesidades del proyecto y las contribuciones de la comunidad.

Fase 1: Versión Inicial (v1.0.0)
Fecha de lanzamiento: Mayo 2024

 - [x] Gestión básica de tareas:
   - [x] Añadir tareas con nombre y prioridad.
   - [x] Marcar tareas como completadas.
   - [x] Modificar nombre y/o prioridad de tareas existentes.
   - [x] Eliminar tareas.
 - [x] Persistencia de datos:
   - [x] Guardar y cargar tareas desde un archivo.
   - [x] Establecer nombre de usuario y recordarlo.
 - [x] Interfaz de usuario en la terminal.
   - [x] Menú de opciones intuitivo.
   - [x] Mensajes interactivos con el usuario.
   - [x] Uso de `colorama` para resaltar texto.
  
  Esta hoja de ruta es un plan vivo y está sujeto a cambios a medida que el proyecto evoluciona y se reciben comentarios de los usuarios y colaboradores. ¡Tu participación y retroalimentación son fundamentales para el éxito continuo de GESTEC!

---
## Instalación
**Prerrequisitos:**
- Python 3.7 o superior. Puedes descargarlo desde [python.org](https://python.org).

- `colorama` para los colores en la terminal. Instálalo con:
```bash
pip install colorama
```
**Pasos para instalar el proyecto localmente:**
1. Clonar el repositorio:
    ```bash
    git clone https://github.com/raficadev/GESTEC.git
    ```
2. Navegar al directorio del proyecto:
    ```bash
    cd gestec
    ```
3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
    
---
## Uso
Para iniciar el programa, ejecuta:
```bash
cd gestec
```
Seguido de:
```bash
python3 gestec.py
```
Sigue las instrucciones en pantalla para añadir, completar, modificar o eliminar tareas.
> [!NOTE]
> Opciones de menú:
> 1. Añadir una tarea nueva: Te pedirá el nombre y si es una tarea prioritaria.
> 2. Marcar una tarea como completada: Te pedirá la posición de la tarea que has completado.
> 3. Modificar una tarea existente: Te permitirá cambiar el nombre o la prioridad de una tarea.
> 4. Eliminar una tarea existente: Te pedirá confirmar la eliminación de una tarea.
> 5. Salir del programa: Guarda las tareas y cierra el programa.

---
## Contribuir
Las contribuciones son bienvenidas. Sigue estos pasos para contribuir:
1. Haz un fork del proyecto.
2. Crea una nueva rama `git checkout -b feature/nueva-funcionalidad`.
3. Realiza los cambios necesarios y haz commits `git commit -m 'Añadir nueva funcionalidad'`.
4. Sube los cambios a tu repositorio `git push origin feature/nueva-funcionalidad`.
5. Abre un Pull Request.

También puedes contribuir de las siguientes formas:
1. Crea un [issue](https://github.com/raficadev/GESTEC/issues) con tus sugerencias o mejoras.
2. Participa en las discusiones de la comunidad en el repositorio.
   
**Por favor, asegúrate de que tu código sigue el estilo del proyecto y que todos los tests pasan.**

### Reporte de errores
Si encuentras un error, por favor abre un [issue](https://github.com/raficadev/GESTEC/issues) e incluye detalles sobre el problema.

---
## Licencia
Este proyecto está licenciado bajo la licencia Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) creado por Rafel Castelló Fiol (raficadev) en 2024. Puedes encontrar más información sobre la licencia en [safecreative](https://www.safecreative.org/work/2405097929940-gestec).
    
---
## Autor
[Rafel Castelló Fiol (raficadev)](https://github.com/raficadev) - Desarrollador principal

---
## Agradecimientos
- A Fundae por la oportunidad, mediante su programa de becas, de haber podido realizar el curso Python Full Stack.
- Al igual que quiero agradecer la colaboración entre IBM SkillsBuild y a los chicos de BeJob por todo lo aprendido en el curso de Python Full Stack.
