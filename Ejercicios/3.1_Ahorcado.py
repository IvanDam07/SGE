import random

def ahorcado():
    palabras = ["java", "python", "android", "linux", "pokemon", "windows"]
    palabra_elegida = random.choice(palabras)
    letras_adivinadas = set()
    vidas = 6

    while vidas > 0:
        palabra_oculta = ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra_elegida)
        print(f"\nPalabra: {palabra_oculta}.")
        print(f"\nTe quedan {vidas} vidas.")

        if '_' not in palabra_oculta:
            print(f"\nEnhorabuena, has acertado la palabra. La palabra era: {palabra_elegida}")
            return

        letra = input("Di la letra que quieres comprobar: ").lower()

        if len(letra) != 1:
            print("Solo se puede ingresar una letra. Has ingresado más de una letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya has comprobado esta letra. Introduzca otra distinta.")
            continue

        letras_adivinadas.add(letra)

        if letra in palabra_elegida:
            print("Correcto. La letra se encuentra en la palabra.")
        else:
            vidas -= 1
            print(f"Incorrecto. Está letra no está en la palabra, pierdes una vida.")
    print(f"\nHas perdido todas las vidas. La palabra era {palabra_elegida}")

ahorcado()