class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Cliente(Persona):
    def __init__(self,nombre, apellido, edad, numero_cuenta, balance):
        super().__init__(nombre, apellido, edad)
        self.numero_cuenta = numero_cuenta
        self.balance = balance


    def depositar(self, numero_cuenta, balance, deposito):
        self.numero_cuenta = numero_cuenta
        self.balance = balance+deposito

    def retirar(self, numero_cuenta, balance, retiro):
        self.numero_cuenta = numero_cuenta
        self.balance = balance-retiro

    def __str__(self):
        print(f"El nombre del cliente es: {self.nombre} {self.apellido}, y tiene {self.balance}")

