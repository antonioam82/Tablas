import subprocess
from VALID import OK, OKI, ns, ER

def AB(md):
    while md!=("A") and md!=("B"):
        md=input("Escriba solo \'A\' o \'B\' según su opción: ")
    return md

while True:
    n=OKI(input("Primer número: "))
    n2=OKI(input("Segundo número: "))
    o=[n,n2]
    o.sort()
    preg=ns(input("¿Desea ver la secuencia de sumas?: "))
    if preg==("s"):
        md=AB(input("Modo de presentacion en columna (\'A\')o en lista (\'B\'): "))
    summ=0
    li=[]
    for i in range(o[0],(o[1])+1):
        summ+=i
        if preg==("s") and md==("A"):
            print(summ)
        else:
            li.append(summ)
    if preg==("s") and md==("B"):
        print(li)
        print("")
    print("El sumatorio entre",o[0],"y",o[1],"es",summ,ER(summ),chr(7))

    c=ns(input("¿Continuar con otro sumatorio?: "))
    if c==("n"):
        break
    subprocess.call(["cmd.exe","/C","cls"])
