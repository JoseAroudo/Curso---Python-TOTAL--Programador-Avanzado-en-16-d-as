'''txt=",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

x= txt.lstrip(",:%_#")
print(x)
Esto remueve los caracteres solo del lado izquierdo de la frase'''

'''frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(3,"naranja")

print(frutas)
Deja en la posicion 3 de la lista la palabra que hay despues de la coma'''


'''
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados=marcas_tv.isdisjoint(marcas_smartphones)

print(conjuntos_aislados)'''



'''def invertir_palabra(palabra):
    x= palabra[::-1].upper()
    print(x)
    return x

invertir_palabra("hola")'''

'''from random import randint


def lanzar_dados():
    x = randint(1, 7)
    y = randint(1, 7)

    return x, y


def evaluar_jugada(x):
    z = x[0] + x[1]
    if (z < 6):
        print(f"La suma de tus datos es {z}. Lamentable")

    elif (z > 6 and z < 10):
        print(f"La suma de tus dados es {z}. Tienes buenas chances")

    elif (z >= 10):
        print(f"La suma de tus dados es {z}. Parece una jugada ganadora")

evaluar_jugada(lanzar_dados())'''

'''import statistics


def reducir_lista(x):
    y= set(x)
    z=list(y)
    z.pop()
    return z


def promedio(listaReducida):
    return statistics.mean(listaReducida)


lista_numeros = [1, 2, 2, 3, 3, 3, 4, 18]
listaReducida = promedio(lista_numeros)

print(reducir_lista(lista_numeros))
print(listaReducida)'''

'''import random

def lanzar_moneda():
    x= random.randint(0,2)
    return x

def probar_suert(x):

    if x==1:
        print("La lista se autodestruirá")
    else:
        print("La lista fue salvada")
        print("Te salio cara")


probar_suert(lanzar_moneda())



lista_numeros=[1,2,3,4,5,6,7,8,9]'''

import random

def lanzar_moneda():
    x= random.randint(0,2)
    if x==1:
        z="Cara"
    else:
        z="Cruz"
    return z

def probar_suerte(x,lista):

    if x=="Cara":
        lista.clear()
        print("La lista se autodestruirá")
        return lista#o print si se quiere mostrar
    else:
        print("La lista fue salvada")
        print("Te salio cara")

lista_numeros=[1,2,3,4,5,6,7,8,9]
probar_suerte(lanzar_moneda(),lista_numeros
