# Funciones para leer y guardar los alumnos en formato JSON.

import json


def cargar_alumnos():
    """Lee alumnos.json y devuelve un diccionario de alumnos."""
    try:
        with open("alumnos.json", "r", encoding="utf-8") as archivo:
            alumnos = json.load(archivo)

        if isinstance(alumnos, dict):
            return alumnos

        print("El archivo no tiene el formato esperado. Se iniciara vacio.")
        return {}

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        print("El archivo JSON esta vacio o tiene un formato incorrecto.")
        return {}


def guardar_alumnos(alumnos):
    """Guarda el diccionario completo en alumnos.json."""
    with open("alumnos.json", "w", encoding="utf-8") as archivo:
        json.dump(alumnos, archivo, ensure_ascii=False, indent=4)
