import random

def adivina_el_numero():
    nombre = input("¿Podrías decirme tu nombre? ")

    print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo 8 intentos para adivinar cuál crees que es el número.")

    numero_a_adivinar = random.randint(1,100)
    intentos = 8

    for intento in range(1, intentos + 1):
        numero_elegido = int(input(f"Intento {intento}. Elige un número: "))

        if numero_elegido < 1 or numero_elegido > 100:
            print("Has elegido un número que está fuera del rango.")
        elif numero_elegido < numero_a_adivinar:
            print("Número incorrecto. El número elegido es menor que el número a adivinar.")
        elif numero_elegido > numero_a_adivinar:
            print("Número incorrecto. El número elegido es mayor que el número a adivinar.")
        else:
            print(f"Enhorabuena. Has acertado el número en {intento} intentos.")
            return
    print(f"Lo siento, has agotado todos tus intentos y no has acertado el número secreto. El número era {numero_a_adivinar}.")

adivina_el_numero()