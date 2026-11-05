# Instrucciones para la Entrega - Semana 10

## Información del Proyecto

**Curso:** Desarrollo de Aplicaciones Web (IS093A)  
**Práctica:** Semana 10 - Programación Orientada a Objetos en Python  
**Universidad:** Universidad Nacional del Centro del Perú  
**Facultad:** Ingeniería de Sistemas

---

## Pasos Previos a la Entrega

### 1. Completar Información Personal

Editar el archivo `README.md` y completar:

```markdown
### Integrantes
- **Integrante 1:** [Nombre Completo] - [Código]
- **Integrante 2:** [Nombre Completo] - [Código]

### Docente
- **Profesor:** [Nombre del Docente]
```

### 2. Verificar Requisitos del Sistema

Asegurarse de tener instalado Python 3.11 o superior:

```bash
python --version
```

Si no está instalado, descargar desde: https://www.python.org/downloads/

**IMPORTANTE para Windows:** Durante la instalación, marcar la opción "Add Python to PATH".

### 3. Probar el Sistema

#### a) Ejecutar el programa principal

```bash
cd C:\Users\GABRIEL\Desktop\AGUILAR\S10
python main.py
```

Verificar que:
- El menú se muestra correctamente
- Se pueden agregar productos
- Se pueden listar productos
- Se pueden calcular precios
- Las excepciones se capturan adecuadamente

#### b) Ejecutar las pruebas unitarias

```bash
python -m unittest discover -s tests -v
```

**Resultado esperado:**
```
Ran 83 tests in X.XXXs

OK
```

Si alguna prueba falla:
1. Revisar el mensaje de error
2. Corregir el código correspondiente
3. Volver a ejecutar las pruebas

### 4. Capturar las Tres Evidencias Obligatorias

Seguir las instrucciones detalladas en `evidencias/README.md`.

#### Evidencia 1: Caso Exitoso
- Registrar un producto
- Calcular su precio final
- Capturar pantalla o copiar texto
- Guardar como `evidencia_1_exito.png` o `evidencia_1_exito.txt`

#### Evidencia 2: ValidationError
- Intentar ingresar datos inválidos (precio negativo, stock inválido, etc.)
- Observar mensaje de error
- Capturar pantalla o copiar texto
- Guardar como `evidencia_2_validation_error.png` o `.txt`

#### Evidencia 3: NotFoundError
- Intentar buscar un producto con ID inexistente
- Observar mensaje de error
- Capturar pantalla o copiar texto
- Guardar como `evidencia_3_not_found_error.png` o `.txt`

**Nota:** En la carpeta `evidencias/` hay tres archivos de ejemplo (`.txt`) que muestran cómo debería verse cada caso. Pueden usarse como referencia.

### 5. Verificar Documentación

Revisar que el `README.md` contenga:
- [x] Información general completa
- [x] Objetivos claramente definidos
- [x] Diagrama UML de clases
- [x] Explicación de POO (herencia, encapsulamiento, polimorfismo)
- [x] Explicación del MRO
- [x] Reglas de negocio documentadas
- [x] Manual de usuario
- [x] Instrucciones de instalación
- [x] Documentación de excepciones
- [x] Información sobre pruebas
- [x] Referencias a evidencias
- [x] Conclusiones

---

## Contenido Mínimo de Entrega

### Archivos Obligatorios

```
gestion-productos/
├── main.py                                 ✓ Punto de entrada
├── README.md                               ✓ Documentación principal
├── requirements.txt                        ✓ Dependencias
├── .gitignore                              ✓ Control de versiones
│
├── models/
│   ├── __init__.py                        ✓ Exportaciones
│   └── producto.py                        ✓ Clases POO
│
├── utils/
│   ├── __init__.py                        ✓ Exportaciones
│   ├── exceptions.py                      ✓ Excepciones
│   └── validators.py                      ✓ Validadores
│
├── tests/
│   ├── __init__.py                        ✓ Inicialización
│   ├── test_producto.py                   ✓ Pruebas de clases
│   ├── test_validators.py                 ✓ Pruebas de validadores
│   └── test_cli.py                        ✓ Pruebas de CLI
│
└── evidencias/
    ├── README.md                          ✓ Guía de evidencias
    ├── evidencia_1_exito.*                ⚠ CAPTURAR
    ├── evidencia_2_validation_error.*     ⚠ CAPTURAR
    └── evidencia_3_not_found_error.*      ⚠ CAPTURAR
```

