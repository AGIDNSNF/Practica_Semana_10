# Evidencias de Ejecución

Este directorio contiene las evidencias requeridas para la evaluación de la práctica.

## Evidencias Requeridas

### Evidencia 1: Caso Exitoso
**Descripción:** Registro de un producto y cálculo de precio final.

**Pasos para capturar:**
1. Ejecutar `python main.py`
2. Seleccionar opción `1` (Agregar Producto)
3. Ingresar datos válidos de un producto electrónico
4. Seleccionar opción `3` (Calcular Precio Final)
5. Ingresar el ID del producto registrado
6. Capturar pantalla mostrando el resultado del cálculo

**Ejemplo de ejecución:**
```
=== GESTIÓN DE PRODUCTOS (CLI) ===
1. Agregar Producto
2. Listar Productos
3. Calcular Precio Final
4. Salir
Opción > 1

--- AGREGAR PRODUCTO ---
Categoría (Electronico/Libro): Electronico
Nombre: Laptop HP
Precio base (S/): 2500
Stock: 10
Garantía en meses: 12

✓ Producto registrado correctamente.
  ID asignado: 1

Opción > 3

--- CALCULAR PRECIO FINAL ---
Ingrese el ID del producto: 1

==================================================
=== CÁLCULO DE PRECIO FINAL ===
==================================================
ID: 1
Producto: Laptop HP
Categoría: Electronico
Precio base: S/ 2500.00
Precio final: S/ 2950.00
==================================================
```

---

### Evidencia 2: ValidationError
**Descripción:** Error de validación al ingresar datos inválidos.

**Pasos para capturar:**
1. Ejecutar `python main.py`
2. Seleccionar opción `1` (Agregar Producto)
3. Ingresar un precio negativo o stock inválido
4. Observar el mensaje de error `ValidationError`
5. Capturar pantalla mostrando el error

**Ejemplo de ejecución:**
```
--- AGREGAR PRODUCTO ---
Categoría (Electronico/Libro): Electronico
Nombre: Mouse
Precio base (S/): -50

✗ Error de validación: El valor debe ser mayor o igual a 0.01.
```

**Otro ejemplo:**
```
--- AGREGAR PRODUCTO ---
Categoría (Electronico/Libro): Hardware

✗ Error de validación: Categoría inválida: 'Hardware'. Las categorías válidas son: Electronico, Libro.
```

---

### Evidencia 3: NotFoundError
**Descripción:** Error al buscar un producto inexistente.

**Pasos para capturar:**
1. Ejecutar `python main.py`
2. Seleccionar opción `3` (Calcular Precio Final)
3. Ingresar un ID que no existe en el inventario
4. Observar el mensaje de error `NotFoundError`
5. Capturar pantalla mostrando el error

**Ejemplo de ejecución:**
```
--- CALCULAR PRECIO FINAL ---
Ingrese el ID del producto: 999

✗ No encontrado: No existe un producto con ID 999.
```

---

## Instrucciones para Captura

### Método 1: Captura de Pantalla
1. Ejecutar el programa en CMD o PowerShell
2. Realizar las acciones descritas
3. Presionar `Win + Shift + S` para captura parcial
4. Guardar la imagen en este directorio con nombres:
   - `evidencia_1_exito.png`
   - `evidencia_2_validation_error.png`
   - `evidencia_3_not_found_error.png`

### Método 2: Copia de Terminal
También puede copiar el texto completo de la terminal y guardarlo en archivos `.txt`:
- `evidencia_1_exito.txt`
- `evidencia_2_validation_error.txt`
- `evidencia_3_not_found_error.txt`

---

## Verificación de Completitud

- [ ] Evidencia 1: Caso exitoso capturado
- [ ] Evidencia 2: ValidationError capturado
- [ ] Evidencia 3: NotFoundError capturado
- [ ] Imágenes o archivos guardados en este directorio
- [ ] Referencias actualizadas en el README principal

---

## Notas Adicionales

Las evidencias son fundamentales para demostrar el correcto funcionamiento del sistema y el cumplimiento de los requisitos de la guía práctica.

Asegúrese de que las capturas sean legibles y muestren claramente:
- Los comandos ingresados
- Los mensajes del sistema
- Los tipos de excepciones capturadas
- El formato de salida de los datos

**Universidad Nacional del Centro del Perú**  
**Facultad de Ingeniería de Sistemas**  
**Curso:** Desarrollo de Aplicaciones Web (IS093A)  
**Práctica:** Semana 10
