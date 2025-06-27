# Documentación del Sistema de Biblioteca - biblioteca.py

## Descripción General
El archivo `biblioteca.py` es el módulo principal de un sistema de gestión de biblioteca que proporciona una interfaz de usuario por consola para administrar un catálogo de libros. Este sistema permite realizar diversas operaciones como agregar libros, consultar informes estadísticos, y exportar datos.

## Dependencias
El módulo importa las siguientes funciones del módulo `funciones`:
- `get_catalog`: Obtiene el catálogo de libros
- `add_book_manual`: Añade un libro manualmente al catálogo
- `informe_total_ejemplares`: Calcula el total de ejemplares
- `informe_por_genero`: Genera informe por género
- `informe_promedio_anio`: Calcula el año promedio de publicación
- `informe_libros_viejos`: Filtra libros por año de publicación
- `informe_top_autores`: Lista los autores más frecuentes
- `guardar_resumen_json`: Exporta resumen en formato JSON
- `check_entry_int`: Valida entrada de números enteros
- `get_genero`: Obtiene lista de géneros disponibles
- `display_catalog`: Muestra el catálogo con límite

## Funciones del Sistema

### 1. `send_message(message: str, expected_type: type) -> None`
**Propósito**: Función utilitaria para solicitar y validar entrada del usuario.

**Parámetros**:
- `message`: Mensaje a mostrar al usuario
- `expected_type`: Tipo de dato esperado (int o str)

**Funcionalidad**:
- Solicita entrada del usuario con el mensaje proporcionado
- Valida que la entrada corresponda al tipo esperado
- Permite al usuario salir ingresando '0'
- Para enteros: verifica que sea un número válido
- Para strings: verifica que no esté vacío
- Continúa pidiendo entrada hasta obtener un valor válido

### 2. `handle_promedio_anio(catalog: list) -> None`
**Propósito**: Calcula y muestra el año promedio de publicación de todos los libros en el catálogo.

**Parámetros**:
- `catalog`: Lista del catálogo de libros

**Funcionalidad**:
- Llama a `informe_promedio_anio()` para calcular el promedio
- Maneja el caso cuando no hay años válidos (retorna 0)
- Muestra el resultado formateado al usuario

### 3. `handle_informe_libros_viejos(catalog: list) -> None`
**Propósito**: Permite al usuario buscar y mostrar libros publicados antes de un año específico.

**Parámetros**:
- `catalog`: Lista del catálogo de libros

**Funcionalidad**:
- Solicita al usuario un año de corte
- Filtra libros publicados antes de ese año
- Muestra los resultados en formato numerado con título, autor, año y género
- Maneja el caso cuando no se encuentran libros que cumplan el criterio

### 4. `handle_top_autores(catalog: list) -> None`
**Propósito**: Muestra los autores más frecuentes en el catálogo.

**Parámetros**:
- `catalog`: Lista del catálogo de libros

**Funcionalidad**:
- Obtiene la lista de autores ordenados por frecuencia
- Muestra cada autor con su cantidad de libros
- Maneja el caso cuando no hay autores en el catálogo

### 5. `handle_catalogo(catalog: list) -> None`
**Propósito**: Permite al usuario ver el catálogo completo con un límite especificado de libros a mostrar.

**Parámetros**:
- `catalog`: Lista del catálogo de libros

**Funcionalidad**:
- Solicita al usuario cuántos libros mostrar
- Presenta los libros en formato numerado con información básica
- Controla la cantidad de libros mostrados según el límite especificado

### 6. `handle_informe_genero(catalog: list) -> None`
**Propósito**: Permite consultar el total de libros de un género específico.

**Parámetros**:
- `catalog`: Lista del catálogo de libros

**Funcionalidad**:
- Muestra todos los géneros disponibles en el catálogo
- Solicita al usuario seleccionar un género
- Cuenta y muestra el total de ejemplares de ese género
- Maneja casos cuando el género no existe o no hay géneros disponibles

### 7. `handle_add_book_manual(catalog: list) -> None`
**Propósito**: Permite al usuario agregar un nuevo libro al catálogo de forma interactiva.

**Parámetros**:
- `catalog`: Lista del catálogo de libros

**Funcionalidad**:
- Solicita los datos del libro: título, autor, año de publicación y género
- Permite cancelar la operación en cualquier momento con '0'
- Crea un nuevo registro de libro con formato específico
- Añade el libro al catálogo y lo guarda en el archivo CSV
- Confirma la operación al usuario

### 8. `handle_total_ejemplares(catalog: list) -> None`
**Propósito**: Muestra el total de ejemplares en todo el catálogo.

**Parámetros**:
- `catalog`: Lista del catálogo de libros

**Funcionalidad**:
- Calcula y muestra el número total de ejemplares en el catálogo
- Proporciona un resumen rápido del tamaño de la colección

### 9. `handle_guardar_resumen_json(catalog: list, filename: str = "resumen.json") -> None`
**Propósito**: Exporta un resumen del catálogo en formato JSON.

**Parámetros**:
- `catalog`: Lista del catálogo de libros
- `filename`: Nombre del archivo JSON (por defecto "resumen.json")

**Funcionalidad**:
- Genera y guarda un archivo JSON con el resumen del catálogo
- Confirma al usuario que el archivo fue guardado exitosamente

### 10. `show_main_menu() -> None`
**Propósito**: Muestra el menú principal de opciones del sistema.

**Funcionalidad**:
- Presenta todas las opciones disponibles numeradas del 1 al 8
- Incluye opción de salida (0)
- Interfaz clara y organizada para la navegación del usuario

### 11. `menu() -> None`
**Propósito**: Función principal que controla el flujo del programa y maneja la interacción con el usuario.

**Funcionalidad**:
- Carga el catálogo inicial
- Presenta el menú principal en un bucle continuo
- Procesa la selección del usuario y ejecuta la función correspondiente
- Maneja opciones inválidas
- Permite al usuario realizar múltiples operaciones o salir del sistema
- Controla el flujo completo de la aplicación

### 12. `main() -> None`
**Propósito**: Función de entrada principal del programa.

**Funcionalidad**:
- Punto de entrada del sistema
- Inicializa la aplicación llamando a `menu()`

## Flujo de Ejecución
1. El programa inicia en `main()` 
2. Se llama a `menu()` que carga el catálogo
3. Se muestra el menú principal
4. El usuario selecciona una opción
5. Se ejecuta la función correspondiente (`handle_*`)
6. Se pregunta si desea realizar otra operación
7. El ciclo continúa hasta que el usuario decide salir

