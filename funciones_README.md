# Documentación del Módulo de Funciones - funciones.py

## Descripción General
El archivo `funciones.py` es el módulo principal que contiene la lógica de negocio del sistema de gestión de biblioteca. Este módulo proporciona todas las funciones necesarias para manipular el catálogo de libros, realizar cálculos estadísticos, ordenar datos y exportar información en diferentes formatos.

## Dependencias
El módulo utiliza las siguientes librerías:
- `pprint`: Para formateo de salida (pretty printing)
- `csv`: Para manejo de archivos CSV
- `json`: Para exportación de datos en formato JSON

## Constantes de Índices
El módulo define constantes para acceder a los campos del catálogo de libros:
- `INDEX_TITULO = 0`: Posición del título en el registro
- `INDEX_AUTOR = 1`: Posición del autor en el registro
- `INDEX_IDIOMA = 2`: Posición del idioma en el registro
- `INDEX_PRIMERA_PUBLICACION = 3`: Posición del año de publicación en el registro
- `INDEX_VENTAS_MILLONES = 4`: Posición de las ventas en millones en el registro
- `INDEX_GENERO = 5`: Posición del género en el registro

## Funciones del Sistema

### 1. `get_catalog(filepath: str = "libros.csv") -> list`
**Propósito**: Carga el catálogo de libros desde un archivo CSV.

**Parámetros**:
- `filepath`: Ruta del archivo CSV (por defecto "libros.csv")

**Retorna**: Lista de registros de libros

**Funcionalidad**:
- Abre el archivo CSV con codificación UTF-8
- Omite la primera línea (encabezado)
- Lee todos los registros y los convierte en una lista
- Maneja automáticamente la estructura CSV

### 2. `check_entry_int(input_str: str) -> bool`
**Propósito**: Valida si una cadena de texto representa un número entero válido.

**Parámetros**:
- `input_str`: Cadena de texto a validar

**Retorna**: Booleano indicando si es un entero válido

**Funcionalidad**:
- Utiliza el método `isdigit()` para verificar si todos los caracteres son dígitos
- Función utilitaria para validación de entrada de usuario

### 3. `add_book_manual(new_book: list, catalog: list) -> list`
**Propósito**: Añade un nuevo libro al catálogo y lo persiste en el archivo CSV.

**Parámetros**:
- `new_book`: Lista con los datos del nuevo libro
- `catalog`: Lista del catálogo actual

**Retorna**: Catálogo actualizado

**Funcionalidad**:
- Escribe el nuevo libro al final del archivo CSV
- Añade el libro al catálogo en memoria
- Mantiene la sincronización entre archivo y memoria
- Utiliza codificación UTF-8 para caracteres especiales

### 4. `informe_total_ejemplares(catalog: list) -> int`
**Propósito**: Calcula el total de ejemplares en el catálogo.

**Parámetros**:
- `catalog`: Lista del catálogo

**Retorna**: Número entero con el total de ejemplares

**Funcionalidad**:
- Simplemente retorna la longitud de la lista del catálogo
- Función básica de conteo

### 5. `get_genero(catalog) -> list`
**Propósito**: Extrae todos los géneros únicos presentes en el catálogo.

**Parámetros**:
- `catalog`: Lista del catálogo

**Retorna**: Lista de géneros únicos

**Funcionalidad**:
- Itera por todos los registros del catálogo
- Normaliza los géneros (convierte a minúsculas y luego a título)
- Evita duplicados manteniendo una lista de géneros únicos
- Proporciona una vista de todos los géneros disponibles

### 6. `informe_por_genero(catalog, genre: str) -> int`
**Propósito**: Cuenta el total de libros de un género específico.

**Parámetros**:
- `catalog`: Lista del catálogo
- `genre`: Género a buscar

**Retorna**: Número entero con el total de libros del género

**Funcionalidad**:
- Normaliza el género de búsqueda (minúsculas a título)
- Verifica que el género exista en el catálogo
- Cuenta los registros que coinciden con el género especificado
- Incluye validación de longitud de registro

### 7. `informe_promedio_anio(catalog) -> float`
**Propósito**: Calcula el año promedio de publicación de todos los libros.

**Parámetros**:
- `catalog`: Lista del catálogo

**Retorna**: Año promedio como número flotante

**Funcionalidad**:
- Itera por todos los registros validando que tengan año válido
- Suma todos los años de publicación que sean números
- Calcula el promedio usando división entera
- Maneja el caso de catálogo vacío retornando 0

### 8. `informe_libros_viejos(catalog, year_cutoff: int) -> list`
**Propósito**: Filtra y retorna libros publicados antes de un año específico.

**Parámetros**:
- `catalog`: Lista del catálogo
- `year_cutoff`: Año límite para el filtro

**Retorna**: Lista de libros antiguos formateada

