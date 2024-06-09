suma_cuadrados = 0
resultado= list(range(0,16))

for i in resultado:
    resultado[i]=i**2
    suma_cuadrados+= (i**2)

print(resultado)
print(suma_cuadrados)
print(type(suma_cuadrados))