energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
cont_antiSpam = 0
costo_energia = 20
costo_tiempo = 2

nombre_agente = input("Ingrese el nombre del agente: ")

while not nombre_agente.isalpha():
    print("----- -----")
    nombre_agente = input("Ingrese un nombre de agente valido: ")

while True:
    print("----- -----")
    print("Menu de opciones")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    print("4. Fin")
    print("Estado del juego:")
    print(f"Energia: {energia} Tiempo: {tiempo} Cerraduras abiertas: {cerraduras_abiertas}")

    opcion = input("Elija una opcion del menu: ")

    while not opcion.isdigit():
        opcion = input("Elija una opcion valida del menu (1-4): ")

    opcion = int(opcion)

    if opcion == 1:
        cont_antiSpam += 1
    else:
        cont_antiSpam = 0
    
    match opcion:
        case 1:
            print("----- -----")
            print("Se elijio la opcion 1 Forzar cerradura")
            if cont_antiSpam == 3 :
                alarma = True
                print("Se elijio 3 veces seguidas la opcion de forzar cerradura")
                print("Se activo la alarma porque la cerradura se trabo")
                if tiempo <= 3 and cerraduras_abiertas < 3:
                    print("El sistema se bloqueo por bloqueo de alarma")
                    print("GAME OVER")
                    break
            elif energia < 40:
                print("Hay riesgo de alarma")
                riesgo_alarma = input("Ingrese un numero del 1 al 3: ")
                while not (riesgo_alarma.isdigit() or (int(riesgo_alarma) < 1 or int(riesgo_alarma) > 3)):
                    riesgo_alarma = input("Ingrese un valor valido (1-3): ")
                match riesgo_alarma:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        alarma = True
                        print("Se activo la alarma")
            elif not alarma:
                cerraduras_abiertas += 1
                print("Se abrio la cerradura")
                if cerraduras_abiertas == 3:
                    print("Se abrio la boveda")
                    print("VICTORIA")
                    print("Fin del juego")
                    break
            energia -= costo_energia
            tiempo -= costo_tiempo
            if energia <= 0 or tiempo <= 0:
                print(f"La energia es de {energia} y el tiempo es de {tiempo}")
                print("DERROTA")
                print("GAME OVER")
                break            
        case 2:
            print("----- -----")
            print("Se elijo la opcion 2 Hackear panel")
            for i in range(1, 5):
                print(f"Paso numero {i}")
                codigo = input("Ingrese una letra: ")
                while not (codigo.isalpha() and (len(codigo) == 1)):
                    codigo = input("Ingrese una letra y solo una: ")
                codigo_parcial += codigo
                print(f"El codigo parcial es el siguiente: {codigo_parcial}")
            if len(codigo_parcial) >= 8:
                cerraduras_abiertas += 1
                print("Se abrio una cerradura")
            energia -= 10
            tiempo -= 3
            if energia <= 0 or tiempo <= 0:
                print(f"La energia es de {energia} y el tiempo es de {tiempo}")
                print("DERROTA")
                print("Fin del juego")
                break  
        case 3:
            print("----- -----")
            print("Se elijio la opcion 3 Descansar")
            if energia == 85:
                energia = 100
            elif energia < 85:
                energia += 15
            else:
                (f"Su enrgia ya se encuentra al maximo {energia}")
            if alarma:
                energia -= 10
            tiempo -= 1
            if energia <= 0 or tiempo <= 0:
                print(f"La energia es de {energia} y el tiempo es de {tiempo}")
                print("DERROTA")
                print("Fin del juego")
                break  
        case 4: 
            print("----- -----")
            print("Se elijio la opcion 4")
            print("TERMINAR JUEGO")
            break
        case _:
            print("----- -----")
            print("se elijio una opcion invalida")