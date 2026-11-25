# Funciones para validar los datos que ingresa el usuario.

# Esta funcion comprueba que el DNI tenga solamente numeros
# y que no se encuentre registrado en el diccionario de alumnos.
def validar_dni(dni, alumnos):
    """Comprueba que el DNI tenga solo numeros y no este registrado."""

    # isdigit() verifica que todos los caracteres sean numeros.
    if not dni.isdigit():
        return False

    # Comprueba si el DNI ya existe como clave del diccionario.
    if dni in alumnos:
        return False

    # Si supera las dos comprobaciones, el DNI es valido.
    return True


# Esta funcion comprueba que el nombre o apellido
# contenga solamente letras y espacios.
def validar_nombre(texto):
    """Comprueba que un nombre o apellido contenga letras y espacios."""

    # strip() elimina los espacios al principio y al final.
    texto = texto.strip()

    # len() comprueba que el texto no este vacio.
    if len(texto) == 0:
        return False

    # Recorremos cada caracter del texto.
    for caracter in texto:

        # isalpha() comprueba si es una letra.
        # Tambien permitimos que el caracter sea un espacio.
        if not (caracter.isalpha() or caracter == " "):
            return False

    # Si todos los caracteres son correctos, devuelve True.
    return True


# Esta funcion comprueba que la edad sea un numero entero
# mayor o igual a cero.
def validar_edad(edad):
    """Comprueba que la edad sea un numero entero no negativo."""

    try:
        # Convertimos el dato ingresado a entero.
        edad = int(edad)

        # Comprueba que la edad sea mayor o igual a cero.
        return edad >= 0

    # Si no se puede convertir a entero, devuelve False.
    except ValueError:
        return False


# Esta funcion comprueba que la nota sea un numero
# comprendido entre 0 y 10.
def validar_nota(nota):
    """Comprueba que la nota sea un numero entre 0 y 10."""

    try:
        # Convertimos el dato ingresado a numero decimal.
        nota = float(nota)

        # Comprueba que la nota este dentro del rango permitido.
        return 0 <= nota <= 10

    # Si no se puede convertir a numero, devuelve False.
    except ValueError:
        return False


# Esta funcion solicita un DNI y vuelve a pedirlo
# mientras no sea valido o ya se encuentre registrado.
def solicitar_dni_nuevo(alumnos):

    # input() solicita el DNI y strip() elimina espacios externos.
    dni = input("Ingrese el DNI: ").strip()

    # Mientras el DNI no sea valido, seguimos solicitandolo.
    while not validar_dni(dni, alumnos):
        print("DNI invalido o ya registrado. Intente nuevamente.")
        dni = input("Ingrese el DNI: ").strip()

    # Cuando el DNI es valido, lo devuelve.
    return dni


# Esta funcion solicita un nombre o apellido
# y repite la solicitud hasta recibir un texto valido.
def solicitar_texto(mensaje):

    texto = input(mensaje).strip()

    # Mientras el texto no sea valido, vuelve a solicitarlo.
    while not validar_nombre(texto):
        print("Ingrese solamente letras y espacios.")
        texto = input(mensaje).strip()

    return texto


# Esta funcion solicita la edad del alumno
# hasta que se ingrese un numero entero no negativo.
def solicitar_edad():

    edad = input("Ingrese la edad: ").strip()

    # Comprueba la edad utilizando la funcion de validacion.
    while not validar_edad(edad):
        print("La edad debe ser un numero entero mayor o igual a cero.")
        edad = input("Ingrese la edad: ").strip()

    # Devuelve la edad convertida a entero.
    return int(edad)


# Esta funcion solicita la nota final del alumno
# hasta que se ingrese un numero entre 0 y 10.
def solicitar_nota():

    nota = input("Ingrese la nota final (0 a 10): ").strip()

    # Mientras la nota no sea valida, vuelve a solicitarla.
    while not validar_nota(nota):
        print("La nota debe ser un numero entre 0 y 10.")
        nota = input("Ingrese la nota final (0 a 10): ").strip()

    # Devuelve la nota convertida a numero decimal.
    return float(nota)