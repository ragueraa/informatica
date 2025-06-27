from typing import List, Tuple, Any
from collections import Counter
import csv
import json  # ← agregado para usar JSON

# Índices para acceder a los campos del catálogo
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
        next(reader, None)  # Saltar encabezado si existe
        books = [row for row in reader]
    return books

def check_entry_int(input_str: str) -> bool:
    return input_str.isdigit()

def send_message(message: str, expected_type: type) -> Any:
    while True:
        entry = input(message)
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

def add_book_manual(catalog: List[List[Any]]) -> None:
    """Pide datos por teclado y añade un nuevo libro al catálogo."""
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

    catalog.append([title, author, "", str(year), "", genre])
    print(f"Libro '{title}' añadido al catálogo.")

def informe_total_ejemplares(catalog: List[List[Any]]) -> str:
    return f"Total de ejemplares: {len(catalog)}"

def informe_por_genero(catalog: List[List[Any]], genre: str) -> str:
    genre_normalizado = genre.strip().lower()
    total_genre = sum(
        1 for row in catalog
        if len(row) > INDEX_GENERO and row[INDEX_GENERO].strip().lower() == genre_normalizado
    )
    return f"El género '{genre}' tiene un total de {total_genre} ejemplares."


def informe_promedio_anio(catalog: List[List[Any]], index_year: int) -> float:
    total_years = 0
    count = 0
    for row in catalog:
        if len(row) > index_year and row[index_year].isdigit():
            total_years += int(row[index_year])
            count += 1
    return total_years / count if count else 0.0

def informe_libros_viejos(catalog: List[List[Any]], year_cutoff: int, index_year: int) -> List[List[Any]]:
    return [row for row in catalog if len(row) > index_year and row[index_year].isdigit() and int(row[index_year]) < year_cutoff]

def informe_top_autores(catalog: List[List[Any]], top_n: int = 3) -> List[Tuple[str, int]]:
    autores = [row[INDEX_AUTOR] for row in catalog if len(row) > INDEX_AUTOR]
    return Counter(autores).most_common(top_n)

def bubble_sort_titulo(catalog: List[List[Any]]) -> None:
    n = len(catalog)
    for i in range(n):
        for j in range(0, n - i - 1):
            if catalog[j][INDEX_TITULO] > catalog[j + 1][INDEX_TITULO]:
                catalog[j], catalog[j + 1] = catalog[j + 1], catalog[j]

def insertion_sort_anio(catalog: List[List[Any]]) -> None:
    for i in range(1, len(catalog)):
        key = catalog[i]
        j = i - 1
        while j >= 0 and catalog[j][INDEX_PRIMERA_PUBLICACION].isdigit() and key[INDEX_PRIMERA_PUBLICACION].isdigit() and int(catalog[j][INDEX_PRIMERA_PUBLICACION]) > int(key[INDEX_PRIMERA_PUBLICACION]):
            catalog[j + 1] = catalog[j]
            j -= 1
        catalog[j + 1] = key

def display_catalog(catalog: List[List[Any]], limit: int) -> None:
    print("\n--- Catálogo ---")
    for count, row in enumerate(catalog[:limit]):
        print(f"{count + 1}. Título: {row[INDEX_TITULO]}, Autor: {row[INDEX_AUTOR]}, Año: {row[INDEX_PRIMERA_PUBLICACION]}, Género: {row[INDEX_GENERO]}")
    print("----------------")

def guardar_resumen_json(nombre_archivo: str, catalog: List[List[Any]]) -> None:
    años = [int(row[INDEX_PRIMERA_PUBLICACION]) for row in catalog if row[INDEX_PRIMERA_PUBLICACION].isdigit()]
    libro_mas_antiguo = min(años) if años else None
    libro_mas_reciente = max(años) if años else None

    generos = [row[INDEX_GENERO] for row in catalog if len(row) > INDEX_GENERO and row[INDEX_GENERO]]
    conteo_generos = dict(Counter(generos))

    resumen = {
        "total_libros": len(catalog),
        "libro_mas_antiguo": libro_mas_antiguo,
        "libro_mas_reciente": libro_mas_reciente,
        "cantidad_por_genero": conteo_generos
    }

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(resumen, f, indent=4, ensure_ascii=False)

    print(f"Resumen guardado en '{nombre_archivo}'")


def menu() -> None:
    catalog = load_from_csv("libros.csv")
    while True:
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

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            add_book_manual(catalog)
        elif opcion == "2":
            print(informe_total_ejemplares(catalog))
        elif opcion == "3":
            genre = input("Ingrese el género a buscar: ")
            print(informe_por_genero(catalog, genre))
        elif opcion == "4":
            promedio = informe_promedio_anio(catalog, INDEX_PRIMERA_PUBLICACION)
            print(f"Año promedio de publicación: {promedio:.2f}")
        elif opcion == "5":
            corte = send_message("Mostrar libros anteriores a qué año?: ", int)
            if corte is not None:
                viejos = informe_libros_viejos(catalog, corte, INDEX_PRIMERA_PUBLICACION)
                print(f"Libros publicados antes de {corte}:")
                for libro in viejos:
                    print(libro)
        elif opcion == "6":
            top = informe_top_autores(catalog)
            print("Autores más frecuentes:")
            for autor, cantidad in top:
                print(f"{autor}: {cantidad}")
        elif opcion == "7":
            limit = send_message("¿Cuántos libros mostrar?: ", int)
            if limit is not None:
                display_catalog(catalog, limit)
        elif opcion == "8":
            guardar_resumen_json("resumen.json", catalog)
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
