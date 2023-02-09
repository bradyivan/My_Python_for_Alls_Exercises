
def celsius2Farenheit():
    celsius = float(input("introdusca la temperatura en grados Celsius: "))
    out = "Temperatura en grados Farenheit: {} F."
    return out.format(celsius*1.8 +32)

def farenheit2Celsius():
    farenheit = float(input("introdusca la temperatura en grados Farenheit: "))
    out = "Temperatura en grados Celsius: {} F."
    return out.format((farenheit -32)*0.5556)

def calcSalario():
    horas = float(input("Introduzca horas: "))
    tarifa = float(input("Introduzca tarifa: "))
    txt = "Salario: {}"
    return txt.format(horas*tarifa)

def helloPeople():
    nombre = input("Introduzca tu nombre: ")
    txt = "\nOpcion 1-Hola:\n Hola, {}"
    return txt.format(nombre)
    #return "Hola\n, "+ nombre

while True:
    print("""____________________________________________________________
    Escoja una opcion:
    --------------------------------------------------------
    1-Hola. 
    2-Celsius to Farenheit.
    3-Farenheit to Celsius.
    4-Calculo del Salario (Salario = horas*tarifa) 
    5-Salir.
_____________________________________________________________""")
    opcion=input()
    if (opcion == "1"):
        print(helloPeople())

    elif (opcion == "2"):
        print(celsius2Farenheit())
        
    elif (opcion == "3"):
        print(farenheit2Celsius())

    elif (opcion == "4"):
        print(calcSalario())
        
    elif (opcion == "5"):
        break
    else:
        print("""
        Wrong option. Try Again
        """)


