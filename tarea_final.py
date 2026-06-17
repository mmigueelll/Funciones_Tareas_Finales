import os, time, msvcrt
from pprint import pprint #SIRVE PARA IMPORTAR LA OPCION DE PODER IMPRIMIR EL DICCIONARIO ENTERO Y ORDENADO

def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Registrar reserva
2. Buscar reserva
3. Eliminar reserva
4. Actualizar confirmaciones
5. Mostrar reservas
6. Salir
7. Mostrar reservas confirmadas""")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese la opcion deseada (1-7): "))
            if opcion >= 1 and opcion <=7:
                return opcion
            else:
                print("Error, debe ingresar un número entre 1 y 7")
        except:
            print("Error, debe ingresar un número entero")

def validar_codigo_reserva(valor):
    if not valor[0].upper() == "R":
        print("Error: el código debe empezar con la letra R")
    elif len(valor) != 7:
        print("Error: el código debe tener exactamente 7 carácteres")
    elif " " in valor:
        print("Error: el código no debe contener espacios")
    else:
        return True
    
def validar_nombre_solicitante(valor):
    if len(valor) < 5:
        print("Error: el nombre debe tener al menos 5 carácteres")
    elif valor.isdigit():
        print("Error: el nombre no debe contener números")
    else:
        return True

def validar_tipo_sala(valor):
    if not valor[0].upper() in("P","M","G"):
        print("Error: debe ingresar una letra válida (P,M,G)")
    else:
        return True

def validar_cantidad_personas(valor):
    try:
        cantidad_personas = int(valor)
        if cantidad_personas < 2 or cantidad_personas > 20:
            print("Error: debe ingresar un número entre 2 y 20 (incluidos)")
        else:
            return True
    except:
        print("Error: debe ingresar la cantidad en números enteros")

def validar_horas_reserva(valor):
    try:
        horas_reserva = int(valor)
        if horas_reserva < 1 or horas_reserva > 8:
            print("Error: debe ingresar un número entre 1 y 8 (incluidos)")
        else:
            return True
    except:
        print("Error: debe ingresar la cantidad en números enteros")

def buscar_reserva(reservas:list, codigo_reserva):
    for posicion in range(len(reservas)):
        if reservas[posicion]["codigo_reserva"] == codigo_reserva:
            return posicion
    return -1

def agregar_reserva(reservas:list):
    while True:
        codigo_reserva = input("Ingrese el código de reserva: ")
        if not validar_codigo_reserva(codigo_reserva):
            continue
        if buscar_reserva(reservas, codigo_reserva) != -1:
            print("El código de reserva ya existe")
        else:
            break
    while True:
        nombre_solicitante = input("Ingrese el nombre del solicitante: ")
        if not validar_nombre_solicitante(nombre_solicitante):
            continue
        else:
            break
    while True:
        tipo_sala = input("Ingrese el tipo de sala (P,M,G): ")
        if not validar_tipo_sala(tipo_sala):
            continue
        else:
            tipo_sala = tipo_sala.upper()
            break
    while True:
        cantidad_personas = input("Ingrese la cantidad de personas: ")
        if not validar_cantidad_personas(cantidad_personas):
            continue
        else:
            cantidad_personas = int(cantidad_personas)
            break
    while True:
        horas_reserva = input("Ingrese las horas de reserva: ")
        if not validar_horas_reserva(horas_reserva):
            continue
        else:
            horas_reserva = int(horas_reserva)
            break
    reserva = {
        "codigo_reserva": codigo_reserva,
        "nombre_solicitante": nombre_solicitante,
        "tipo_sala": tipo_sala,
        "cantidad_personas": cantidad_personas,
        "horas_reserva": horas_reserva,
        "confirmada": False
    }
    reservas.append(reserva)
    print("Reserva agregada con éxito")

def eliminar_reserva(reservas:list, codigo_reserva):
    posicion = buscar_reserva(reservas, codigo_reserva)
    if posicion == -1:
        print("La reserva no existe")
    else:
        reservas.pop(posicion)
        print("Reserva eliminada con éxito")

def actualizar_confirmaciones(reservas:list):
    for reserva in reservas:
        if reserva["cantidad_personas"] >= 10:
            reserva["confirmada"] = True
        else:
            reserva["confirmada"] = False
    print("Todas las confirmaciones fueron actualizadas.")

def mostrar_reservas(reservas:list):
    for reserva in reservas:
        print("\n-------------------")
        print("Código reserva:", reserva["codigo_reserva"])
        print("Nombre solicitante:", reserva["nombre_solicitante"])
        print("Sala:", reserva["tipo_sala"])
        print("Cantidad personas:", reserva["cantidad_personas"])
        print("Cantidad horas:", reserva["horas_reserva"])
        print("Confirmación:", reserva["confirmada"])

def mostrar_reservas_confirmadas(reservas:list):
    confirmadas = False
    for reserva in reservas:
        if reserva["confirmada"] == True:
            print("\n-------------------")
            print("Código reserva:", reserva["codigo_reserva"])
            print("Nombre solicitante:", reserva["nombre_solicitante"])
            print("Sala:", reserva["tipo_sala"])
            print("Cantidad personas:", reserva["cantidad_personas"])
            print("Cantidad horas:", reserva["horas_reserva"])
            print("Confirmación:", reserva["confirmada"])
            confirmadas = True
    if not confirmadas:
        print("Aún no hay reservas confirmadas")

reservas = []
while True:
    os.system("cls")
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        os.system("cls")
        print("*** AGERGAR RESERVA ***")
        agregar_reserva(reservas)
    
    elif opcion == 2:
        os.system("cls")
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            print("*** BUSCAR RESERVA ***")
            codigo_reserva = input("Ingrese el codigo de reserva a buscar: ")
            posicion = buscar_reserva(reservas, codigo_reserva)
            if posicion == -1:
                print("La reserva no existe")
            else:
                print("Reserva encontrada en la posicion:","N°",posicion+1)
                pprint(reservas[posicion], indent=4) #IMPRIME LA RESERVA (DICCIONARIO) COMPLETA Y ORDENADA 
                print("\n. . . Presione una tecla para volver al menú principal . . .")
                msvcrt.getch()

    elif opcion == 3:
        os.system("cls")
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            print("*** ELIMINAR RESERVA ***")
            codigo_reserva = input("Ingrese el codigo de reserva a eliminar: ")
            eliminar_reserva(reservas, codigo_reserva)

    elif opcion == 4:
        os.system("cls")
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            actualizar_confirmaciones(reservas)
    
    elif opcion == 5:
        os.system("cls")
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            print("***       RESERVAS REALIZADAS       ***")
            mostrar_reservas(reservas)
            print("\n. . . Presione una tecla para volver al menú principal . . .")
            msvcrt.getch()
    
    elif opcion == 7:
        os.system("cls")
        if len(reservas) == 0:
            print("Aún no hay reservas")
        else:
            print("***       RESERVAS CONFIRMADAS       ***")
            mostrar_reservas_confirmadas(reservas)
            print("\n. . . Presione una tecla para volver al menú principal . . .")
            msvcrt.getch()
    else:
        print("Finalizando ejecución de programa, adiosito uvu")
        break
    print("\nEspere 2 segundos...")
    time.sleep(2)