from pathlib import Path
import os

#base = Path(r"C:\Users\jajap\OneDrive\Desktop\Programacion\CursoUdemy\pythonProject\Dia 6\Recetas")


def leer_archivo(archivo):
    archi=open(archivo)       #Abre el archivo dado
    print(archi.read())      #Muestra el archivo en pantalla

def Ver_categorias():
    base= os.getcwd()                   #Ruta base hasta "Dia 6"
    recetas= Path(base, "Recetas")#A esa ruta base le agrego recetas para que esté dentro de las categorias
    aver= os.listdir(recetas)           #Mostras las diferentes categorias de comidas
    print(aver)
    return recetas

def Elegir_carpeta(carpeta):             #Se hace la función que reciba la categoria de a la que va a entrar
    base= os.getcwd()                    #Se ubica en el path donde estamos
    categoria= Path(base, carpeta) #Se agrega la categoria a la que se quiere entrar a el path
    return categoria

def Ver_recetas(ruta):
    # Buscar archivos .txt recursivamente en todos los subdirectorios dentro de la carpeta
    archivos_txt = list(ruta.rglob("*.txt"))
    num = 0
    for archivo in archivos_txt: # Imprimir los archivos encontrados
        num += 1  # Cuenta las recetas
        print(archivo)  # Muestra las recetas
    return num


def MenuPrincipal():
    print('''############ MENU PRINCIPAL ############ 
    
[1] leer receta
[2] crear receta
[3] crear categoria
[4] eliminar receta
[5] eliminar categoria
[6] finalizar programa''')

#TODO    Mostrar Recetas
#TODO    Elegir receta
#TODO    Leer receta
def opcio1():
    print("\nPor favor, elige una categoría entre las siguientes opciones:\n")
    Ver_categorias()
    categoria=input()
    Ver_recetas(Path(base, categoria))
    receta=input("Elije una receta: ")
    leer_archivo(Path(base, categoria,receta+".txt"))

MenuPrincipal()
opcio1()