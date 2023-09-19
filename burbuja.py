import os
import time 

# usar el append para guardar elementos en un arreglo 

def llenar():   #funcion para llenar el arreglo

    tamArreglo:int =int(input("ingrese el numero del elementos a ordenar: "))
    arreglo:int=[]
    for i in range(0,tamArreglo):
        arreglo.append(int(input("numero "+str(i+1)+": ")))


    return arreglo


def burbuja(arreglo):
    inicio= time.time()
    print("****** METODO BURBUJA ********")
    aux:int = 0
    for i in range(0,len(arreglo)-1):
        for j in range(0,len(arreglo)-1):
            if arreglo[j] > arreglo [j+1]:
                aux=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]= aux

    print(arreglo)
    fin= time.time()
    tiempo_ejecutado = fin-inicio
    return tiempo_ejecutado



def burbujaOptimizada(arreglo):
    inicio= time.time()
    print("****** METODO BURBUJA OPTIMIZADA ********")
    bandera:int = 1
    aux: int = 0
    n: int = len(arreglo)

    for paso in range(0,n-1):
        bandera = 0
        for j in range(0,n-paso-1):
            if arreglo[j] > arreglo [j+1]:
                bandera = 1
                aux = arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]=aux
        if bandera ==0:
            break

    print(arreglo)
    fin= time.time()
    tiempo_ejecutado = fin-inicio
    return tiempo_ejecutado

def mostrarMenu():
    opcionmenu = 1
    while opcionmenu !=4: 
        os.system ("cls")
        print("****************** ORDENAMIENTO *******************")

        print(" 1)...............  burbuja  ")
        print(" 2)...............  burbuja optimizada  ")
        print(" 3)............... ambos  ")
        print(" 4)............... salir  ")
        
        opcionmenu=int(input("escoja una opcion: "))
        if opcionmenu ==1:
            numeros = llenar()
            #burbuja(numeros)
            tiempoburbuja=burbuja(numeros)
            print("tiempo de ejecucion de burbuja: ",tiempoburbuja)
        if opcionmenu==2:
            numeros = llenar()
            #burbujaOptimizada(numeros)
            tiempoburbujaoptimizada=burbujaOptimizada(numeros)
            print("tiempo de ejecucion de burbuja optimizada: ",tiempoburbujaoptimizada)
        if opcionmenu==3:
            numeros = llenar()
            tiempoburbuja=burbuja(numeros)
            print("tiempo de ejecucion de burbuja: ",tiempoburbuja)
            tiempoburbujaoptimizada=burbujaOptimizada(numeros)
            print("tiempo de ejecucion de burbuja optimizada: ",tiempoburbujaoptimizada)
            if tiempoburbuja < tiempoburbujaoptimizada:
                print("tiempo de burbuja es el mejor ")
            else:
                print("tiempo de burbuja optimizada es el mejor ")
        if opcionmenu==4:
            break

        os.system ("PAUSE")
    return

mostrarMenu()