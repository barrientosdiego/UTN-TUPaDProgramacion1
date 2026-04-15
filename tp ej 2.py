usuario_correcto = "alumno"
clave_correcta = "phyton123"

usuario_ingresado = input("Ingrese su usuario: ")
intentos = 1

while intentos < 3 and usuario_ingresado != usuario_correcto:
    intentos += 1
    usuario_ingresado = input("Ingrese un usuario valido: ")

if usuario_ingresado == usuario_correcto:
    clave_ingresada = input("Ingrese su clave: ")
    while intentos < 3 and clave_ingresada != clave_correcta:
        intentos += 1
        clave_ingresada = input("Ingrese una clave valida: ")

if intentos == 3:
            input("Cuenta bloqueada.")

if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
    print(" 1. Estado 2. Cambiar clave 3. Mensaje 4. Salir")
    opcion_elejida = input("Ingrese una opcion: ")
    while not opcion_elejida.isdigit() or not ( int(opcion_elejida) >= 1 and int(opcion_elejida) <= 4 ):
            opcion_elejida = input("Ingrese una opcion valida (del 1 al 4): ")
    if int(opcion_elejida) == 1:
            input("Inscripto. ")
    if int(opcion_elejida) == 2:
            nueva_contrasenia = input("Ingrese una nueva contrasenia (minimo 6 caracteres): ")
            while len(nueva_contrasenia) < 6:
                nueva_contrasenia = input("Ingrese una nueva contrasenia valida (minimo 6 caracteres): ")
            confirmar_contrasenia = input("Confirme su contrasenia: ")
            while nueva_contrasenia != confirmar_contrasenia:
                confirmar_contrasenia = input(f"Por favor confirme su contrasenia correctamente ({nueva_contrasenia}): ")
            if nueva_contrasenia == confirmar_contrasenia:
                input("Se cambio la contrasenia exitosamente. ")
    if int(opcion_elejida) == 3:
            input("Frase motivacional. ")
    if int(opcion_elejida) == 4:
            input("Fin. ")
