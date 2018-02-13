from math import log
from VALID import OK, ns
import subprocess

def AB(m):
    while m!=("A") and m!=("B"):
        m=input("Introduzca solo \'A\' o \'B\' según su opción: ")
    return m

def ran_val(n):
    rang=n.split(",")#SEPARAMOS "nums" MEDIANTE COMA
    while len(rang)!=2 or(int(rang[0])<1 or int(rang[1])<1):
        rang=ran_val(input(str("Rango no válido: ")))
    return rang

def op_val(b):
    if b!=("e"):
        try:
            b=int(b)
            if b<=1:
                b=op_val(input("La base ha de ser mayor de 1: "))
        except:
            b=op_val(input("introduce un valor numérico: "))
    return b

while True:
    print("TABLA DE LOGARITMOS")
    print("¿QUE METODO DESEA?")
    print("A)Metodo \'LISTA\'")
    print("B)Metodo \'RANGO\'")
    met=AB(input("Introduzca aquí su opción: "))
    B=op_val(input("Introduzca base: "))
    if met==("A"):
        x=1.0
        top=OK(input("¿Hasta que numero quiere la tabla?: "))
        #print("NUMERO",  "LOG BASE ",B)
        while x<=top:
            if B==("e"):
                print(x, '\t', log(x))
            else:
                print(x, '\t', log(x)/log(B))

            x=x+1.0 #LO MISMO QUE x+=1.0
    else: #met==("B")
        nums=ran_val(input(str("Introduzca rango separado por coma: ")))
        nums=[int(nums[0]),int(nums[1])]#PASAMOS LOS ELEMENTOS DE LA LISTA A ENTEROS
        nums.sort() #ORDENAR LOS NÚMEROS DEL RANGO 
        print(nums)
        for i in range(nums[0],nums[1]+1):
            if B==("e"):
                print(i, '\t', log(i))
            else:
                print(i, '\t', log(i)/log(B))
                
    conti=ns(input("¿Crear nueva tabla?: "))
    if conti==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])
