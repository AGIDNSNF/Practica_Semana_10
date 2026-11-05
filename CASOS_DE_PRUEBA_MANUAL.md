# Casos de Prueba Manual

## Sistema de Gestión de Productos - Semana 10

**Universidad Nacional del Centro del Perú**  
**Facultad de Ingeniería de Sistemas**

---

## Propósito

Este documento contiene casos de prueba manual para verificar el funcionamiento correcto del sistema más allá de las pruebas automatizadas. Úsalo para validar la experiencia del usuario y el comportamiento del sistema en escenarios realistas.

---

## Instrucciones Generales

1. Ejecutar `python main.py` antes de cada caso de prueba
2. Seguir los pasos exactamente como se describen
3. Comparar el resultado obtenido con el resultado esperado
4. Marcar ✓ si pasa, ✗ si falla
5. Anotar cualquier comportamiento inesperado

---

## Caso de Prueba 1: Registro Completo de Productos

**Objetivo:** Verificar el registro exitoso de múltiples productos de diferentes categorías.

**Precondiciones:** Sistema iniciado con inventario vacío.

**Pasos:**

1. Seleccionar opción `1`
2. Ingresar:
   - Categoría: `Electronico`
   - Nombre: `Laptop Dell Inspiron`
   - Precio base: `3500`
   - Stock: `15`
   - Garantía: `24`
3. Verificar mensaje de confirmación con ID 1
4. Seleccionar opción `1` nuevamente
5. Ingresar:
   - Categoría: `Libro`
   - Nombre: `El Principito`
   - Precio base: `45`
   - Stock: `50`
   - Autor: `Antoine de Saint-Exupéry`
   - ¿Es libro de texto?: `n`
6. Verificar mensaje de confirmación con ID 2
7. Seleccionar opción `2` (Listar)
8. Verificar que ambos productos aparecen

**Resultado Esperado:**
```
ID: 1 | [Electronico] Laptop Dell Inspiron | S/ 3500.00 | Stock: 15 | Garantía: 24 meses
ID: 2 | [Libro] El Principito | S/ 45.00 | Stock: 50 | Autor: Antoine de Saint-Exupéry | Tipo: Libro general
```

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 2: Cálculo de Precio con IGV

**Objetivo:** Verificar el cálculo correcto del precio con IGV para productos electrónicos.

**Precondiciones:** Producto electrónico con stock ≤ 50 registrado.

**Pasos:**

1. Agregar producto:
   - Categoría: `Electronico`
   - Nombre: `Mouse Logitech`
   - Precio base: `100`
   - Stock: `20`
   - Garantía: `6`
2. Seleccionar opción `3`
3. Ingresar ID del producto registrado
4. Verificar precio final

**Resultado Esperado:**
```
Precio base: S/ 100.00
Precio final: S/ 118.00
```

**Cálculo Manual:**
- Precio base: S/ 100.00
- IGV (18%): S/ 100 × 1.18 = S/ 118.00
- Stock: 20 (≤ 50, sin descuento adicional)
- **Precio final: S/ 118.00** ✓

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 3: Descuento por Stock Alto

**Objetivo:** Verificar que se aplica descuento del 5% cuando stock > 50.

**Precondiciones:** Ninguna.

**Pasos:**

1. Agregar producto:
   - Categoría: `Electronico`
   - Nombre: `Cable USB`
   - Precio base: `20`
   - Stock: `75`
   - Garantía: `3`
2. Calcular precio final

**Resultado Esperado:**
```
Precio base: S/ 20.00
Precio final: S/ 22.42
```

**Cálculo Manual:**
- Precio base: S/ 20.00
- Con IGV: S/ 20 × 1.18 = S/ 23.60
- Descuento 5%: S/ 23.60 × 0.95 = S/ 22.42
- **Precio final: S/ 22.42** ✓

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 4: Stock Exactamente en el Umbral

**Objetivo:** Verificar que con stock = 50 NO se aplica descuento.

**Precondiciones:** Ninguna.

**Pasos:**

1. Agregar producto:
   - Categoría: `Electronico`
   - Nombre: `Teclado Mecánico`
   - Precio base: `200`
   - Stock: `50`
   - Garantía: `12`
2. Calcular precio final

**Resultado Esperado:**
```
Precio base: S/ 200.00
Precio final: S/ 236.00
```

**Cálculo Manual:**
- Precio base: S/ 200.00
- Con IGV: S/ 200 × 1.18 = S/ 236.00
- Stock: 50 (no es > 50, sin descuento)
- **Precio final: S/ 236.00** ✓

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 5: Descuento para Libro de Texto

**Objetivo:** Verificar el descuento del 10% para libros de texto.

**Precondiciones:** Ninguna.

**Pasos:**

1. Agregar producto:
   - Categoría: `Libro`
   - Nombre: `Cálculo de una Variable`
   - Precio base: `150`
   - Stock: `40`
   - Autor: `James Stewart`
   - ¿Es libro de texto?: `s`
2. Calcular precio final

