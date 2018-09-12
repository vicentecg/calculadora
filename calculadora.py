def sumar():
    print("--------------------------")
    primer_n = int(input("Primer valor:"))
    segundo_n = int(input("Segundo valor:"))
    print("---------------------------")
    suma = primer_n + segundo_n
    print("--------------------------")
    print("La suma es:" , suma)
    print("---------------------------")
    pass

def restar():
    print("--------------------------")
    primer_n = int(input("Primer valor:"))
    segundo_n = int(input("Segundo valor:"))
    print("---------------------------")
    resta = primer_n - segundo_n
    print("--------------------------")
    print("La resta es:", resta)
    print("---------------------------")
    pass

def multiplicar():
    print("--------------------------")
    primer_n = int(input("Primer valor:"))
    segundo_n = int(input("Segundo valor:"))
    print("---------------------------")
    multip = primer_n * segundo_n
    print("--------------------------")
    print("El resultado es:", multip)
    print("---------------------------")
    pass

def dividir():
    print("--------------------------")
    primer_n = int(input("Primer valor:"))
    segundo_n = int(input("Segundo valor:"))
    print("---------------------------")
    divic = primer_n / segundo_n
    print("--------------------------")
    print("El resultado es:", divic)
    print("---------------------------")
    pass

def elevar():
    print("--------------------------")
    primer_n = int(input("Numero:"))
    segundo_n = int(input("Veces a elevar:"))
    print("---------------------------")
    elev = primer_n ** segundo_n
    print("--------------------------")
    print("El resultado es:", elev)
    print("---------------------------")
    pass

def menu():
    while(True):
        print("------------------------------")
        print("Bienvenido a calculadora 2018")
        print("------------------------------")
        print("operaciones:")
        print("a.- Sumar")
        print("b.- Restar")
        print("c.- Multiplicar")
        print("d.- Dividir")
        print("e.- Elevar")
        print("f.- Salir")
        print("------------------------------")
        opcion = input("Ingrese opcion:")

        if(opcion.lower() == "a"):
            sumar()
        elif(opcion.lower() == "b"):
            restar()
        elif(opcion.lower() == "c"):
            multiplicar()
        elif(opcion.lower() == "d"):
            dividir()
        elif(opcion.lower() == "e"):
            elevar()
        elif(opcion.lower() == "f"):
            break
menu()
pass


