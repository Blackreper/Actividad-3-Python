
def AreaCuadrado(b:float, h:float):
    return b*h

def AreaTriangulo(b:float, h:float):
    return ((b*h)/2)

def AreaCirculo(r:float):
    return (3.1416*(r*r))


while True:
    opc = input("\n1. Area del cuadrado.\n2. Area del Triangulo\n3. Area del circulo\n0. Salir\n\nopc:  ")

    if (opc == '1') or (opc == '2'):
        b = float(input("\nIngresar base y altura.\nBase: "))
        h = float(input("Altura: "))
        if opc == '1': print("Area Cuadrado: ",AreaCuadrado(b,h))
        else: print("Area Triangulo: ",AreaTriangulo(b,h))
    if opc == '3': 
        r = float(input("\nIngresar el radio del circulo: "))
        print("Area circulo: ",AreaCirculo(r))
    if opc == '0':
        break