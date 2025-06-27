from pprint import pprint
import tkinter as tk
from tkinter import messagebox, simpledialog
from collections import Counter
import csv
import json  

# Índices para acceder a los campos del catálogo
INDEX_TITULO = 0
INDEX_AUTOR = 1
INDEX_IDIOMA = 2
INDEX_PRIMERA_PUBLICACION = 3
INDEX_VENTAS_MILLONES = 4
INDEX_GENERO = 5

def get_catalog(filepath: str = "libros.csv") -> list:
    """Carga el catálogo desde un CSV y devuelve una lista de registros."""
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # Saltar encabezado si existe
        books = [row for row in reader]
    return books

def check_entry_int(input_str: str) -> bool:
    """Verifica si la entrada es un número entero."""
    return input_str.isdigit()

def add_book_manual(new_book: list, catalog: list) -> None:
    """Añade un nuevo libro al catálogo y al archivo CSV."""
    # Escribir en el CSV
    with open("libros.csv", "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(new_book)

    catalog.append(new_book)

    return catalog

def informe_total_ejemplares(catalog: list) -> int:
    """Devuelve el total de ejemplares en el catálogo."""
    return len(catalog)

def get_genero(catalog) -> str:

    """Devuelve una lista de géneros únicos en el catálogo."""

    total_genre = []

    for row in catalog:
        genre = row[INDEX_GENERO].lower().title()
        if genre not in total_genre:
            total_genre.append(genre)
    
    return total_genre

def informe_por_genero(catalog, genre: str) -> str:

    """Devuelve el total de libros por género."""

    parsed_genre = genre.lower().title()

    total_genre = 0

    if parsed_genre in get_genero(catalog):
        total_genre = sum(1 for row in catalog if len(row) > INDEX_GENERO and row[INDEX_GENERO].lower().title() == parsed_genre)

    return total_genre

def informe_promedio_anio(catalog) -> float:

    """Devuelve el año promedio de publicación de los libros en el catálogo."""
    total_years = 0
    count = 0
    for row in catalog:
        if len(row) > INDEX_PRIMERA_PUBLICACION and row[INDEX_PRIMERA_PUBLICACION].isdigit():
            total_years += int(row[INDEX_PRIMERA_PUBLICACION])
            count += 1
    return total_years // count if count else 0

def informe_libros_viejos(catalog, year_cutoff: int) -> list:
    """Devuelve una lista de libros publicados antes de un año específico."""
    libros_viejos = [row for row in catalog if len(row) > INDEX_PRIMERA_PUBLICACION and row[INDEX_PRIMERA_PUBLICACION].isdigit() and int(row[INDEX_PRIMERA_PUBLICACION]) < year_cutoff]

    libros_viejos = display_catalog(libros_viejos, len(libros_viejos))

    return libros_viejos

def informe_top_autores(catalog, top_n: int = 3) -> list:
    """Devuelve una lista de los autores más frecuentes en el catálogo."""
    
    autores = cantidad_ordenada_por_categoria_desc(catalog, INDEX_AUTOR)
    if autores:
        return autores[:top_n]
    return []

def insertion_sort_tuple_desc(counter: list) -> list:
    """Ordena una lista de tuplas en orden descendente por el segundo elemento."""

    for i in range(1, len(counter)):
        valor_actual = counter[i]
        j = i - 1

        while j >= 0 and counter[j][1] < valor_actual[1]:
            counter[j + 1] = counter[j]
            j -= 1
        counter[j + 1] = valor_actual

    return counter

def cantidad_ordenada_por_categoria_desc(catalog: list, index_categoria) -> tuple:

    """Devuelve una lista de tuplas con la cantidad de libros por categoría, ordenada en orden descendente."""

    generos = []

    for row in catalog:
        if len(row) > index_categoria and row[index_categoria] not in generos:
            generos.append(row[index_categoria])
    
    counter = []

    for genero in generos:
        n = 0
        for row in catalog:
            if  len(row) > index_categoria and row[index_categoria] == genero :
                n+= 1
        counter.append((genero, n))

    if len(counter) > 0:
        counter = insertion_sort_tuple_desc(counter)
        return counter

    return []

def bubble_sort_titulo(catalog:list) -> None:
    """Ordena el catálogo por título usando el algoritmo de burbuja."""
    n = len(catalog)
    for i in range(n):
        for j in range(0, n - i - 1):
            if catalog[j][INDEX_TITULO] > catalog[j + 1][INDEX_TITULO]:
                catalog[j], catalog[j + 1] = catalog[j + 1], catalog[j]

def guardar_resumen_json(nombre_archivo: str, catalog: list) -> None:
    total_libros = len(catalog)

    años_validos = [int(row[INDEX_PRIMERA_PUBLICACION]) for row in catalog
                    if len(row) > INDEX_PRIMERA_PUBLICACION and row[INDEX_PRIMERA_PUBLICACION].isdigit()]
    libro_mas_antiguo = min(años_validos) if años_validos else None
    libro_mas_reciente = max(años_validos) if años_validos else None

    conteo_generos = {}
    for row in catalog:
        if len(row) > INDEX_GENERO:
            genero = row[INDEX_GENERO].strip()
            if genero:
                if genero in conteo_generos:
                    conteo_generos[genero] += 1
                else:
                    conteo_generos[genero] = 1

    resumen = {
        "total_libros": total_libros,
        "libro_mas_antiguo": libro_mas_antiguo,
        "libro_mas_reciente": libro_mas_reciente,
        "cantidad_por_genero": conteo_generos
    }

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(resumen, f, indent=4, ensure_ascii=False)

    print(f"Resumen guardado en '{nombre_archivo}'")
    
def display_catalog(catalog: list, limit: int) -> None:

    """Devuelve una lista de libros del catálogo, limitada por el parámetro 'limit'."""
    
    payload = []

    count = 0
   
    for row in catalog:
        titulo = row[INDEX_TITULO]
        autor = row[INDEX_AUTOR]   
        anio = row[INDEX_PRIMERA_PUBLICACION]
        genero = row[INDEX_GENERO]
        payload.append([titulo, autor, anio, genero])

        count += 1
        if count >= limit:
            break


    return payload

