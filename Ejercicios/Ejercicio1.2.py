def analizar_texto():
    texto = input("Ingresa un texto: ").lower()
    letras = [input(f"Ingresa la letra {i+1}: ").lower() for i in range(3)]

    cont_letras = {letra: texto.count(letra) for letra in letras} #Cuenta las letras de la palabra
    num_palabras = len(texto.split()) #Divide el texto por palabras y devuelve el número
    primera_letra = texto[0] #Selecciona la primera letra
    ultima_letra = texto[-1] #Selecciona la última letra
    texto_invertido = texto[::-1] #Le da la vuelta al texto, lo invierte
    esta_python = "python" in texto

    resultado = {
        "cont_letras": cont_letras,
        "num_palabras": num_palabras,
        "primera_letra": primera_letra,
        "ultima_letra": ultima_letra,
        "texto_invertido": texto_invertido,
        "esta_python": "Sí" if esta_python else "No"
    }

    print(f"Letras contadas: {resultado['cont_letras']}")
    print(f"Número de palabras: {resultado['num_palabras']}")
    print(f"Primera letra del texto: {resultado['primera_letra']}")
    print(f"Última letra del texto: {resultado['ultima_letra']}")
    print(f"Texto invertido: {resultado['texto_invertido']}")
    print(f"¿Aparece la palabra 'Python' en el texto? {resultado['esta_python']}")

analizar_texto()