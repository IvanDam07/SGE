def calcular_comision():
    nombre = input("Por favor, ingresa tu nombre: ")
    ventas = float(input("¿Cuánto has vendido este mes? "))
    comision = ventas * 0.13
    return f"{nombre}, tu comisión este mes es de {comision:.2f} euros."

print(calcular_comision())