import os, time, msvcrt

def mostrar_menu():
    print("""=== MENÚ PRINCIPAL ===
1. Registrar préstamo
2. Buscar préstamo
3. Eliminar préstamo
4. Actualizar seguimiento
5. Mostrar préstamos
6. Salir""")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese la opción que desee (1-6): "))
            if 1 <= opc <= 6:
                return opc
            else:
                print("Error: debe ingresar un número entre 1 y 6")
        except:
            print("Error: Debe ingresar un número entero")

def validar_codigo_prestamo(valor,lista):
    if len(valor) != 6:
        return False, "Error: el código debe tener exactamente 6 caracteres"
    elif valor[0].upper() != "P":
        return False, "Error: el código debe empezar con la letra P"
    elif " " in valor:
        return False, "Error: el código no debe contener espacios"
    for prestamo in lista:
        if prestamo["codigo_prestamo"] == valor.upper():
            return False, "Error: el código ya existe, intente con otro"
    else:
        return True, ""

def validar_titulo_libro(valor):
    if len(valor) != 5:
        return False, "Error: el titulo debe tener exactamente 5 caracteres"
    elif valor.isdigit():
        return False, "Error: el titulo no debe estar conformado únicamente por números"
    else:
        return True, ""
    
def validar_categoria(valor):
    if valor.upper() not in("A","L","C"):
        return False, "Error: la categoría debe ser A, L o C"
    else:
        return True, ""

def validar_dias_prestamo(valor):
    try:
        valor = int(valor)
        if 1 <= valor <= 30:
            return True, ""
        else:
            return False, "Error: la cantidad debe ser un número entre 1 y 30"
    except:
        return False, "Error: debe ingresar un número entero"

def validar_multa_pendiente(valor):
    try:
        valor = int(valor)
        if valor >= 0:
            return True, ""
        else:
            return False, "Error: la cantidad debe ser un número mayor o igual a 0"
    except:
        return False, "Error: debe ingresar un número entero"

def registrar_prestamo(lista):
    while True:
        codigo_prestamo = input("Ingrese código préstamo: ")
        validar,mensajito = validar_codigo_prestamo(codigo_prestamo,lista)
        if validar == False:
            print(mensajito)
        else:
            break
    while True:
        titulo_libro = input("Ingrese titulo: ")
        validar,mensajito = validar_titulo_libro(titulo_libro)
        if validar == False:
            print(mensajito)
        else:
            break
    while True:
        categoria = input("Ingrese categoría (A,L,C): ")
        validar,mensajito = validar_categoria(categoria)
        if validar == False:
            print(mensajito)
        else:
            break
    while True:
        dias_prestamo = input("Ingrese dias: ")
        validar,mensajito = validar_dias_prestamo(dias_prestamo)
        if validar == False:
            print(mensajito)
        else:
            break
    while True:
        multa_pendiente = input("Ingrese multa pendiente (si no tiene ingrese 0): ")
        validar,mensajito = validar_multa_pendiente(multa_pendiente)
        if validar == False:
            print(mensajito)
        else:
            break
    prestamo = {
        "codigo_prestamo": codigo_prestamo.title(),
        "titulo_libro": titulo_libro,
        "categoria": categoria.upper(),
        "dias_prestamo": int(dias_prestamo),
        "multa_pendiente": int(multa_pendiente),
        "seguimiento": False
    }
    prestamos.append(prestamo)
    print("El prestamo fue registrado correctamente")

def buscar_prestamo(valor,prestamos):
    for posicion,prestamo in enumerate(prestamos,1):
        if prestamo["codigo_prestamo"] == valor:
            return posicion
    return -1

def eliminar_prestamo(valor,prestamos):
    for prestamo in prestamos:
        if prestamo["codigo_prestamo"] == valor:
            prestamos.remove(prestamo)
            return True, "Préstamo eliminado correctamente"
    return False, "Error: el prestamo no existe o ya fue eliminado"

def actualizar_seguimiento(prestamos):
    for prestamo in prestamos:
        if prestamo["multa_pendiente"] >= 5000:
            prestamo["seguimiento"] = True
        else:
            prestamo["seguimiento"] = False
    return

def mostrar_prestamos(prestamos):
    for prestamo in prestamos:
        print("\n---------------------------------")
        print("Código préstamo:", prestamo["codigo_prestamo"])
        print("Título libro:", prestamo["titulo_libro"])
        print("Categoría:", prestamo["categoria"])
        print("Días préstamo:", prestamo["dias_prestamo"])
        print("Multa pendiente:", prestamo["multa_pendiente"], "pesos chilenos")
        print("Seguimiento:", prestamo["seguimiento"])

prestamos = []
while True:
    os.system("cls")
    mostrar_menu()
    opcion = validar_opcion()
    
    if opcion == 1:
        registrar_prestamo(prestamos)
        
    elif opcion == 2:
        if len(prestamos) == 0:
            print("Aún no hay prestamos registrados")
        else:
            codigo_prestamo = input("ingrese código a buscar: ").title()
            posicion = buscar_prestamo(codigo_prestamo,prestamos)
            if posicion == -1:
                print("El préstamo no existe")
            else:
                print("La posición del prestamo es: N°",posicion)
    
    elif opcion == 3:
        if len(prestamos) == 0:
            print("Aún no hay prestamos registrados")
        else:
            codigo_prestamo = input("ingrese código a eliminar: ").title()
            validar,mensajito = eliminar_prestamo(codigo_prestamo,prestamos)
            print(mensajito)
    
    elif opcion == 4:
        if len(prestamos) == 0:
            print("Aún no hay prestamos registrados")
        else:
            actualizar_seguimiento(prestamos)
            print("Se han actualizado todos los prestamos")
    
    elif opcion == 5:
        if len(prestamos) == 0:
            print("Aún no hay prestamos registrados")
        else:
            mostrar_prestamos(prestamos)
            print("\n. . . Presione una tecla para volver al menú principal . . .")
            msvcrt.getch()
            print("Espere 2 segundos...")

    else:
        print("Adiosito uvu")
        break
    time.sleep(2)