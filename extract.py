from typing import List, Dict, Tuple, Any
import csv

INDEX_TITULO = 0
INDEX_AUTOR = 1
INDEX_IDIOMA = 2
INDEX_PRIMERA_PUBLICACION = 3
INDEX_VENTAS_MILLONES = 4
INDEX_GENERO = 5

def load_from_csv(filepath: str) -> List[List[Any]]:
    """Carga el catálogo desde un CSV y devuelve una lista de registros."""
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        books = []
        for row in reader:
            books.append(row)

        return books


def check_entry_int(input_str: str) -> int:
    numbers = "0123456789"

    for char in input_str:
        if char not in numbers:
            return False
    return True

def send_message(message: str, type: type) -> None:

    while True:
        entry = input(message)

        if entry == "0":
            print("Saliendo...")
            return

        if type == int:
            if check_entry_int(entry):
                return int(entry)
            else:
                print("Entrada inválida. Por favor ingresa un número entero válido.")
        elif type == str:
            if entry.strip() == "":
                print("Entrada inválida. Por favor ingresa un texto no vacío.")
            else:
                return entry


def add_book_manual(catalog) -> None:
    """Pide datos por teclado y añade un nuevo libro al catálogo."""

    print("Añadiendo un nuevo libro al catálogo...")
    print("Presiona 0 en cualquier momento para salir.")


    title = send_message("Título del libro: ", str)
    author = send_message("Autor: ", str)
    year = str(send_message("Año de publicación: ", int))

    if year:
        year = int(year)

    genre = send_message("Género: ", str)

    if (title or author or year or genre):
        catalog.append([title, author, year, genre])
        print(f"Libro '{title}' añadido al catálogo.")

    else:
        print("No se han proporcionado datos válidos para añadir el libro.")
    return catalog

def informe_total_ejemplares(catalog) -> str:
    """Calcula y retorna el total de ejemplares disponibles."""

    total = len(catalog)

    return "Total de ejemplares: " + str(total)

def informe_por_genero(catalog, genre) :
    """Cuenta libros por género y devuelve un dict género→conteo."""
    total_genre = 0 
    for row in catalog:
        actual_genre = row[INDEX_GENERO]
        if actual_genre == genre:
            total_genre += 1

    return "El genero " + genre + " tiene un total de " + str(total_genre) + " ejemplares."

def informe_promedio_anio(catalog, index_year) -> float:
    """Calcula el año promedio de publicación de los libros."""
    if not catalog:
        return 0.0

    total_years = 0
    count = 0

    for row in catalog:
        year = row[index_year]
        if year.isdigit():
            total_years += int(year)
            count += 1

    if count == 0:
        return 0.0

    return total_years / count

def informe_libros_viejos(catalog, year, index_year):
    """Retorna la lista de libros publicados antes de `año_corte`."""

    libros_viejos = []
    for row in catalog:
        if row[index_year] < year:
            libros_viejos.append(row)
    return libros_viejos

def informe_top_autores(catalog, top_n) -> List[Tuple[str, int]]:
    """Devuelve una lista de los `top_n` autores más frecuentes y su conteo."""
    pass

def bubble_sort_titulo(catalog) -> None:
    """Ordena el catálogo in place por título usando el algoritmo burbuja."""
    n = len(catalog)
    for i in range(n):
        for j in range(0, n-i-1):
            if catalog[j][0] > catalog[j+1][0]:
                catalog[j], catalog[j+1] = catalog[j+1], catalog[j]

def insertion_sort_anio(catalog) -> None:
    """Ordena el catálogo in place por año de publicación usando inserción."""
    for i in range(1, len(catalog)):
        key = catalog[i]
        j = i - 1
        while j >= 0 and key[2] < catalog[j][2]:
            catalog[j + 1] = catalog[j]
            j -= 1
        catalog[j + 1] = key

def display_catalog(catalog, limit) -> None:
    """Muestra por consola los primeros `limit` registros del catálogo."""

    count = 0
    while count < limit and count < len(catalog):
        row = catalog[count]
        print(f"{count + 1}. Título: {row[0]}, Autor: {row[1]}, Año: {row[2]}, Género: {row[3]}")
        count += 1

def menu() -> None:
    """Muestra el menú principal y gestiona la selección de opciones."""
    catalog = load_from_csv("text.txt")
    while True:
        print("\nMenú:")
        print("1. Añadir libro manualmente")
        print("2. Informe total de ejemplares")
        print("3. Informe por género")
        print("4. Informe promedio de año")
        print("5. Informe libros viejos")
        print("6. Informe top autores")
        print("7. Mostrar catálogo")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            add_book_manual(catalog)
        elif opcion == "2":
            total = informe_total_ejemplares(catalog)
            print(total)
        elif opcion == "3":
            por_genero = informe_por_genero(catalog)
            print(por_genero)
        elif opcion == "4":
            promedio = informe_promedio_anio(catalog)
            print(f"Año promedio de publicación: {promedio}")
        elif opcion == "5":
            viejos = informe_libros_viejos(catalog)
            print("Libros publicados antes de 1950:", viejos)
        elif opcion == "6":
            top = informe_top_autores(catalog)
            print(top)
        elif opcion == "7":
            display_catalog(catalog)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

def main() -> None:
    """Punto de entrada: inicializa estructuras, bucle de menú y finaliza."""
    menu()

if __name__ == "__main__":
    main()