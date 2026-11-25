# Programa principal: muestra el menu y coordina las funciones.

from archivos import cargar_alumnos, guardar_alumnos
from procesamientos import (registrar_alumno,listar_alumnos,buscar_alumno,
modificar_alumno,eliminar_alumno,mostrar_estadisticas)


def mostrar_menu():
    print("\n========== GESTION DE ALUMNOS ==========")
    print("1. Registrar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Ver estadisticas")
    print("7. Salir")


def main():
    alumnos = cargar_alumnos()
    opcion = ""

    while opcion != "7":
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            cambio = registrar_alumno(alumnos)
            if cambio:
                guardar_alumnos(alumnos)

        elif opcion == "2":
            listar_alumnos(alumnos)

        elif opcion == "3":
            buscar_alumno(alumnos)

        elif opcion == "4":
            cambio = modificar_alumno(alumnos)
            if cambio:
                guardar_alumnos(alumnos)

        elif opcion == "5":
            cambio = eliminar_alumno(alumnos)
            if cambio:
                guardar_alumnos(alumnos)

        elif opcion == "6":
            mostrar_estadisticas(alumnos)

        elif opcion == "7":
            print("Programa finalizado.")

        else:
            print("Opcion incorrecta. Seleccione una opcion del 1 al 7.")


if __name__ == "__main__":
    main()
