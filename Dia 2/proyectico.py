username1= input("Hello, please insert your name: ")
venta1= int(input("Now insert your sales: "))

username2= input("Hello, please insert your name: ")
venta2= int(input("Now insert your sales: "))


print(f"Hola {username1} tu vendiste {venta1} este mes, por lo tanto tu comisión es {round(venta1 * 0.13,2)}")

print(f"Hola {username2} tu vendiste {venta2} este mes, por lo tanto tu comisión es {round(venta2 * 0.13,2)}")