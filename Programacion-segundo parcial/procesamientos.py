# Funciones principales para administrar y procesar los alumnos.

# Importamos las funciones que solicitan y validan los datos.
from validaciones import (solicitar_dni_nuevo,solicitar_texto,solicitar_edad,solicitar_nota)


def registrar_alumno(alumnos):
    # Muestra el título de la operación.
    print("\n--- REGISTRAR ALUMNO ---")

    # Solicitamos el DNI y comprobamos que sea válido y no esté registrado.
    dni = solicitar_dni_nuevo(alumnos)

    # Solicitamos y validamos los datos personales del alumno.
    nombre = solicitar_texto("Ingrese el nombre: ")
    apellido = solicitar_texto("Ingrese el apellido: ")
    edad = solicitar_edad()
    nota = solicitar_nota()

    # Creamos un diccionario interno con todos los datos del alumno.
    alumno = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota
    }

    # Guardamos el alumno en el diccionario principal.
    # El DNI funciona como clave y el diccionario del alumno como valor.
    alumnos[dni] = alumno

    print("Alumno registrado correctamente.")

    # Indicamos que el registro se realizó correctamente.
    return True


def listar_alumnos(alumnos):
    print("\n--- LISTADO DE ALUMNOS ---")

    # Comprobamos si el diccionario está vacío.
    if len(alumnos) == 0:
        print("No hay alumnos registrados.")
        return

    # Recorremos el diccionario obteniendo la clave (DNI)
    # y el valor (diccionario con los datos del alumno).
    for dni, alumno in alumnos.items():
        print("-------------------------")

        # Mostramos los datos de cada alumno.
        print("DNI:", alumno["dni"])
        print("Nombre:", alumno["nombre"])
        print("Apellido:", alumno["apellido"])
        print("Edad:", alumno["edad"])
        print("Nota:", alumno["nota"])


def buscar_alumno(alumnos):
    print("\n--- BUSCAR ALUMNO ---")

    # Solicitamos el DNI y eliminamos espacios al principio y al final.
    dni = input("Ingrese el DNI que desea buscar: ").strip()

    # Comprobamos si el DNI existe como clave del diccionario.
    if dni in alumnos:

        # Guardamos el diccionario interno del alumno encontrado.
        alumno = alumnos[dni]

        # Mostramos sus datos.
        print("DNI:", alumno["dni"])
        print("Nombre:", alumno["nombre"])
        print("Apellido:", alumno["apellido"])
        print("Edad:", alumno["edad"])
        print("Nota:", alumno["nota"])

    else:
        print("No se encontro un alumno con ese DNI.")


def modificar_alumno(alumnos):
    print("\n--- MODIFICAR ALUMNO ---")

    # Solicitamos el DNI del alumno que queremos modificar.
    dni = input("Ingrese el DNI del alumno que desea modificar: ").strip()

    # Si el DNI no existe, informamos y terminamos la función.
    if dni not in alumnos:
        print("No se encontro un alumno con ese DNI.")
        return False

    # Obtenemos el diccionario interno del alumno.
    alumno = alumnos[dni]

    # Indicamos que dejar un campo vacío conserva el dato actual.
    print("Deje el campo vacio si desea conservar el dato actual.")

    # Solicitamos un nuevo nombre mostrando el actual entre paréntesis.
    nombre = input("Nombre (" + alumno["nombre"] + "): ").strip()

    # Si el usuario ingresó algo, comprobamos que sean letras y espacios.
    if nombre != "":
        while not nombre.replace(" ", "").isalpha():
            print("Ingrese solamente letras y espacios.")
            nombre = input("Nombre: ").strip()

        # Si pasó la validación, actualizamos el nombre.
        alumno["nombre"] = nombre

    # Solicitamos un nuevo apellido.
    apellido = input("Apellido (" + alumno["apellido"] + "): ").strip()

    # Si no dejó el campo vacío, validamos el apellido.
    if apellido != "":
        while not apellido.replace(" ", "").isalpha():
            print("Ingrese solamente letras y espacios.")
            apellido = input("Apellido: ").strip()

        # Actualizamos el apellido.
        alumno["apellido"] = apellido

    # Solicitamos una nueva edad.
    # str() convierte el valor numérico actual en texto para mostrarlo.
    edad = input("Edad (" + str(alumno["edad"]) + "): ").strip()

    # Si ingresó una edad, comprobamos que esté formada por dígitos.
    if edad != "":
        while not edad.isdigit():
            print("La edad debe ser un entero mayor o igual a cero.")
            edad = input("Edad: ").strip()

        # Convertimos la edad validada de texto a entero.
        alumno["edad"] = int(edad)

    # Solicitamos una nueva nota mostrando la nota actual.
    nota = input("Nota (" + str(alumno["nota"]) + "): ").strip()

    # Si el campo no está vacío, comenzamos a validar la nota.
    if nota != "":
        nota_valida = False

        # Repetimos hasta que la nota sea válida.
        while not nota_valida:
            try:
                # Convertimos el texto ingresado a número decimal.
                nota_numero = float(nota)

                # Comprobamos que esté dentro del rango permitido.
                if 0 <= nota_numero <= 10:
                    nota_valida = True
                else:
                    print("La nota debe estar entre 0 y 10.")
                    nota = input("Nota: ").strip()

            # Evitamos que el programa se interrumpa si ingresa letras.
            except ValueError:
                print("Ingrese un numero valido.")
                nota = input("Nota: ").strip()

        # Guardamos la nota cuando ya fue validada.
        alumno["nota"] = nota_numero

    print("Datos modificados correctamente.")

    # Indicamos que la modificación se realizó correctamente.
    return True


