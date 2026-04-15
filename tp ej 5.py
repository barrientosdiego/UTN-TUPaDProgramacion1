print("--- BIENVENIDO A LA ARENA ---")
nombre_gladiador = input("Ingrese el nombre del gladiador: ")

while not nombre_gladiador:
    print("Error solo se permiten letras")
    nombre_gladiador = input("Ingrese un nombre de gladiador valido: ")

vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
danio_base = 15
danio_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")

while True:
    print(f"Vida del gladiador {nombre_gladiador}: ({vida_gladiador})")
    print(f"Vida enemigo ({vida_enemigo})")
    print(f"Posiones de vida: {pociones_vida}")
    print("Elejir accion:")
    print("1. Ataque pesado")
    print("2. Rafaga veloz")
    print("3. Curar")

    opcion = input("opcion: ")
    while not (opcion.isdigit() and ( int(opcion) >= 1 and int(opcion) <= 3 )):
        opcion = input("Elija una opcion valida (1-3): ")

    opcion = int(opcion)

    match opcion:
        case 1:
            if vida_enemigo < 20:
                vida_enemigo -= float(danio_base * 1.5)
                print(f"Atacaste al enemigo por {float(danio_base * 1.5)} puntos de danio")
            else:
                vida_enemigo -= danio_base
                print(f"Atacaste al enemigo {danio_base} puntos de danio")
            turno_gladiador = False
        case 2:
            for i in range(1, 4):
                vida_enemigo -= 5
                print("Golpe conectado por 5 de danio")
            turno_gladiador = False
        case 3:
            if pociones_vida > 0:
                vida_gladiador += 30
                pociones_vida -= 1
            else:
                print("No quedan pociones de vida")
            turno_gladiador = False
    if not turno_gladiador:
        if vida_enemigo > 0:    
            print("Turno del enemigo")
            vida_gladiador -= danio_enemigo
            print("¡El enemigo te ataco por 12 punto de danio")
            turno_gladiador = True
            print("=== NUEVO TURNO ===")
    if vida_gladiador > 0 and vida_enemigo <= 0:
        print(F"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
        break
    elif vida_enemigo > 0 and vida_gladiador <= 0:
        print("¡DERROTA!. Has caido en combate.")
        break