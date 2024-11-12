def nombre_cerveza():
    palabra1 = input("¿Cuál es tu color favorito?")
    palabra2 = input("¿Cuál es tu animal favorito?")
    return f"El nombre de tu cerveza es... {palabra1.capitalize()} {palabra2.capitalize()}"

print(nombre_cerveza()) 