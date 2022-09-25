from os import system

limite = 16
n = 0
e = 0

def factorial(n):
    i = 1
    num = 1
    while i <= n:
        num *= i
        i += 1
    return num

while n < limite:
	e += 1/factorial(n) # se llama a la función factorial creada por ti
	n = n + 1

print("\n\n   Limite = ",limite,"\n   Exponencial: ",e,"\n\n")
system("pause")