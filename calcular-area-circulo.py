import math


# 1. Solicitar al usuario que ingrese el radio del circulo, hay que castear el string y pasarlo a float.

radio = float(input("Por favor, ingrese el radio del circulo: "))


# 2. Calcular el area del circulo utilizando la formula area = π * radio^2

area = math.pi * (radio**2)




# 3. Mostrar al ususario el area calculada.

print("El area del circulo con radio", radio, "es: ", area)