def eliminar_alumno(alumnos):
    print("\n--- ELIMINAR ALUMNO ---")

    # Solicitamos el DNI del alumno que se desea eliminar.
    dni = input("Ingrese el DNI del alumno que desea eliminar: ").strip()

    # Comprobamos que el DNI exista en el diccionario.
    if dni in alumnos:

        # Solicitamos confirmación y convertimos la respuesta a minúscula.
        confirmacion = input("Confirma la eliminacion? (s/n): ").strip().lower()

        # Si confirma con la letra s, eliminamos el registro.
        if confirmacion == "s":
            del alumnos[dni]
            print("Alumno eliminado correctamente.")
            return True

        else:
            # Si no confirma, no modificamos el diccionario.
            print("Operacion cancelada.")
            return False

    # Si el DNI no existe, informamos que no encontramos al alumno.
    print("No se encontro un alumno con ese DNI.")
    return False


def mostrar_estadisticas(alumnos):
    print("\n--- ESTADISTICAS ---")

    # Obtenemos la cantidad de alumnos registrados.
    cantidad = len(alumnos)
    print("Cantidad total de alumnos:", cantidad)

    # Si no hay alumnos, no podemos calcular estadísticas.
    if cantidad == 0:
        print("No hay datos para calcular estadisticas.")
        return

    # Inicializamos las variables que utilizaremos en los cálculos.
    suma_notas = 0
    aprobados = 0
    desaprobados = 0

    # Empezamos en -1 para poder comparar correctamente
    # con cualquier nota válida, que va de 0 a 10.
    mayor_nota = -1

    # Esta variable guardará el diccionario del alumno con mayor nota.
    mejor_alumno = None

    # Recorremos los diccionarios internos de todos los alumnos.
    for alumno in alumnos.values():

        # Obtenemos la nota del alumno actual.
        nota = alumno["nota"]

        # Acumulamos las notas para calcular el promedio general.
        suma_notas += nota

        # Clasificamos al alumno según su nota.
        if nota >= 6:
            aprobados += 1
        else:
            desaprobados += 1

        # Comparamos la nota actual con la mayor encontrada hasta ahora.
        if nota > mayor_nota:
            mayor_nota = nota

            # Guardamos al alumno que tiene la mayor nota.
            mejor_alumno = alumno

    # Calculamos el promedio general de todas las notas.
    promedio = suma_notas / cantidad

    # Mostramos los resultados.
    # round() redondea el promedio a dos decimales.
    print("Promedio de notas:", round(promedio, 2))
    print("Alumno con mayor nota:", mejor_alumno["nombre"], mejor_alumno["apellido"])
    print("Mayor nota:", mayor_nota)
    print("Cantidad de aprobados:", aprobados)
    print("Cantidad de desaprobados:", desaprobados)
