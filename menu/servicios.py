import json
def mostrar_servicios():
    with open("database.json","r") as servicio:
        lista =json.load(servicio)
        for x in lista["servicios"]:
            print(f"Nombre: {x['nombre']}")
            print(f"Capacidad: {x['capacidad']}")
            print(f"Inscritos: {x['inscritos']}")
            print("----------------------")