**Funcionalidad**:
- Filtra libros con año de publicación válido y menor al año de corte
- Utiliza `display_catalog` para formatear la salida
- Incluye validación de longitud de registro y formato de año

### 9. `informe_top_autores(catalog, top_n: int = 3) -> list`
**Propósito**: Retorna los autores más frecuentes en el catálogo.

**Parámetros**:
- `catalog`: Lista del catálogo
- `top_n`: Número de autores a retornar (por defecto 3)

**Retorna**: Lista de tuplas (autor, cantidad) ordenada descendentemente

**Funcionalidad**:
- Utiliza `cantidad_ordenada_por_categoria_desc` para obtener autores ordenados
- Limita el resultado a los primeros `top_n` autores
- Maneja el caso de catálogo vacío

### 10. `insertion_sort_tuple_desc(counter: list) -> list`
**Propósito**: Implementa el algoritmo de ordenamiento por inserción para tuplas en orden descendente.

**Parámetros**:
- `counter`: Lista de tuplas a ordenar

**Retorna**: Lista ordenada descendentemente por el segundo elemento de cada tupla

**Funcionalidad**:
- Implementación manual del algoritmo insertion sort
- Ordena por el segundo elemento de las tuplas (cantidad)
- Orden descendente (mayor a menor)
- Algoritmo eficiente para listas pequeñas a medianas

### 11. `cantidad_ordenada_por_categoria_desc(catalog: list, index_categoria) -> list`
**Propósito**: Cuenta elementos por categoría y los ordena descendentemente.

**Parámetros**:
- `catalog`: Lista del catálogo
- `index_categoria`: Índice de la categoría a analizar

**Retorna**: Lista de tuplas (categoría, cantidad) ordenada

**Funcionalidad**:
- Extrae todas las categorías únicas del catálogo
- Cuenta la frecuencia de cada categoría
- Crea tuplas (categoría, cantidad)
- Utiliza `insertion_sort_tuple_desc` para ordenar
- Función genérica que funciona con cualquier índice de categoría



### 13. `guardar_resumen_json(nombre_archivo: str, catalog: list) -> None`
**Propósito**: Genera un resumen completo del catálogo y lo exporta en formato JSON.

**Parámetros**:
- `nombre_archivo`: Nombre del archivo JSON de salida
- `catalog`: Lista del catálogo

**Retorna**: None (crea archivo)

**Funcionalidad**:
- Genera estadísticas de géneros usando `cantidad_ordenada_por_categoria_desc`
- Calcula estadísticas de años de publicación
- Identifica el libro más reciente y más antiguo
- Crea un diccionario con resumen completo
- Exporta a JSON con formato legible (indentado)
- Mantiene caracteres especiales con `ensure_ascii=False`

### 14. `display_catalog(catalog: list, limit: int) -> list`
**Propósito**: Formatea y limita la visualización del catálogo para mostrar información esencial.

**Parámetros**:
- `catalog`: Lista del catálogo completo
- `limit`: Número máximo de libros a procesar

**Retorna**: Lista formateada con información básica de los libros

**Funcionalidad**:
- Extrae información esencial: título, autor, año, género
- Limita el número de registros según el parámetro `limit`
- Crea una estructura simplificada para visualización
- Optimiza la presentación de datos al usuario

## Arquitectura y Patrones de Diseño

### **Separación de Responsabilidades**
- **Funciones de datos**: Carga y persistencia (`get_catalog`, `add_book_manual`)
- **Funciones de validación**: Verificación de entrada (`check_entry_int`)
- **Funciones de análisis**: Cálculos y estadísticas (`informe_*`)
- **Funciones de utilidad**: Ordenamiento y formateo (`insertion_sort_*`, `display_catalog`)
- **Funciones de exportación**: Generación de reportes (`guardar_resumen_json`)

### **Algoritmos Implementados**
1. **Insertion Sort**: Para ordenar tuplas por frecuencia

### **Características Técnicas**
- **Manejo de archivos**: CSV para persistencia, JSON para exportación
- **Validación robusta**: Verificación de longitud de registros y tipos de datos
- **Normalización de datos**: Consistencia en mayúsculas/minúsculas

### **Extensibilidad**
- Los índices constantes facilitan cambios en la estructura de datos
- Las funciones genéricas (`cantidad_ordenada_por_categoria_desc`) permiten análisis de diferentes campos
- La separación clara de responsabilidades facilita el mantenimiento y extensión

## Notas Técnicas
- Utiliza encoding UTF-8 para soporte de caracteres especiales
- Implementa validaciones para evitar errores por datos inconsistentes
- Las funciones de ordenamiento modifican listas in-place cuando es apropiado
- El manejo de archivos incluye contexto adecuado (with statements)
- La exportación JSON mantiene legibilidad con formato indentado
