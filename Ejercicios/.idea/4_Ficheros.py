import os
import shutil

# Ruta base donde se almacenan las recetas
PATH = r"C:\Users\ivans\Documents\Recetas"

print(f"Bienvenido al administrador de recetas.\nTus recetas se encuentran en: {PATH}")

total = sum(len(files) for _, _, files in os.walk(PATH))
print(f"Actualmente hay {total} recetas en el sistema.")


def show_menu():
    print("\nMenú de opciones:")
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Finalizar programa")
    return input("Seleccione una opción: ")

while True:

    option = show_menu()

    if option == '1':
        categoria = input("Dime la categoría: ")
        categoria_path = os.path.join(PATH, categoria)

        if not os.path.exists(categoria_path):
            print("No existe esta categoría.")
            break

        recetas = [recet for recet in os.listdir(categoria_path) if recet.endswith('.txt')]

        if not recetas:
            print("No hay recetas en esta categoría.")
            break

        print("Estas son las recetas disponibles: ")
        for receta in recetas:
            print(receta)

        nombre_receta = input("Dime el nombre de la receta que desea leer: ")
        receta_path = os.path.join(categoria_path, nombre_receta)

        if not os.path.exists(receta_path):
            print("Esta receta no existe.")
            break

        with open(receta_path, 'r') as file:
            print(file.read())

    elif option == '2':
        categoria = input("Dime la categoría donde quieres añadir la receta: ")
        categoria_path = os.path.join(PATH, categoria)

        if not os.path.exists(categoria_path):
            print("Esta categoría no existe.")
            break

        nombre_receta = input("Ingresa el nombre de la receta: ")
        nombre_receta = nombre_receta + ".txt"
        contenido = input("Ingresa el contenido que tendrá la receta: ")
        receta_path = os.path.join(categoria_path, nombre_receta)

        with open(receta_path, 'w') as file:
            file.write(contenido)

        print("Se ha creado la receta correctamente.")

    elif option == '3':
        categoria = input("Ingresa el nombre de la nueva categoría: ")
        categoria_path = os.path.join(PATH, categoria)

        os.makedirs(categoria_path, exist_ok=True)

        print("La categoría ha sido creada exitosamente.")

    elif option == '4':
        categoria = input("Dime la categoría a la que pertenece la receta que quieres eliminar: ")
        categoria_path = os.path.join(PATH, categoria)

        if not os.path.exists(categoria_path):
            print("La categoría introducida no existe.")
            break

        nombre_receta = input("Ingresa el nombre de la receta que quieres eliminar: ")
        nombre_receta = nombre_receta + ".txt"
        receta_path = os.path.join(categoria_path, nombre_receta)

        if not os.path.exists(receta_path):
            print("Esta receta no existe, no se puede eliminar.")

        os.remove(receta_path)

        print("Receta eliminada con éxito.")

    elif option == '5':
        categoria = input("Dime la categoría que quieres eliminar: ")
        categoria_path = os.path.join(PATH, categoria)

        if not os.path.exists(categoria_path):
            print("La categoría no existe, no se puede eliminar.")
            break

        shutil.rmtree(categoria_path)

        print("Se ha eliminado la categoría de forma exitosa.")
    elif option == '6':
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

    input("\nPresione Enter para continuar...")