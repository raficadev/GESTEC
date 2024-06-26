# GESTEC - Gestor de Tareas

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Colorama](https://img.shields.io/badge/Colorama-0.4.4-green.svg)](https://pypi.org/project/colorama/)
[![JSON](https://img.shields.io/badge/JSON-Data%20Format-0c8ec5.svg)](https://www.json.org/json-en.html)
[![pytest](https://img.shields.io/badge/pytest-framework-yellow.svg)](https://docs.pytest.org/en/stable/)
[![Safe Creative](https://img.shields.io/badge/Safe%20Creative-Registro%20de%20Derechos-orange.svg)](https://www.safecreative.org/)
[![CC BY-SA 4.0](https://img.shields.io/badge/CC%20BY--SA%204.0-Licencia-blue.svg)](https://creativecommons.org/licenses/by-sa/4.0/)


![Logo de GESTEC](images/LogoGESTEC.png)

**GESTEC** es una aplicación desarrollada en lenguaje `Python` que, haciendo uso de la interfaz de línea de comandos (CLI), permite al usuario a través de la Terminal/Consola del Sistema Operativo (SO) gestionar una lista de tareas pendientes. 

De manera sencilla permite añadir, completar, modificar y eliminar tareas. Las tareas son almacenadas en un archivo `tareas.json` al igual que el nombre de usuario `usuario.json` en la carpeta `Gestec Archivos` para su conservación y posterior cargado al volver a acceder a la aplicación.

---
## Tabla de Contenidos
1. [Características](#características)
2. [Hoja de Ruta](#hoja-de-ruta)
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
- Persistencia de datos en archivo `JSON`.

---
## Hoja de Ruta
Esta hoja de ruta detalla las etapas del desarrollo de **GESTEC**. Las fechas y características pueden ajustarse según las necesidades del proyecto y las contribuciones de la comunidad.

> [!NOTE]
> <details>
> <summary>Fase 1: Versión Inicial (v1.0.0). 
> 
> Fecha de lanzamiento: Mayo 2024</summary>
> - Gestión básica de tareas:
> - [x] Añadir tareas con nombre y prioridad.
> - [x] Marcar tareas como completadas.
> - [x] Modificar nombre y/o prioridad de tareas existentes.
> - [x] Eliminar tareas.
> - Persistencia de datos:
> - [x] Guardar y cargar tareas desde un archivo.
> - [x] Establecer nombre de usuario y recordarlo.
> - Interfaz de usuario en la terminal:
> - [x] Menú de opciones intuitivo.
> - [x] Mensajes interactivos con el usuario.
> - [x] Uso de `colorama` para resaltar texto.
</details>
  
Esta hoja de ruta es un plan vivo y está sujeto a cambios a medida que el proyecto evoluciona y se reciben comentarios de los usuarios y colaboradores. ¡Tu participación y retroalimentación son fundamentales para el éxito continuo de **GESTEC**!

---
## Instalación
**Prerrequisitos:**
- Python 3.7 o superior.

- `colorama`.
  
**Pasos para instalar el proyecto localmente:**
```bash
git clone https://github.com/raficadev/GESTEC.git
cd GESTEC
pip install -r requirements.txt
```

**Descargar el ejecutable:**

Si prefieres no clonar el repositorio y deseas usar una versión precompilada del programa, puedes descargar el ejecutable desde la sección de [Releases](https://github.com/raficadev/GESTEC/releases).
    
---
## Uso
Para iniciar el programa, ejecuta:
```bash
python3 GESTEC.py
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
1. Realiza un fork del proyecto.
2. Crea una nueva rama `git checkout -b nueva-funcionalidad`.
3. Realiza los cambios necesarios y haz commit `git commit -m 'Añadir nueva funcionalidad'`.
4. Sube los cambios a tu repositorio `git push origin nueva-funcionalidad`.
5. Abre un [Pull Request](https://github.com/raficadev/GESTEC/pulls).

También puedes contribuir de las siguientes formas:
1. Crea un [issue](https://github.com/raficadev/GESTEC/issues) con tus sugerencias o mejoras.
2. Participa en las discusiones de la comunidad en el repositorio.
   
**Por favor, asegúrate de que tu código sigue el estilo del proyecto y que todos los tests pasan.**

### Reporte de errores
Si encuentras un error, por favor abre un [issue](https://github.com/raficadev/GESTEC/issues) e incluye detalles sobre el problema.

---
## Licencia
Este proyecto está licenciado bajo la licencia [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) creada por [Rafel Castelló Fiol (raficadev)](https://github.com/raficadev) en 2024. 

Puedes encontrar más información sobre la licencia en [safecreative](https://www.safecreative.org/work/2405097929940-gestec).

El texto completo de la licencia se encuentra en el archivo [LICENSE](LICENSE).
    
---
## Autor
[Rafel Castelló Fiol (raficadev)](https://github.com/raficadev) - Desarrollador principal
![Banner](images/CDDDFB2D-7176-4772-A71D-4D6F3BADC7BB.jpeg)

---
## Agradecimientos
- A Fundae por la oportunidad, mediante su programa de becas, de haber podido realizar el curso Python Full Stack.
- Al igual que quiero agradecer la colaboración entre IBM SkillsBuild y a los chicos de BeJob por todo lo aprendido en el curso de Python Full Stack.
