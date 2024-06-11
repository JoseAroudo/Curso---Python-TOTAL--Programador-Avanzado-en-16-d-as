#Funcion que reciba 3 diferentes parametros y sumarlos para con el resultado

def devolver_distintos(a,b,c):
    lista=[a,b,c]
    mayor, menor, intermedio =0,0,0
    menor = min(lista)
    mayor = max(lista)
    for i in lista:
        if i != menor and i != mayor:
            intermedio=i
    print(f"El mayor es {mayor}, El menor es {menor} y el del medio es {intermedio}")
    suma=a+b+c
    if suma>15:
        print(f"El mayor es {mayor}")
    elif(suma<10):
        print(f"El menor es {menor}")
    else:
        print(f"El medio es {intermedio}")

devolver_distintos(1,2,3)
