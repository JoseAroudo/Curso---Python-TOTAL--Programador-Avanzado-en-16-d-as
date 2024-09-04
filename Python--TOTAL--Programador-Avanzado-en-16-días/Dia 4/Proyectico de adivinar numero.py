from random import randint
intentos=8      #las vidas que tiene el usuario
numero_usuario=int(input("Aver, selecciona un numero del 1 al 100 para adivinar el numero de la maquina, tienes 8 vidas\n"))#el numero que va a decir el usuario
aleatorio=randint(0,101)     #es el numero aleatorio que crea la maquina

while intentos>=0:

    if(numero_usuario<1 or numero_usuario>100):
        print(f"no seas imbecil, coloca un numero del 1 al 100 como te lo pedí, tienes {intentos} cabron\n")
        intentos -= 1
        numero_usuario = int(input("Selecciona otro número\n"))
        

    elif(numero_usuario>aleatorio):
        print(f"Tu numero es mayor, intenta de nuevo con un numero menor, tienes {intentos} intentos\n")
        intentos -=1
        numero_usuario=int(input("Selecciona otro número\n"))


    elif(numero_usuario<aleatorio):
        print(f"Tu numero es menor, intenta un numero mayor, tienes {intentos} intentos\n")
        intentos -= 1
        numero_usuario = int(input("Selecciona otro número\n"))


    elif(aleatorio==numero_usuario):
        print("Ganaste hdpm\n")
        break
    elif(intentos==0):
        print(f"perdiste, no tienes más vidas, pendejo, el numero era {aleatorio}")