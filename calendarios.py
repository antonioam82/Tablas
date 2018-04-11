from VALID import ns, OKI
import calendar
import subprocess

def AB(n):
    while n!=("A") and n!=("B"):
        n=input("Escriba solo \'A\' o \'B\' segun su opción: ")
    return n

def año_valido(n):
    while n<1 or n>9999:
        n=OKI(input("Introduzca un año valido: "))
    return n

def mes_valido(n):
     while n<1 or n>12:
         n=OKI(input("Introduzca un mes valido: "))
     return n


while True:
    print("CALENDARIOS")
    print("""Escoja una opción:
A)Ver los calendarios correspondientes a un determinado año
B)Ver el calendario correspondiente a un año y mes determinados
""")
    opcion=AB(input("Introduzca su opción: "))
    if opcion==("A"):
        año=año_valido(OKI(input("Introduce el año cuyos calendarios desea ver: ")))
        cl=calendar.TextCalendar()
        calendario=cl.formatyear(año)
        print("")
        print(calendario)
    else:
        año=año_valido(OKI(input("Introduzca el año: ")))
        mes=mes_valido(OKI(input("Introduzca mes: ")))
        cl=calendar.TextCalendar()
        calendario=cl.formatmonth(año,mes)
        print("")
        print(calendario)
    conti=ns(input("¿Desea continuar?: "))
    if conti==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])

