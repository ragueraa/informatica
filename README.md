# Sistema de Gestión de Biblioteca

## Descripción
Sistema de gestión de biblioteca que permite administrar un catálogo de libros a través de una interfaz de consola. El sistema puede cargar datos desde archivos CSV, generar informes estadísticos y exportar resúmenes en formato JSON.

## Requisitos
- Python 3.x
- Archivo `libros.csv` en el directorio del proyecto (se crea automáticamente al agregar libros)

## Instalación y Ejecución

### 1. Ejecutar el programa
```bash
python biblioteca.py
```

### 2. Estructura de archivos necesaria
```
informatica/
├── biblioteca.py          # Archivo principal
├── funciones.py          # Módulo de funciones
├── libros.csv           # Base de datos de libros (se crea automáticamente)
└── resumen.json         # Archivo de resumen (se genera al usar opción 8)
```

## Uso del Sistema

Al ejecutar el programa, se mostrará un menú con las siguientes opciones:

### Menú Principal
```
Menú:
1. Añadir libro manualmente
2. Informe total de ejemplares
3. Informe por género
4. Informe promedio de año
5. Informe libros viejos
6. Informe top autores
7. Mostrar catálogo
8. Resumen de catálogo en JSON
0. Salir
```

### Descripción de Opciones

#### **1. Añadir libro manualmente**
- Permite agregar un nuevo libro al catálogo
- Solicita: título, autor, año de publicación y género
- El libro se guarda automáticamente en `libros.csv`
- **Nota**: Puedes presionar `0` en cualquier momento para cancelar

#### **2. Informe total de ejemplares**
- Muestra el número total de libros en el catálogo
- Operación instantánea sin entrada adicional

#### **3. Informe por género**
- Muestra todos los géneros disponibles en el catálogo
- Permite seleccionar un género específico
- Muestra el total de libros de ese género

#### **4. Informe promedio de año**
- Calcula y muestra el año promedio de publicación de todos los libros
- No requiere entrada adicional

#### **5. Informe libros viejos**
- Solicita un año de corte
- Muestra todos los libros publicados antes de ese año
- Lista detallada con título, autor, año y género

#### **6. Informe top autores**
- Muestra los 3 autores más frecuentes en el catálogo
- Incluye el número de libros por autor

#### **7. Mostrar catálogo**
- Solicita cuántos libros mostrar
- Presenta una lista numerada del catálogo
- Información mostrada: título, autor, año, género

#### **8. Resumen de catálogo en JSON**
- Genera un archivo `resumen.json` con estadísticas completas
- Incluye: total de libros, libro más antiguo, más reciente, y cantidad por género

#### **0. Salir**
- Termina la ejecución del programa

## Funcionalidades Especiales

### **Cancelación de Operaciones**
- En cualquier momento durante la entrada de datos, puedes escribir `0` para cancelar y volver al menú principal

### **Validación de Entrada**
- El sistema valida automáticamente los tipos de datos
- Para números: solo acepta enteros válidos
- Para texto: no acepta entradas vacías

### **Continuación de Operaciones**
- Después de cada operación, el sistema pregunta si deseas realizar otra operación
- Responde `s` para continuar o `n` para salir

## Ejemplos de Uso

### Ejemplo 1: Agregar un libro
```
Selecciona una opción: 1
Añadiendo un nuevo libro al catálogo...
Presiona 0 en cualquier momento para salir.
Título del libro: El Quijote
Autor: Miguel de Cervantes
Año de publicación: 1605
Género: Novela
Libro 'El Quijote' añadido al catálogo y guardado en 'libros.csv'.
```

### Ejemplo 2: Consultar por género
```
Selecciona una opción: 3
Los géneros disponibles son: Novela, Ciencia Ficción, Fantasía
Ingrese el género a buscar: Novela
El género 'Novela' tiene un total de 5 ejemplares.
```

### Ejemplo 3: Ver libros antiguos
```
Selecciona una opción: 5
Mostrar libros anteriores a qué año?: 1900

----- Libros publicados antes de 1900: ----
1. Título: Don Quijote de la Mancha, Autor: Miguel de Cervantes, Año: 1605, Género: Novela
2. Título: Orgullo y Prejuicio, Autor: Jane Austen, Año: 1813, Género: Romance
----------------
```

## Notas Importantes

1. **Archivo CSV**: Se crea automáticamente al agregar el primer libro
2. **Codificación**: El sistema maneja caracteres especiales (UTF-8)
3. **Persistencia**: Todos los cambios se guardan automáticamente
4. **Formato de datos**: El sistema mantiene un formato consistente para todos los registros

## Solución de Problemas

### Error: "No such file or directory: 'libros.csv'"
- **Solución**: Agrega al menos un libro usando la opción 1 para crear el archivo

### Error de entrada inválida
- **Solución**: Asegúrate de ingresar el tipo de dato correcto (número o texto según se solicite)

### El programa no responde
- **Solución**: Presiona `Ctrl+C` para terminar y reinicia el programa

## Contacto y Soporte
Para reportar problemas o sugerencias, consulta la documentación técnica en los archivos de documentación incluidos en el proyecto.