**Resultado Esperado:**
```
Precio base: S/ 150.00
Precio final: S/ 135.00
```

**Cálculo Manual:**
- Precio base: S/ 150.00
- Descuento 10%: S/ 150 × 0.90 = S/ 135.00
- **Precio final: S/ 135.00** ✓

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 6: Libro General Sin Descuento

**Objetivo:** Verificar que libros NO de texto mantienen el precio base.

**Precondiciones:** Ninguna.

**Pasos:**

1. Agregar producto:
   - Categoría: `Libro`
   - Nombre: `Don Quijote de la Mancha`
   - Precio base: `85`
   - Stock: `12`
   - Autor: `Miguel de Cervantes`
   - ¿Es libro de texto?: `n`
2. Calcular precio final

**Resultado Esperado:**
```
Precio base: S/ 85.00
Precio final: S/ 85.00
```

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 7: ValidationError - Precio Negativo

**Objetivo:** Verificar que se rechaza un precio negativo.

**Precondiciones:** Ninguna.

**Pasos:**

1. Seleccionar opción `1`
2. Ingresar:
   - Categoría: `Electronico`
   - Nombre: `Producto Test`
   - Precio base: `-100`
3. Observar mensaje de error

**Resultado Esperado:**
```
✗ Error de validación: El valor debe ser mayor o igual a 0.01.
```

**Verificación Adicional:**
- El producto NO debe agregarse al inventario
- El sistema debe permitir continuar operando
- El menú debe mostrarse nuevamente

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 8: ValidationError - Stock Decimal

**Objetivo:** Verificar que se rechaza un stock con decimales.

**Precondiciones:** Ninguna.

**Pasos:**

1. Agregar producto con:
   - Stock: `15.5`
2. Observar mensaje de error

**Resultado Esperado:**
```
✗ Error de validación: El stock debe ser un número entero, no decimal.
```

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 9: ValidationError - Categoría Inválida

**Objetivo:** Verificar que se rechaza una categoría no reconocida.

**Precondiciones:** Ninguna.

**Pasos:**

1. Agregar producto con:
   - Categoría: `Ropa`
2. Observar mensaje de error

**Resultado Esperado:**
```
✗ Error de validación: Categoría inválida: 'Ropa'. Las categorías válidas son: Electronico, Libro.
```

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 10: Normalización de Categoría

**Objetivo:** Verificar que la categoría se normaliza correctamente.

**Precondiciones:** Ninguna.

**Pasos:**

1. Probar cada variación:
   - `electronico`
   - `ELECTRONICO`
   - `Electrónico`
   - `electrónico`
   - `libro`
   - `LIBRO`
2. Verificar que todas se aceptan
3. Listar productos
4. Verificar formato canónico: `[Electronico]` o `[Libro]`

**Resultado Esperado:**
Todas las variaciones deben aceptarse y normalizarse correctamente.

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 11: NotFoundError - ID Inexistente

**Objetivo:** Verificar manejo de búsqueda de producto inexistente.

**Precondiciones:** Inventario con productos con IDs 1, 2, 3.

**Pasos:**

1. Seleccionar opción `3`
2. Ingresar ID: `999`
3. Observar mensaje de error

**Resultado Esperado:**
```
✗ No encontrado: No existe un producto con ID 999.
```

**Verificación Adicional:**
- El sistema debe continuar funcionando
- No debe producirse un error fatal

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 12: ValidationError - Opción de Menú Inválida

**Objetivo:** Verificar que se rechaza una opción no existente.

**Precondiciones:** Sistema en menú principal.

**Pasos:**

1. Ingresar opción: `9`
2. Observar mensaje de error
3. Verificar que el menú se muestra nuevamente

**Resultado Esperado:**
```
✗ Error de validación: Opción '9' no válida. Seleccione una opción entre 1 y 4.
```

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 13: Inventario Vacío

**Objetivo:** Verificar el comportamiento cuando no hay productos registrados.

**Precondiciones:** Inventario vacío.

**Pasos:**

1. Seleccionar opción `2` (Listar)
2. Observar mensaje

**Resultado Esperado:**
```
--- INVENTARIO ---
No hay productos registrados.
```

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 14: Salida Normal del Sistema

**Objetivo:** Verificar que el sistema se cierra correctamente.

**Precondiciones:** Sistema en ejecución.

**Pasos:**

1. Seleccionar opción `4`
2. Observar mensaje de despedida
3. Verificar que el programa termina

**Resultado Esperado:**
```
==================================================
Cerrando sistema...
Gracias por utilizar el Sistema de Gestión de Productos.
==================================================
```

El programa debe finalizar sin errores.

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 15: Validación de Garantía Mínima

**Objetivo:** Verificar que se acepta garantía de 1 mes y se rechaza 0.

**Precondiciones:** Ninguna.

**Pasos:**

1. Agregar producto electrónico con garantía: `1`
   - Debe aceptarse ✓
2. Intentar agregar con garantía: `0`
   - Debe rechazarse con ValidationError ✗

