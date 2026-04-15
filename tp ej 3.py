nombre_operador = input("Ingrese su nombre: ")

while not nombre_operador.isalpha():
    nombre_operador = input("Ingrese su nombre correctamente: ")

nombre_paciente = ""
#turnos_pacientes = ""
#turnos_dias = ""
turnos_lunes = ""
turnos_martes = ""
cont_lunes = 0
cont_martes = 0

while True:

    print("----------")
    print("Menu de opciones")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    opcion = input("Elija una opcion: ")

    while not opcion.isdigit():
        print("----------")
        print("Menu de opciones")
        print("1. Reservar turno")
        print("2. Cancelar turno")
        print("3. Ver agenda del dia")
        print("4. Ver resumen general")
        print("5. Cerrar sistema")
        print("Elija una opcion correcta: ")
        opcion = input()

    opcion = int(opcion)

    #while not (opcion >= 1 and opcion <= 5):
        #print("--- OPCION INVALIDA ---")
        #print("Menu de opciones")
        #print("1. Reservar turno")
        #print("2. Cancelar turno")
        #print("3. Ver agenda del dia")
        #print("4. Ver resumen general")
        #print("5. Cerrar sistema")
        #opcion = int(input("Elija una opcion correcta (1-5): "))

    match opcion:
        case 1:
            print("----------")
            print("Opcion elejida: Reservar turno")
            nombre_paciente = input("Ingrese el nombre del paciente: ")
            while not nombre_paciente.isalpha():
                nombre_paciente = input("Ingrese un nombre de paciente valido: ")
            print("Ingrese 1 para elejir Lunes")
            print("Ingrese 2 para elejir Martes")
            dia_elejido = input("Elija el dia del turno a reservar: ")

            while not dia_elejido.isdigit():
                print("----------")
                print("Ingrese 1 para elejir Lunes")
                print("Ingrese 2 para elejir Martes")
                print("Ingrese una opcion valida (1/2): ")
                dia_elejido = input()

            while int(dia_elejido) != 1 and int(dia_elejido) != 2:
                print("----------")
                print("Ingrese un valor valido")
                print("Ingrese 1 para elejir Lunes")
                print("Ingrese 2 para elejir Martes")
                dia_elejido = input()
            if int(dia_elejido) == 1:
                if cont_lunes == 4:
                    print("No hay mas cupos para reservar otro turno para el lunes")
                elif nombre_paciente in turnos_lunes:
                    print(f"El paciente {nombre_paciente} ya tiene un turno reservado para el dia lunes")
                else:
                    print(f"Se reservo su turno para el dia Lunes")
                    turnos_lunes += nombre_paciente + " "
                    cont_lunes += 1
            else:
                if cont_martes == 3:
                    print("No hay mas cupos para reservar otro turno para el martes")
                elif nombre_paciente in turnos_martes:
                    print(f"El paciente {nombre_paciente} ya tiene un turno reservado para el dia martes")
                else:
                    print(f"Se reservo su turno para el dia Martes")
                    turnos_martes += nombre_paciente + " "
                    cont_martes += 1
        case 2:
            print("----------")
            print("Opcion elejida: Cancelar turno")
            #dia = input("Ingrese el dia del turno a cancelar: (lunes o martes)")
            nombre_paciente = input("Ingrese el nombre del paciente: ")
            while not nombre_paciente.isalpha():
                nombre_paciente =("Ingrese un nombre de paciente valido: ")
            if nombre_paciente in turnos_lunes:
                turnos_lunes.replace(nombre_paciente, "")
                print(f"Se cancelo el turno del paciente {nombre_paciente} del dia lunes")
            elif nombre_paciente in turnos_martes:
                turnos_martes.replace(nombre_paciente, "")
                print(f"Se cancelo el turno del paciente {nombre_paciente} del dia martes")
            else:
                print(f"El paciente {nombre_paciente} no tiene un numero reservado")


        case 3:
            print("----------")
            print("Opcion elejida: Ver agenda del dia")
            print(f"Agenda del dia lunes: {turnos_lunes}")
            print("Turnos maximos para los lunes es de 4")
            print(f"Agenda del dia martes: {turnos_martes}")
            print("Turnos maximos para los martes es de 3")
        case 4:
            print("----------")
            print("Opcion elejida: Ver resumen general")
            print(f"Los turnos del dia lunes son: {turnos_lunes}")
            print(f"Los turnos del dia martes son: {turnos_martes}")
            if cont_lunes > cont_martes:
                print(f"Esta semana hay mas turnos el dia lunes ({cont_lunes})")
            elif cont_lunes < cont_martes:
                print(f"Esta semana hay mas turnos el dia martes ({cont_martes})")
            else:
                print(f"Esta semana hay la misma cantidad de turnos para los dias lunes y martes ({cont_lunes})")
        case 5:
            print("----------")
            print("Opcion elejida: Cerrar sistema")
            break
        case _:
            print("----------")
            print("Opcion incorrecta")

#no funciona la opcion de cancelar turno