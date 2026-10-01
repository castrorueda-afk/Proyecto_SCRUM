# Sistema de Gestión - Gimnasio ForceTech 

Este proyecto es un sistema de software diseñado para gestionar de manera eficiente las inscripciones, los servicios ofrecidos, los instructores y el seguimiento del progreso físico de los clientes del Gimnasio ForceTech. 

El desarrollo de este software se gestiona bajo el marco de trabajo ágil **SCRUM**, enfocándose en entregas incrementales y mejora continua.

## 👥 Equipo de Desarrollo (Equipo SCRUM)
- **Castro** - Scrum Master / Infraestructura y Base de Datos
- **Eduardo** - Development Team (Módulo de Clientes)
- **Samid** - Development Team (Servicios)
- **Vazques** - Development Team (Matrículas y Reportes)

## 🛠️ Tecnologías Utilizadas
- **Lenguaje Principal:** Python (Lógica y consola)
- **Base de Datos / Persistencia:** Archivos JSON (`database.json`)
- **Control de Versiones:** Git & GitHub (Commits Convencionales)
- **Gestión Ágil:** Monday.com (Tablero Kanban)

---

## 📅 Bitácora de Desarrollo y Evidencias (Daily Stand-ups)

En esta sección se documenta el progreso diario, las problemáticas encontradas y las soluciones aplicadas durante los Sprints.

### Día 1 - Sábado 26 de Septiembre
- **¿Qué hicimos?** 
  - Planificación del Sprint 1 y creación del repositorio en GitHub[cite: 3]. 
  - Configuración del archivo `.gitignore` para Python.
  - Implementación de la estructura inicial del código en Python con lógica de persistencia en archivos JSON (`database.json`).
  - Incorporación de validaciones interactivas (`input`, `strip`, `.isdigit()`, `.isalpha()`) para asegurar el registro correcto de datos de los clientes.
- **¿Qué estamos estudiando/preparando?** Definiendo los flujos de datos en formato JSON y la integración de las ramas personales de Git mediante Commits Convencionales.
- **Problemas presentados (Impedimentos):** Hubo conflictos iniciales de historiales no relacionados al sincronizar la rama local con el repositorio remoto de GitHub y detalles en la acumulación de datos dentro del JSON.
- **Solución:** Se unificaron los historiales de Git de forma local, se estructuró el manejo seguro de archivos vacíos o existentes en Python y se aplicó la nomenclatura correcta de Commits Convencionales (`docs:`, `chore:`, `feat:`).

### Día 2 - Domingo 27 de Septiembre
* **¿Qué hicimos?** Estructuración modular inicial del software (`menu.py`, `clientes.py`, persistencia de datos en `database.json`) y configuración del archivo `.gitignore` para ignorar carpetas del sistema como `__pycache__/`.
* **¿Qué estamos estudiando/preparando?** Configuración de bucles de control (`while`, condicionales `if/elif`) y gestión de rutas de importación entre archivos de Python en la misma carpeta.
* **Problemas presentados (Impedimentos):** 
  - Conflicto de fusión (*Merge Conflict*) en el archivo `README.md` al intentar sincronizar las ramas local y remota. 
  - Bloqueo temporal al hacer el `git push` debido a cambios pendientes. Se solucionó aceptando los cambios correspondientes, limpiando los marcadores de conflicto y confirmando los commits (`git add`, `git commit`).

### Día 3 - Lunes 28 de Septiembre
* **¿Qué hicimos?** Refactorización total del código base hacia una arquitectura modular limpia separando la interfaz (`menu.py`) de la lógica de negocio y persistencia (`clientes.py` interactuando con `database.json`).
* **¿Qué estamos estudiando/preparando?** Manejo de importaciones cruzadas entre módulos locales de Python, validaciones avanzadas de entrada de datos y depuración de errores en tiempo de ejecución.
* **Problemas presentados (Impedimentos):** 
  - Error de importación (`ImportError: cannot import name 'ver_prioridad'`) al intentar vincular el menú principal con el módulo secundario de clientes debido a la ausencia inicial de la función de consulta.
  - Se solucionó añadiendo e integrando correctamente la función `ver_prioridad()` en `clientes.py`, asegurando la sincronización de directorios de trabajo.
  - <img width="1770" height="1027" alt="image" src="https://github.com/user-attachments/assets/e13a9157-4042-4ff7-a424-89e978d06d9d" />


### Día 4 y 5 - Actualización y Sincronización del Sistema
* **¿Qué hicimos?** Consolidación definitiva del flujo del menú interactivo (opciones 1 a 5), pruebas de escritura y lectura en tiempo real sobre `database.json`, y resolución de estados de bloqueo en Git (`MERGE_HEAD` y limpieza de entornos locales).
* **¿Qué estamos estudiando/preparando?** Preparación de los entregables finales del Sprint para la sustentación y revisión del cumplimiento de la rúbrica de evaluación Scrum.
* **Problemas presentados (Impedimentos):** 
  - Bloqueos de terminal por archivos temporales de intercambio en Git/Vim durante fusiones interrumpidas.
  - Se solucionó abortando fusiones colgadas (`git merge --abort`), limpiando el árbol de trabajo y estabilizando la rama de desarrollo (`feature/castro`).

---

## 📝 Reglas de Commits (Conventional Commits)
Para mantener un historial limpio, el equipo utiliza el siguiente estándar para subir código:
- `feat:` Nueva funcionalidad (ej. `feat(clientes): agregar logica de registro con json`).
- `fix:` Corrección de errores (ej. `fix(json): solucionar lectura de archivo vacio`).
- `docs:` Cambios en la documentación o README (ej. `docs(bitacora): actualizar bitacora del proyecto`).
- `chore:` Tareas de mantenimiento o configuración (ej. `chore(setup): agregar archivo .gitignore`).