**Resultado Esperado:**
- Garantía 1: Aceptada
- Garantía 0: `✗ Error de validación: La garantía debe ser de al menos 1 mes.`

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 16: Nombres con Espacios

**Objetivo:** Verificar que se manejan correctamente los espacios.

**Precondiciones:** Ninguna.

**Pasos:**

1. Agregar producto con nombre: `   Laptop Gaming   `
2. Listar productos
3. Verificar que el nombre se muestra sin espacios extras: `Laptop Gaming`

**Resultado Esperado:**
El sistema debe eliminar espacios al inicio y final (strip).

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 17: Nombres Vacíos

**Objetivo:** Verificar que se rechaza un nombre vacío.

**Precondiciones:** Ninguna.

**Pasos:**

1. Intentar agregar producto con:
   - Nombre: (dejar vacío, solo Enter)
2. Observar error

**Resultado Esperado:**
```
✗ Error de validación: El nombre no puede estar vacío.
```

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 18: Autor Vacío

**Objetivo:** Verificar que se rechaza un autor vacío para libros.

**Precondiciones:** Ninguna.

**Pasos:**

1. Agregar libro con:
   - Autor: (dejar vacío)
2. Observar error

**Resultado Esperado:**
```
✗ Error de validación: El autor no puede estar vacío.
```

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 19: Stock Cero Válido

**Objetivo:** Verificar que se acepta stock = 0 (producto agotado).

**Precondiciones:** Ninguna.

**Pasos:**

1. Agregar producto con stock: `0`
2. Verificar que se acepta
3. Listar productos
4. Verificar que aparece con Stock: 0

**Resultado Esperado:**
El sistema debe aceptar stock = 0 como válido.

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Caso de Prueba 20: Secuencia Completa de Uso

**Objetivo:** Verificar un flujo completo y realista de uso del sistema.

**Precondiciones:** Sistema recién iniciado.

**Pasos:**

1. Agregar 3 productos diferentes:
   - 1 electrónico con stock bajo
   - 1 electrónico con stock alto
   - 1 libro de texto
2. Listar todos los productos
3. Calcular precio de cada uno
4. Intentar buscar un ID inexistente
5. Intentar agregar un producto con datos inválidos
6. Salir del sistema

**Resultado Esperado:**
- Todos los productos se registran correctamente
- Los precios se calculan según las reglas de negocio
- Los errores se manejan adecuadamente
- El sistema permanece estable durante toda la sesión

**Estado:** [ ] Pasa  [ ] Falla

**Observaciones:**
______________________________________________________________________

---

## Resumen de Resultados

| Caso | Descripción | Estado |
|------|-------------|--------|
| CP-01 | Registro completo | [ ] Pasa [ ] Falla |
| CP-02 | Cálculo con IGV | [ ] Pasa [ ] Falla |
| CP-03 | Descuento stock alto | [ ] Pasa [ ] Falla |
| CP-04 | Stock en umbral | [ ] Pasa [ ] Falla |
| CP-05 | Descuento libro texto | [ ] Pasa [ ] Falla |
| CP-06 | Libro sin descuento | [ ] Pasa [ ] Falla |
| CP-07 | ValidationError precio | [ ] Pasa [ ] Falla |
| CP-08 | ValidationError stock | [ ] Pasa [ ] Falla |
| CP-09 | ValidationError categoría | [ ] Pasa [ ] Falla |
| CP-10 | Normalización | [ ] Pasa [ ] Falla |
| CP-11 | NotFoundError | [ ] Pasa [ ] Falla |
| CP-12 | Opción inválida | [ ] Pasa [ ] Falla |
| CP-13 | Inventario vacío | [ ] Pasa [ ] Falla |
| CP-14 | Salida normal | [ ] Pasa [ ] Falla |
| CP-15 | Garantía mínima | [ ] Pasa [ ] Falla |
| CP-16 | Espacios en nombres | [ ] Pasa [ ] Falla |
| CP-17 | Nombre vacío | [ ] Pasa [ ] Falla |
| CP-18 | Autor vacío | [ ] Pasa [ ] Falla |
| CP-19 | Stock cero | [ ] Pasa [ ] Falla |
| CP-20 | Flujo completo | [ ] Pasa [ ] Falla |

**Total de casos:** 20  
**Casos pasados:** ___  
**Casos fallados:** ___  
**Porcentaje de éxito:** ___%

---

## Notas Finales

- Estos casos complementan las 83 pruebas unitarias automatizadas
- Cubren aspectos de experiencia de usuario no capturados por tests
- Deben ejecutarse manualmente antes de la entrega
- Cualquier falla debe investigarse y corregirse
- Documentar cualquier comportamiento inesperado

**Probado por:**
- Nombre: _______________
- Fecha: _______________
- Firma: _______________

---

**Universidad Nacional del Centro del Perú**  
**Facultad de Ingeniería de Sistemas**  
**Curso:** Desarrollo de Aplicaciones Web (IS093A)  
**Semana 10 - 2026**
