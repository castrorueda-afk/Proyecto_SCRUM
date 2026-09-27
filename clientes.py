import json
import os

DB_FILE = "database.json"

def cargar_datos():
    """Carga los datos desde el archivo JSON de forma segura."""
    if not os.path.exists(DB_FILE):
        return {"clientes": []}
    try:
        with open(DB_FILE, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if not contenido.strip():
                return {"clientes": []}
            return json.loads(contenido)
    except json.JSONDecodeError:
        return {"clientes": []}

def guardar_datos(datos):
    with open(DB_FILE, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def registrar_cliente():
    print("\n REGISTRO DE NUEVO CLIENTE (FORCETECH) ")
    
    while True:
        id_cliente = input("Ingrese el ID del cliente (solo números): ").strip()
        if id_cliente.isdigit():
            break
        else:
            print(" Error: Solo se permiten números para el ID. Intente de nuevo.")

    while True:
        nombre = input("Ingrese el nombre completo (solo letras): ").strip()
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print(" Error: El nombre solo debe contener letras. Intente de nuevo.")

    estado = input("Ingrese el estado (Ej: Activo / Inactivo): ").strip()
    riesgo = input("Ingrese el nivel de riesgo (Bajo / Medio / Alto): ").strip()
    
    datos = cargar_datos()
    
    nuevo_cliente = {
        "id": id_cliente,
        "nombre": nombre,
        "estado": estado,
        "riesgo": riesgo
    }
    
    datos["clientes"].append(nuevo_cliente)

    guardar_datos(datos)
    print("\nCliente registrado y guardado en el archivo JSON con éxito")

if __name__ == "__main__":
    registrar_cliente()