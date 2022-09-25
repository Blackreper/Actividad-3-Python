
while True:

    opc = input("\n\n1. Obtener tu signo Zodiacal.\n0. Salir\nOpcion:  ")
    if opc == "1":
        dia = int(input("Dia de Cumpleaños: "))
        mes = int(input("Mes en que naciste (en digitos): "))
        if(dia <= 31 and mes <= 12):

            if (dia >= 21 and mes == 1) or (dia <= 19 and mes == 2):
                print("\nTu signo es Acuario.\nRango:   21 de enero - 19 de febrero")
            if (dia >= 20 and mes == 2) or (dia <= 20 and mes == 3):
                print("\nTu signo es Piscis.\nRango:   20 de febrero - 20 de marzo")
            if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
                print("\nTu signo es Aries.\nRango:   21 de marzo - 20 de abril")
            if (dia >= 21 and mes == 4) or (dia <= 20 and mes == 5):
                print("\nTu signo es Tauro.\nRango:   21 de abril - 20 de mayo")
            if (dia >= 21 and mes == 5) or (dia <= 21 and mes == 6):
                print("\nTu signo es Geminis.\nRango:   21 de mayo - 21 de junio")
            if (dia >= 22 and mes == 6) or (dia <= 22 and mes == 7):
                print("\nTu signo es Cancer.\nRango:   22 de junio - 22 de julio")
            if (dia >= 23 and mes == 7) or (dia <= 23 and mes == 8):
                print("\nTu signo es Leo.\nRango:   23 de julio - 23 de agosto")
            if (dia >= 24 and mes == 8) or (dia <= 22 and mes == 9):
                print("\nTu signo es Virgo.\nRango:   24 de agosto - 22 de septiembre")
            if (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
                print("\nTu signo es Libra.\nRango:   23 de septiembre - 22 de octubre")
            if (dia >= 23 and mes == 10) or (dia <= 22 and mes == 11):
                print("\nTu signo es Escorpio.\nRango:   23 de octubre - 22 de noviembre")
            if (dia >= 23 and mes == 11) or (dia <= 21 and mes == 12):
                print("\nTu signo es Sagitario.\nRango:   23 de noviembre - 21 de diciembre")
            if (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
                print("\nTu signo es Capricornio.\nRango:   22 de diciembre - 20 de enero	")

        else: print("\nEsa fecha no esta disponible")

    if opc == "0":
        break