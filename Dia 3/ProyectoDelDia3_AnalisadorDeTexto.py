#Este codigo es un analisador de texto
#Debe recibir

parrafo= "Un párrafo, también llamado parágrafo o acápite, python es una unidad comunicativa del lenguaje escrito compuesta por un conjunto de oraciones que tienen cierta unidad temática o que, sin tenerla, se enuncian juntas. Es un componente del texto que en su aspecto externo termina en un punto y aparte.".lower()

x= input("Escribe tres letras que quieras buscar en el texto\n ")
y= input()
z=input()

letter1= parrafo.count(x)
letter2= parrafo.count(y)
letter3= parrafo.count(z)

print(f'Hola, el numero de veces que está tu letra "{x}" son {letter1}, de la letra {y} son {letter2} y de la letra "{z}" son {letter3}\n')

#Hasta aqui el primer puntos


#Este el segundo punto, el que cuenta el numero de palabras del parrafo
palabras= parrafo.split()#Esto separa el string y los encapsula en una lista
npalabras= len(palabras)
print(f"El numero de palabras en este parrafo es: {npalabras}\n")



#Tercer punto, mostrar la primera palabra y la ultima palabra
print(f"La primera palabra del parrafo es +{palabras[0]}+ y la ultima palabra es +{palabras[npalabras-1]}+\n")


#El cuarto punto, mostrar el parrafo al contrario

palabras.reverse()
resultado = "".join(palabras)
print(f"El parrafo al reves es {palabras}")

r= "python" in palabras

if r==1:
        print("existe la palabra python en el texto")
else:
        print("No existe ningun ptyhon en el parrafo")