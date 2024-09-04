def decorar_saludo(funcion):

    def funcion_dentro(palabra):
        print("Cordial saludo")
        funcion(palabra)
        print("Adiós muchachos")
    return funcion_dentro

def mayuscula(n):
    print(n.lower())

mayuscula_decorada= decorar_saludo(mayuscula)

mayuscula_decorada(input("Coloca un dicurso"))