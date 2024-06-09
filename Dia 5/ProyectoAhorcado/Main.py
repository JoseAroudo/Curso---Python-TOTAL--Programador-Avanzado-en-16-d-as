import random


def Main():
    listName=["jose","manzana","popular","verga","hello","apple","alberto"]
    palabra= random.choice(listName)
    numberLetters= len(list(palabra))#Number of letters that have a word and with that numbre put the "-" in the client
    letra=input("Ingrese la letra: ")#This is the letter in orden to search
    vida=5                           #The life that the user have


    # AGREGAR LETRAS DIGITADAS ANTERIORMENTE
    add_to_list = lambda Lista, letra: Lista.append(letra)  # Funtion para agregar letras al final

    # SABER DONDE ESTA LA LETRA
    posicion = lambda letra, palabra: palabra.find(letra) if validar(letra) and letra in palabra else -1

    #VALIDACIONES PARA SABER SI ES UNA LETRA VALIDAXD
    validar = lambda x: x.isalpha() and len(list(x)) == 1 and x not in LetrasIngresadas  # Validation to know if it is alphabet and is one letter



    LetrasIngresadas = []
    oculta= "-"*numberLetters        #The word in indden mode




    add_to_list(LetrasIngresadas,letra)


Main()
#vida = lambda x: x > 0 para saber si tiene vidas todavia o no