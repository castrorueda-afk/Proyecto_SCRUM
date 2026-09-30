# Sistema de Gestión - Gimnasio ForceTech 

Este proyecto es un sistema de software diseñado para gestionar de manera eficiente las inscripciones, los servicios ofrecidos, los instructores y el seguimiento del progreso físico de los clientes del Gimnasio ForceTech. 

El desarrollo de este software se gestiona bajo el marco de trabajo ágil **SCRUM**, enfocándose en entregas incrementales y mejora continua.

##  Equipo de Desarrollo (Equipo SCRUM)
- **Castro** - Scrum Master / Infraestructura y Base de Datos
- **Eduardo** - Development Team (Módulo de Clientes)
- **Samid** - Development Team (Servicios)
- **Vazques** - Development Team (Matrículas y Reportes)

## Tecnologías Utilizadas
- **Lenguaje Principal:** Python (Lógica y consola)
- **Base de Datos / Persistencia:** Archivos JSON (`database.json`)
- **Control de Versiones:** Git & GitHub (Commits Convencionales)
- **Gestión Ágil:** Monday.com (Tablero Kanban)

---

## 📅 Bitácora de Desarrollo y Evidencias (Daily Stand-ups)

En esta sección se documenta el progreso diario, las problemáticas encontradas y las soluciones aplicadas durante los Sprints.

### Día 1 - Sábado 26 de Septiembre
- **¿Qué hicimos?** 
  - Planificación del Sprint 1 y creación del repositorio en GitHub. 
  - Configuración del archivo `.gitignore` para Python.
  - Implementación de la **estructura inicial del código en Python** (`main.py`) con lógica de persistencia en archivos JSON (`database.json`).
  - Incorporación de validaciones interactivas (`input`, `strip`, `.isdigit()`, `.isalpha()`) para asegurar el registro correcto de datos de los clientes.
- **¿Qué estamos estudiando/preparando?** Definiendo los flujos de datos en formato JSON y la integración de las ramas personales de Git mediante Commits Convencionales.
- **Problemas presentados (Impedimentos):** Hubo conflictos iniciales de historiales no relacionados al sincronizar la rama local con el repositorio remoto de GitHub y detalles en la acumulación de datos dentro del JSON.
- **Solución:** Se unificaron los historiales de Git de forma local, se estructuró el manejo seguro de archivos vacíos o existentes en Python y se aplicó la nomenclatura correcta de Commits Convencionales (`docs:`, `chore:`, `feat:`).
- **Evidencias:** 
![Tablero SCRUM configurado](![alt text](image.png))

## 📝 Reglas de Commits (Conventional Commits)
Para mantener un historial limpio, el equipo utiliza el siguiente estándar para subir código:
- `feat:` Nueva funcionalidad (ej. `feat(clientes): agregar logica de registro con json`).
- `fix:` Corrección de errores (ej. `fix(json): solucionar lectura de archivo vacio`).
- `docs:` Cambios en la documentación o README (ej. `docs(bitacora): actualizar bitacora del dia 1`).
- `chore:` Tareas de mantenimiento o configuración (ej. `chore(setup): agregar archivo .gitignore`).
### Día 2 - Domingo 27 de septiembre
* **¿Qué hicimos?** Estructuración modular del software (`menu.py`, `clientes.py`, persistencia de datos en `database.json`) y configuración del archivo `.gitignore` para ignorar carpetas del sistema como `__pycache__/`.
* **¿Qué estamos estudiando/preparando?** Configuración de bucles de control (`while`, condicionales `if/elif`) y gestión de rutas de importación entre archivos de Python en la misma carpeta.
* **Problemas presentados (Impedimentos):** 
  - Conflicto de fusión (*Merge Conflict*) en el archivo `README.md` al intentar sincronizar las ramas local y remota. 
  - Bloqueo temporal al hacer el `git push` debido a que existían cambios pendientes sin resolver ni aceptar en la interfaz de conflictos de VS Code. Se solucionó aceptando los cambios entrantes (*Accept Incoming Change*), limpiando los marcadores de conflicto y confirmando los commits correspondientes (`git add`, `git commit`).
* **Evidencia:**
![Estructura modular y menú en consola](![alt text](image.png))
### Día 3 - Lunes 28 de septiembre
* **¿Qué hicimos?** Refactorización del código base hacia una estructura modular limpia (`menu.py` y `clientes.py`) y sincronización con la persistencia en `database.json`.
* **¿Qué estamos estudiando/preparando?** Manejo de importaciones entre archivos locales de Python, validaciones de entrada (`isdigit`, `isalpha`) y depuración de errores de importación (`ImportError`).
* **Problemas presentados (Impedimentos):** 
  - Error de importación (`ImportError: cannot import name 'ver_prioridad'`) al intentar vincular el menú con el módulo de clientes debido a que la función faltaba en el archivo secundario. 
  - Se solucionó añadiendo la función de consulta en `clientes.py` y asegurando que las rutas de los archivos estuvieran en el mismo directorio de trabajo.
* **Evidencia:**
![Estructura modular y depuración de código](./evidencias/dia3_refactor.png)