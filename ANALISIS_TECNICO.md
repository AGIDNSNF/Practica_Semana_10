# Análisis Técnico - Sistema de Gestión de Productos

## Universidad Nacional del Centro del Perú
**Facultad de Ingeniería de Sistemas**  
**Curso:** Desarrollo de Aplicaciones Web (IS093A)  
**Práctica:** Semana 10

---

## Índice

1. [Arquitectura del Sistema](#arquitectura-del-sistema)
2. [Patrones de Diseño Aplicados](#patrones-de-diseño-aplicados)
3. [Análisis de Complejidad](#análisis-de-complejidad)
4. [Principios SOLID](#principios-solid)
5. [Validación de Datos](#validación-de-datos)
6. [Manejo de Memoria](#manejo-de-memoria)
7. [Extensibilidad](#extensibilidad)
8. [Alternativas de Implementación](#alternativas-de-implementación)

---

## 1. Arquitectura del Sistema

### 1.1. Separación en Capas

El sistema sigue una arquitectura en capas simplificada:

```
┌─────────────────────────────────────┐
│   Capa de Presentación (CLI)       │
│   main.py                           │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│   Capa de Lógica de Negocio        │
│   models/producto.py                │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│   Capa de Utilidades                │
│   utils/validators.py               │
│   utils/exceptions.py               │
└─────────────────────────────────────┘
```

**Ventajas:**
- Bajo acoplamiento entre capas
- Fácil mantenimiento
- Testabilidad mejorada
- Reutilización de componentes

### 1.2. Flujo de Datos

```
Usuario → Input → Validación → Modelo → Cálculo → Output → Usuario
          ↓         ↓            ↓         ↓        ↓
       main.py  validators  producto.py  métodos  main.py
```

### 1.3. Gestión del Inventario

**Decisión:** Diccionario `Dict[int, Producto]`

**Análisis de alternativas:**

| Estructura | Búsqueda | Inserción | Espacio | Ordenamiento |
|------------|----------|-----------|---------|--------------|
| Diccionario | O(1) | O(1) | O(n) | No nativo |
| Lista | O(n) | O(1) | O(n) | O(n log n) |
| Lista ordenada | O(log n) | O(n) | O(n) | Mantenido |

**Justificación:** La búsqueda por ID es la operación más frecuente (opción 3 del menú), por lo que O(1) del diccionario es óptimo.

---

## 2. Patrones de Diseño Aplicados

### 2.1. Template Method (Implícito)

La clase `Producto` define el esquema general:

```python
class Producto:
    def __init__(self, nombre, precio_base, stock):
        # Validaciones comunes
        ...
    
    def calcular_precio_final(self):
        # Método abstracto: subclases lo implementan
        raise NotImplementedError
```

Las subclases completan los pasos específicos:

```python
class Electronico(Producto):
    def calcular_precio_final(self):
        # Implementación específica
        ...
```

### 2.2. Property Pattern

Uso de propiedades para encapsular validación:

```python
@property
def precio_base(self) -> float:
    return self.__precio_base

@precio_base.setter
def precio_base(self, valor: Union[int, float]) -> None:
    # Validación centralizada
    if valor <= 0:
        raise ValidationError(...)
    self.__precio_base = float(valor)
```

**Ventajas:**
- Sintaxis natural de acceso
- Validación transparente
- Compatibilidad hacia atrás

### 2.3. Factory Method (Potencial)

Aunque no implementado explícitamente, el patrón podría aplicarse:

```python
class ProductoFactory:
    @staticmethod
    def crear_producto(categoria: str, **kwargs) -> Producto:
        if categoria == "Electronico":
            return Electronico(**kwargs)
        elif categoria == "Libro":
            return Libro(**kwargs)
        else:
            raise ValidationError(...)
```

**Cuándo usarlo:** Si se añaden más categorías (Ropa, Muebles, etc.)

### 2.4. Validator Pattern

Validadores separados en módulo independiente:

```python
def validar_numero(valor, tipo, min_val, max_val):
    # Lógica de validación reutilizable
    ...
```

**Ventajas:**
- Reutilización en múltiples contextos
- Fácil testing aislado
- Modificación centralizada

---

## 3. Análisis de Complejidad

### 3.1. Operaciones del Inventario

| Operación | Complejidad Temporal | Complejidad Espacial |
|-----------|---------------------|---------------------|
| Agregar producto | O(1) | O(1) por producto |
| Buscar por ID | O(1) | O(1) |
| Listar todos | O(n) | O(1) auxiliar |
| Calcular precio | O(1) | O(1) |

Donde **n** es el número de productos en el inventario.

### 3.2. Validaciones

| Validación | Complejidad |
|------------|-------------|
| validar_numero | O(1) |
| validar_categoria | O(1) con normalización O(k) donde k es longitud de la cadena |
| Setters de propiedades | O(1) |

### 3.3. Escalabilidad

**Escenario:** 10,000 productos en inventario

- **Agregar producto:** Instantáneo (O(1))
- **Buscar por ID:** Instantáneo (O(1))
- **Listar todos:** Lineal, aceptable para CLI (O(n))
- **Memoria:** Aproximadamente 10 MB (asumiendo ~1 KB por objeto)

**Conclusión:** La implementación es eficiente para el alcance del proyecto.

---

## 4. Principios SOLID

### 4.1. Single Responsibility Principle (SRP) ✓

Cada clase tiene una única responsabilidad:

- `Producto`: Modelar atributos comunes
- `Electronico`: Lógica específica de electrónicos
- `Libro`: Lógica específica de libros
- `validators`: Validación de datos
- `exceptions`: Definición de excepciones
- `main`: Orquestación del CLI

### 4.2. Open/Closed Principle (OCP) ✓

El sistema está abierto a extensión, cerrado a modificación:

**Ejemplo:** Agregar una nueva categoría "Ropa"

```python
class Ropa(Producto):
    def __init__(self, nombre, precio_base, stock, talla):
        super().__init__(nombre, precio_base, stock)
        self.talla = talla
    
    def calcular_precio_final(self):
        # Descuento del 15% en temporada
        return self.precio_base * 0.85
```

No requiere modificar `Producto` ni otras subclases.

### 4.3. Liskov Substitution Principle (LSP) ✓

Las subclases son intercambiables con la clase base:

```python
def mostrar_precio(producto: Producto):
    print(f"Precio: S/ {producto.calcular_precio_final()}")

# Funciona con cualquier subclase
mostrar_precio(Electronico(...))
mostrar_precio(Libro(...))
```

### 4.4. Interface Segregation Principle (ISP) ✓

No hay interfaces forzadas. Cada clase implementa solo lo necesario.

### 4.5. Dependency Inversion Principle (DIP) ⚠️

**Parcialmente aplicado:**

El código depende de la abstracción (`Producto`), pero `main.py` instancia clases concretas directamente.

**Mejora potencial:** Inyección de dependencias

```python
def agregar_producto(inventario, contador, factory):
    categoria = input(...)
    producto = factory.crear(categoria, ...)
    inventario[contador] = producto
```

---

## 5. Validación de Datos

### 5.1. Capas de Validación

El sistema valida en múltiples niveles:

```
Input del Usuario
       ↓
[Validación de Formato] (validators.py)
       ↓
[Validación Semántica] (setters en producto.py)
       ↓
[Validación de Negocio] (métodos de instancia)
       ↓
Dato Válido
```

### 5.2. Estrategias de Validación

#### Validación Defensiva

```python
def precio_base.setter(self, valor):
    # Rechazar booleanos explícitamente
    if isinstance(valor, bool):
        raise ValidationError(...)
    
    # Validar tipo
    if not isinstance(valor, (int, float)):
        raise ValidationError(...)
    
    # Validar rango
    if valor <= 0:
        raise ValidationError(...)
```

**Beneficio:** Previene estados inválidos en origen.

#### Validación por Tipos

```python
def validar_numero(
    valor: str,
    tipo: type = float,
    min_val: float = 0,
    max_val: Union[float, None] = None
) -> Union[int, float]:
```

**Beneficio:** Reutilizable, parametrizable.

### 5.3. Normalización de Datos

```python
def validar_categoria(categoria: str) -> str:
    # Remover espacios
    categoria = categoria.strip()
    
    # Normalizar mayúsculas
    categoria = categoria.lower()
    
    # Remover tildes
    categoria = unicodedata.normalize('NFD', categoria)
    categoria = ''.join(c for c in categoria if unicodedata.category(c) != 'Mn')
    
    # Mapear a forma canónica
    return categorias_validas.get(categoria)
```

**Beneficio:** Tolerante a variaciones de entrada del usuario.

---

## 6. Manejo de Memoria

### 6.1. Destructor `__del__()`

**Implementado con fines didácticos:**

```python
def __del__(self):
    logging.info(f"Destructor: Producto '{self.nombre}' eliminado de memoria.")
```

**Análisis crítico:**

| Aspecto | Evaluación |
|---------|------------|
| Determinismo | ❌ No garantizado |
| Momento de ejecución | ❌ Impredecible |
| Uso para limpieza crítica | ❌ No recomendado |
| Valor educativo | ✓ Demuestra concepto |

**Alternativa para limpieza real:**

```python
class Producto:
    def cerrar(self):
        # Limpieza explícita de recursos
        ...

# Uso
producto = Electronico(...)
try:
    # Usar producto
    ...
finally:
    producto.cerrar()
```

O mejor aún, context manager:

```python
class Producto:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Limpieza garantizada
        ...

# Uso
with Electronico(...) as producto:
    # Usar producto
    ...
```

### 6.2. Gestión del Inventario en Memoria

**Estado actual:** Diccionario en RAM

**Limitaciones:**
- Pérdida de datos al cerrar el programa
- No compartible entre sesiones

**Alternativas:**

1. **Persistencia en archivo JSON:**
```python
import json

def guardar_inventario(inventario, archivo="inventario.json"):
    data = {id: producto.to_dict() for id, producto in inventario.items()}
    with open(archivo, 'w') as f:
        json.dump(data, f)
```

2. **Base de datos SQLite:**
```python
import sqlite3

conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY,
        tipo TEXT,
        nombre TEXT,
        precio_base REAL,
        stock INTEGER
    )
''')
```

---

## 7. Extensibilidad

### 7.1. Agregar Nueva Categoría

**Pasos:**

1. Crear subclase de `Producto`
2. Implementar `calcular_precio_final()`
3. Actualizar validadores
4. Agregar caso en `main.py`

**Ejemplo: Categoría "Mueble"**

```python
# En models/producto.py
class Mueble(Producto):
    DESCUENTO_MAYORISTA = 0.20
    UMBRAL_MAYORISTA = 10
    
    def __init__(self, nombre, precio_base, stock, material):
        super().__init__(nombre, precio_base, stock)
        self.material = material
    
    def calcular_precio_final(self):
        if self.stock >= self.UMBRAL_MAYORISTA:
            return self.precio_base * (1 - self.DESCUENTO_MAYORISTA)
        return self.precio_base
```

```python
# En utils/validators.py
def validar_categoria(categoria: str) -> str:
    categorias_validas = {
        'electronico': 'Electronico',
        'libro': 'Libro',
        'mueble': 'Mueble'  # Nueva categoría
    }
    ...
```

### 7.2. Agregar Nuevas Validaciones

**Ejemplo: Validar email del proveedor**

```python
# En utils/validators.py
import re

def validar_email(email: str) -> str:
    """Valida formato de correo electrónico."""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, email):
        raise ValidationError(f"Email inválido: {email}")
    return email.strip().lower()
```

### 7.3. Agregar Operaciones al Inventario

**Ejemplo: Buscar por nombre**

```python
def buscar_por_nombre(inventario: Dict[int, Producto], termino: str) -> List[Tuple[int, Producto]]:
    """Busca productos cuyo nombre contenga el término."""
    termino = termino.lower()
    return [
        (id, producto) 
        for id, producto in inventario.items() 
        if termino in producto.nombre.lower()
    ]
```

---

## 8. Alternativas de Implementación

### 8.1. Herencia vs Composición

**Implementación Actual: Herencia**

```python
class Electronico(Producto):
    # "Electronico ES-UN Producto"
    ...
```

**Alternativa: Composición**

```python
class CalculadoraPrecio:
    def calcular(self, producto):
        raise NotImplementedError

class CalculadoraElectronicos(CalculadoraPrecio):
    def calcular(self, producto):
        # Lógica de electrónicos
        ...

class Producto:
    def __init__(self, nombre, precio_base, stock, calculadora):
        # "Producto TIENE-UNA calculadora"
        self.calculadora = calculadora
    
    def calcular_precio_final(self):
        return self.calculadora.calcular(self)
```

**Comparación:**

| Aspecto | Herencia | Composición |
|---------|----------|-------------|
| Relación conceptual | ES-UN | TIENE-UN |
| Complejidad | Menor | Mayor |
| Flexibilidad | Menos flexible | Más flexible |
| Reutilización | Vertical | Horizontal |
| Apropiado aquí | ✓ Sí | ⚠️ Sobrecarga |

**Conclusión:** La herencia es apropiada porque hay una relación jerárquica clara.

### 8.2. Propiedades vs Métodos Getter/Setter

**Implementación Actual: Propiedades**

```python
@property
def nombre(self):
    return self.__nombre

@nombre.setter
def nombre(self, valor):
    # Validación
    ...
```

**Alternativa: Métodos Java-style**

```python
def get_nombre(self):
    return self.__nombre

def set_nombre(self, valor):
    # Validación
    ...
```

**Comparación:**

| Aspecto | Propiedades | Getters/Setters |
|---------|-------------|-----------------|
| Sintaxis | `producto.nombre` | `producto.get_nombre()` |
| Pythónico | ✓ Sí | ❌ No |
| Compatibilidad | Retrocompatible | Cambio de interfaz |
| Recomendado | ✓ Sí | Otros lenguajes |

### 8.3. Excepciones Personalizadas vs Estándar

**Implementación Actual: Personalizadas**

```python
class ValidationError(Exception):
    ...

raise ValidationError("Precio inválido")
```

**Alternativa: Excepciones estándar**

```python
raise ValueError("Precio inválido")
raise KeyError("Producto no encontrado")
```

**Comparación:**

| Aspecto | Personalizadas | Estándar |
|---------|----------------|----------|
| Semántica del dominio | ✓ Clara | ❌ Genérica |
| Captura selectiva | ✓ Específica | ⚠️ Amplia |
| Documentación | ✓ Autodocumenta | Requiere docs |
| Sobrecarga | Clases extra | Sin sobrecarga |

**Conclusión:** Las personalizadas son superiores para dominios específicos.

### 8.4. Validación en Setter vs Constructor

**Implementación Actual: Setter**

```python
def __init__(self, nombre, precio_base, stock):
    self.nombre = nombre  # Llama al setter con validación
    ...
```

**Alternativa: Validación directa en constructor**

```python
def __init__(self, nombre, precio_base, stock):
    if not nombre:
        raise ValidationError(...)
    self.__nombre = nombre
```

**Comparación:**

| Aspecto | Via Setter | Directo |
|---------|------------|---------|
| Reutilización | ✓ DRY | ❌ Duplicado |
| Modificación posterior | ✓ Validada | ⚠️ Sin validar |
| Rendimiento | Ligeramente menor | Ligeramente mayor |

**Conclusión:** Via setter es superior para mantenibilidad.

---

## Conclusiones del Análisis

### Fortalezas del Sistema

1. **Arquitectura clara:** Separación en capas bien definidas
2. **POO correcta:** Herencia, encapsulamiento y polimorfismo bien aplicados
3. **Validación robusta:** Múltiples niveles de validación
4. **Testabilidad:** 83 pruebas unitarias con buena cobertura
5. **Extensibilidad:** Fácil agregar nuevas categorías
6. **Documentación:** Código y README bien documentados

### Áreas de Mejora (Fuera del Alcance)

1. **Persistencia:** Guardar inventario entre sesiones
2. **Logging completo:** Sistema de logs más robusto
3. **Interfaz gráfica:** GUI con tkinter o PyQt
4. **API REST:** Exponer funcionalidad vía HTTP
5. **Autenticación:** Control de acceso por usuarios
6. **Reportes:** Generar estadísticas del inventario

### Aplicabilidad Profesional

Los conceptos implementados son fundamentales para:

- Desarrollo de software empresarial
- Sistemas de gestión de inventarios reales
- Aplicaciones web con Python (Django, Flask)
- Microservicios y APIs
- Sistemas escalables y mantenibles

---

**Universidad Nacional del Centro del Perú**  
**Facultad de Ingeniería de Sistemas**  
**Curso:** Desarrollo de Aplicaciones Web (IS093A)  
**Semana 10 - 2026**
