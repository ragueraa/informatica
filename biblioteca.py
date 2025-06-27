from pprint import pprint
from funciones import (
    get_catalog,
    add_book_manual,
    informe_total_ejemplares,
    informe_por_genero,
    informe_promedio_anio,
    informe_libros_viejos,
    informe_top_autores,
    guardar_resumen_json,
    check_entry_int,
    get_genero,
    display_catalog
)



def send_message(message: str, expected_type: type) -> None:
    while True:
        entry = input(message)
        print("Ingresa '0' para salir en cualquier momento.")
        if entry == "0":
            print("Saliendo...")
            return None

        if expected_type == int:
            if check_entry_int(entry):
                return int(entry)
            else:
                print("Entrada inválida. Por favor ingresa un número entero válido.")
        elif expected_type == str:
            if entry.strip() == "":
                print("Entrada inválida. Por favor ingresa un texto no vacío.")
            else:
                return entry

def handle_promedio_anio(catalog: list) -> None:
    promedio = informe_promedio_anio(catalog)

    if promedio == 0:
        print("No se encontraron años de publicación válidos en el catálogo.")
        return
    print(f"Año promedio de publicación: {promedio}")

def handle_informe_libros_viejos(catalog: list) -> None:
    corte = send_message("Mostrar libros anteriores a qué año?: ", int)
    if corte is not None:
        viejos = informe_libros_viejos(catalog, corte)

        if len(viejos) <= 0:
            print(f"No se encontraron libros publicados antes de {corte}.")
            return
        
        print(f"\n----- Libros publicados antes de {corte}: ----")
        count = 0
        for [titulo, autor, anio, genero] in viejos:
            print(f"{count + 1}. Título: {titulo}, Autor: {autor}, Año: {anio}, Género: {genero}")
            count += 1
        print("----------------")

def handle_top_autores(catalog: list) -> None:
    top = informe_top_autores(catalog)

    if len(top) <=  0:
        print("No se encontraron autores en el catálogo.")
        return
    print("Autores más frecuentes:")
    for autor, cantidad in top:
        print(f"{autor}: {cantidad}")

def handle_catalogo(catalog: list) -> None:
    limit = send_message("¿Cuántos libros mostrar?: ", int)
    if limit is not None:
        display = display_catalog(catalog, limit)
        if len(catalog) > 0:
            print("\n--- Catálogo ---")
            count = 0
            for [titulo, autor, anio, genero] in display:
                print(f"{count + 1}. Título: {titulo}, Autor: {autor}, Año: {anio}, Género: {genero}")
                count += 1
            print("----------------")

def handle_informe_genero(catalog: list) -> None:
    available_genres = get_genero(catalog)
    if len(available_genres) > 0:
        print("Los géneros disponibles son: " + ", ".join(available_genres))
        genre = send_message("Ingrese el género a buscar: ", str)

        total_genre = informe_por_genero(catalog, genre)
        if total_genre > 0:
            print(f"El género '{genre}' tiene un total de {total_genre} ejemplares.")
        else:
            print(f"El género '{genre}' no se encuentra en el catálogo.")

    else:
        print("No se encontraron géneros disponibles.")

def handle_add_book_manual(catalog: list) -> None:
    """Pide datos por teclado y añade un nuevo libro al catálogo y al archivo CSV."""
    print("Añadiendo un nuevo libro al catálogo...")
    print("Presiona 0 en cualquier momento para salir.")

    title = send_message("Título del libro: ", str)
    if title is None: return

    author = send_message("Autor: ", str)
    if author is None: return

    year = send_message("Año de publicación: ", int)
    if year is None: return

    genre = send_message("Género: ", str)
    if genre is None: return

    new_book = [title, author, "", str(year), "", genre]

    catalog = add_book_manual(new_book, catalog)

    print(f"Libro '{title}' añadido al catálogo y guardado en 'libros.csv'.")

def handle_total_ejemplares(catalog: list) -> None:
    """ Imprime el total de ejemplares disponibles."""
    total = informe_total_ejemplares(catalog)
    print("Total de ejemplares: " + str(total))

def handle_guardar_resumen_json(catalog: list, filename: str = "resumen.json") -> None:
    guardar_resumen_json(filename, catalog)
    print(f"Resumen guardado en '{filename}'")

def show_main_menu() -> None:
    print("\nMenú:")
    print("1. Añadir libro manualmente")
    print("2. Informe total de ejemplares")
    print("3. Informe por género")
    print("4. Informe promedio de año")
    print("5. Informe libros viejos")
    print("6. Informe top autores")
    print("7. Mostrar catálogo")
    print("8. Resumen de catálogo en JSON")
    print("0. Salir")

def menu() -> None:
    catalog = get_catalog()

    while True:
        
        show_main_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            handle_add_book_manual(catalog)
        elif opcion == "2":
            handle_total_ejemplares(catalog)
        elif opcion == "3":
            handle_informe_genero(catalog)
        elif opcion == "4":
            handle_promedio_anio(catalog)
        elif opcion == "5":
            handle_informe_libros_viejos(catalog)
        elif opcion == "6":
            handle_top_autores(catalog)
        elif opcion == "7":
            handle_catalogo(catalog)
        elif opcion == "8":
            handle_guardar_resumen_json(catalog)
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
        

        continuar = input("\n¿Deseás realizar otra operación? (s/n): ").strip().lower()
        if continuar == "n":
            print("Saliendo del sistema...")
            break

def main() -> None:
    menu()

if __name__ == "__main__":
    main()
