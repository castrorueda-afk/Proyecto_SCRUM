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
- ## 📈 Evolución del Tablero SCRUM (Progreso del Proyecto)

A lo largo de los Sprints, el equipo ha mantenido un seguimiento riguroso de las tareas, épicas y requerimientos mediante el tablero Kanban en **Monday.com**. A continuación, se muestra la evolución visual del flujo de trabajo desde la planificación inicial hasta la finalización de los componentes:

### 1. Configuración y Planificación Inicial del Sprint
En las primeras fases se definieron las épicas principales, el backlog del producto y la asignación inicial de tareas para cada integrante del equipo (Juan Manuel Castro, Eduardo Gamboa, Samid Andrés Plata y Andrés Vázquez).
<img width="1641" height="851" alt="image" src="https://github.com/user-attachments/assets/0e4d6962-a8ea-46d5-b64a-9b31c90c40c2" />


### 2. Tablero Actualizado y Tareas Finalizadas
Con el avance de los días, la integración del código modular en Python (`menu.py`, `clientes.py` y `database.json`) y las pruebas continuas, las tarjetas del tablero se desplazaron progresivamente hacia la columna de **Hecho** (*Finalizada*), evidenciando el cumplimiento de los objetivos del Sprint.
<img width="1915" height="906" alt="image" src="https://github.com/user-attachments/assets/677e713a-84db-4fb1-8dc6-bee94ca070b3" />
link del cuadro de scrum:https://jmcastroruedas-team.monday.com/boards/18432853372/views/283078110
## 👥 Gestión de Roles SCRUM y Funciones del Equipo

Dentro del marco de trabajo ágil, la distribución de responsabilidades y la supervisión del proceso se estructuraron de la siguiente manera:

* **Juan Manuel Castro (Scrum Master y Product Owner):** Encargado de facilitar las ceremonias ágiles, eliminar los bloqueos e impedimentos técnicos (como la resolución de conflictos en Git y bloqueos de terminal), gestionar la estructura de la base de datos en formato JSON y asegurar que el desarrollo cumpliera con las pautas de la rúbrica del proyecto.
* **Eduardo Gamboa (Development Team):** Responsable del desarrollo, validaciones y lógica principal del módulo de gestión de clientes.
* **Samid Andrés Plata (Development Team):** Encargado del diseño, implementación y control de aforo del módulo de servicios del gimnasio.
* **Andrés Vázquez (Development Team):** Responsable de la estructuración de matrículas y la generación de reportes del sistema.

---

## 📞 Evidencia de Ceremonias y Reuniones de Sprints (Daily Stand-ups)

Para garantizar la sincronización continua, la resolución de impedimentos y la revisión de avances, el equipo realizó reuniones de seguimiento y coordinación mediante canales de voz y video en equipo. 

A continuación se muestran las evidencias de las conexiones y ceremonias realizadas:

* **Sincronización y Daily Stand-up en equipo:** Registro de las sesiones de trabajo colaborativo para alinear los avances del código modular y la integración de ramas.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/14dd7f35-174b-494f-bfde-917bbe9e3526" />

* **Revisión y depuración en conjunto:** Sesión de revisión de código y solución de errores de importación y rutas de persistencia.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4b1b5e6f-6bd0-409c-a0b9-cc711cd57699" />

* **Cierre y verificación de Sprint:** Encuentro final para constatar el estado de las tareas y preparar los entregables finales.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/55242acc-8c12-4c0b-81f2-4e20b4bac96e" />