⚠ **IMPORTANTE:** Los tres archivos de evidencias con capturas reales son OBLIGATORIOS.

---

## Modalidades de Entrega

### Opción A: Repositorio GitHub (Recomendado)

1. Crear un repositorio en GitHub
2. Inicializar Git en el proyecto:

```bash
cd C:\Users\GABRIEL\Desktop\AGUILAR\S10
git init
git add .
git commit -m "Entrega Semana 10: Sistema de Gestión de Productos"
git branch -M main
git remote add origin [URL_DE_TU_REPOSITORIO]
git push -u origin main
```

3. Compartir el enlace del repositorio con el docente
4. Asegurarse de que el repositorio sea **público** o dar acceso al docente

### Opción B: Archivo ZIP

1. Comprimir toda la carpeta del proyecto
2. Nombrar el archivo: `S10_Apellidos_Codigo.zip`
3. Verificar que el archivo incluya todas las carpetas y archivos
4. Subir según las indicaciones del docente (aula virtual, email, etc.)

**Verificación antes de comprimir:**
```bash
# En PowerShell
Get-ChildItem -Recurse | Measure-Object
# Debería mostrar aproximadamente 15-20 archivos
```

---

## Criterios de Evaluación

### Rúbrica Oficial (Total: 100%)

| Criterio | Peso | Verificación |
|----------|------|--------------|
| **Diseño POO:** Clases, atributos, métodos, super() | 25% | ✓ Implementado |
| **Encapsulamiento y Polimorfismo** | 20% | ✓ Implementado |
| **Manejo de excepciones robusto** | 20% | ✓ Implementado |
| **Estructuras de control y funciones** | 15% | ✓ Implementado |
| **Modularización, PEP 8, documentación** | 20% | ✓ Implementado |

### Checklist de Autoevaluación

Antes de entregar, verificar:

- [ ] El programa se ejecuta sin errores
- [ ] Las 83 pruebas unitarias pasan exitosamente
- [ ] Las tres evidencias están capturadas
- [ ] El README tiene información completa de los integrantes
- [ ] El código sigue PEP 8 (indentación, nombres, etc.)
- [ ] Todos los métodos y clases tienen docstrings
- [ ] Se utiliza herencia correctamente
- [ ] Se utiliza `super()` en las subclases
- [ ] Los atributos están encapsulados (privados/protegidos)
- [ ] Se implementa polimorfismo en `calcular_precio_final()`
- [ ] Las excepciones personalizadas funcionan
- [ ] Se usa `try/except/else/finally` correctamente
- [ ] El MRO está explicado en el README
- [ ] El diagrama UML está incluido
- [ ] Las reglas de negocio funcionan correctamente

---

## Preparación para Evaluación Presencial

### Conceptos que Debes Poder Explicar

1. **Herencia:**
   - ¿Por qué Electronico y Libro heredan de Producto?
   - ¿Qué ventajas ofrece la herencia en este diseño?

2. **Encapsulamiento:**
   - ¿Por qué los atributos son privados?
   - ¿Cómo funcionan las propiedades con `@property`?

3. **Polimorfismo:**
   - ¿Cómo permite el sistema tratar diferentes productos de forma uniforme?
   - ¿Qué método demuestra polimorfismo?

4. **MRO:**
   - ¿Qué es el Method Resolution Order?
   - ¿Cómo funciona `super()` en relación al MRO?

