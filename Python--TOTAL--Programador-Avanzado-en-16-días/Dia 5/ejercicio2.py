def uniqueLetters(a):#a es un string

    a=a.lower()
    a=list(a)#Convert the string in a list where anyone letter is a index in the list
    a.sort()#order the letters
    a=set(a)#Convert the list to a set in orden to delete the duplicate letters
    a=list(a)#Go back to a list
    print(a)


uniqueLetters("HolaPvtoGOOOONOREAAAJIJIIJijijijIJIi")

'''mi_string = "hola"
mi_lista = [letra for letra in mi_string]
print(mi_lista)  # Salida: ['h', 'o', 'l', 'a']'''
