lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

'''for indice, i in enumerate(lista_nombres):
    print(f'{i} se encuentra en el índice {indice}')'''

'''x="Python"
lista_indices= list(enumerate(x))
print(lista_indices)'''


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, i in enumerate(lista_nombres):#Los vuelve un diccionario, siendo el indice la clave y la lista el valor
    if i[0].lower()=="m":#Comprueba si la palabra inicia con M haciendole un lower primero para no tener errores
        print(indice)
    else:
        continue