5. **Excepciones:**
   - ¿Cuándo se lanza ValidationError?
   - ¿Cuándo se lanza NotFoundError?
   - ¿Qué hace cada bloque: try, except, else, finally?

6. **Validaciones:**
   - ¿Qué validaciones se aplican al precio?
   - ¿Qué validaciones se aplican al stock?
   - ¿Cómo se normaliza la categoría?

7. **Reglas de Negocio:**
   - ¿Cómo se calcula el precio de un electrónico?
   - ¿Cuándo se aplica el descuento por stock alto?
   - ¿Cómo se calcula el precio de un libro de texto?

### Demostraciones que Debes Poder Realizar

1. Ejecutar el programa y agregar productos
2. Listar el inventario
3. Calcular precios finales
4. Provocar y mostrar ValidationError
5. Provocar y mostrar NotFoundError
6. Ejecutar las pruebas unitarias
7. Explicar el código de una clase específica
8. Modificar una regla de negocio (ej: cambiar el IGV)

---

## Preguntas Frecuentes

### ¿Python no está instalado en mi sistema?

Descargar e instalar desde: https://www.python.org/downloads/

Durante la instalación, marcar: ☑ **"Add Python to PATH"**

### ¿Las pruebas no se ejecutan?

Verificar que estás en el directorio raíz del proyecto:

```bash
cd C:\Users\GABRIEL\Desktop\AGUILAR\S10
python -m unittest discover -s tests -v
```

### ¿Cómo capturo pantalla en Windows?

- **Pantalla completa:** Tecla `Print Screen` o `PrtScn`
- **Región seleccionada:** `Win + Shift + S`
- **Ventana activa:** `Alt + Print Screen`

### ¿Puedo modificar el código?

Sí, pero asegúrate de:
1. Mantener la estructura obligatoria
2. No romper las pruebas unitarias
3. Documentar cualquier cambio significativo
4. Actualizar el README si es necesario

### ¿Debo incluir un entorno virtual (venv)?

No es necesario, ya que el proyecto no tiene dependencias externas.

Si lo creas, asegúrate de incluir `venv/` en `.gitignore` (ya está incluido).

### ¿Qué hago si una prueba falla?

1. Leer el mensaje de error cuidadosamente
2. Identificar qué prueba falló y por qué
3. Revisar el código relacionado
4. Corregir el problema
5. Volver a ejecutar las pruebas

---

## Recursos Adicionales

### Documentación de Python
- Guía oficial: https://docs.python.org/es/3/
- Tutorial POO: https://docs.python.org/es/3/tutorial/classes.html

### PEP 8 - Guía de Estilo
- https://peps.python.org/pep-0008/

### Unittest
- https://docs.python.org/3/library/unittest.html

### Git y GitHub
- Guía básica de Git: https://git-scm.com/book/es/v2
- GitHub Docs: https://docs.github.com/es

---

## Contacto y Soporte

Para dudas técnicas sobre el proyecto:
1. Revisar este documento completo
2. Consultar el `README.md`
3. Revisar los comentarios en el código
4. Ejecutar las pruebas para identificar problemas
5. Consultar con el docente en horario de clase

---

## Lista de Verificación Final

Antes de entregar, confirmar:

- [ ] Información personal completada en README.md
- [ ] Programa ejecutable sin errores
- [ ] 83 pruebas unitarias aprobadas
- [ ] Tres evidencias capturadas y guardadas
- [ ] Código siguiendo PEP 8
- [ ] Documentación completa
- [ ] Archivos organizados según estructura obligatoria
- [ ] .gitignore incluido (si se usa Git)
- [ ] Repositorio público o archivo ZIP listo
- [ ] Preparado para explicar conceptos POO
- [ ] Preparado para demostrar funcionamiento

---

**¡Éxito en la entrega de la práctica!**

**Universidad Nacional del Centro del Perú**  
**Facultad de Ingeniería de Sistemas**  
**Curso: Desarrollo de Aplicaciones Web (IS093A)**  
**Semana 10 - 2026**
