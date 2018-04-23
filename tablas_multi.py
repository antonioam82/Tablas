from VALID import OK, ns
import subprocess

while True:
    print("TABLAS DE MULTIPLICAR")
    numero=OK(input("Dame el número: "))

    for i in range(0,11):
        resul=i*numero
        print(("%d x %d = %d")%(numero,i,resul))

    conti=ns(input("¿Desea continuar?: "))
    if conti==("s"):
        subprocess.call(["cmd.exe","/C","cls"])
        continue
    break

