"""
Sistema de Gestión de Productos - Interfaz de Línea de Comandos (CLI)

Aplicación de consola para gestionar un inventario de productos electrónicos
y libros, demostrando programación orientada a objetos en Python.

Universidad Nacional del Centro del Perú
Facultad de Ingeniería de Sistemas
Curso: Desarrollo de Aplicaciones Web (IS093A)
Práctica: Semana 10
"""

import logging
from typing import Dict
from models.producto import Producto, Electronico, Libro
from utils.validators import validar_numero, validar_categoria
from utils.exceptions import ValidationError, NotFoundError

# Configurar logging para errores inesperados
logging.basicConfig(
    level=logging.ERROR,
    format='[%(levelname)s] %(message)s'
)


def menu() -> None:
    """
    Muestra el menú principal del sistema.
    """
    print("\n" + "=" * 40)
    print("=== GESTIÓN DE PRODUCTOS (CLI) ===")
    print("=" * 40)
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Calcular Precio Final")
    print("4. Salir")
    print("=" * 40)


def solicitar_datos_comunes() -> tuple:
    """
    Solicita y valida los datos comunes a todos los productos.
    
    Returns:
        Tupla con (nombre, precio_base, stock).
    
    Raises:
        ValidationError: Si algún dato no es válido.
        EOFError: Si se detecta fin de entrada.
        KeyboardInterrupt: Si el usuario interrumpe.
    """
    nombre = input("Nombre: ").strip()
    if not nombre:
        raise ValidationError("El nombre no puede estar vacío.")
    
    precio_str = input("Precio base (S/): ").strip()
    precio_base = validar_numero(precio_str, float, 0.01)
    
    stock_str = input("Stock: ").strip()
    stock = validar_numero(stock_str, int, 0)
    
    return nombre, precio_base, stock


def agregar_producto(inventario: Dict[int, Producto], contador_id: int) -> int:
    """
    Opción 1: Agregar un nuevo producto al inventario.
    
    Solicita al usuario la información necesaria, valida los datos,
    crea la instancia correspondiente y la agrega al inventario.
    
    Args:
        inventario: Diccionario de productos por ID.
        contador_id: Siguiente ID disponible.
    
    Returns:
        El nuevo valor del contador de IDs.
    
    Raises:
        ValidationError: Si los datos ingresados no son válidos.
    """
    print("\n--- AGREGAR PRODUCTO ---")
    
    # Solicitar categoría
    categoria_str = input("Categoría (Electronico/Libro): ").strip()
    categoria = validar_categoria(categoria_str)
    
    # Solicitar datos comunes
    nombre, precio_base, stock = solicitar_datos_comunes()
    
    # Crear instancia según la categoría
    if categoria == "Electronico":
        garantia_str = input("Garantía en meses: ").strip()
        garantia_meses = validar_numero(garantia_str, int, 1)
        
        producto = Electronico(
            nombre=nombre,
            precio_base=precio_base,
            stock=stock,
            garantia_meses=garantia_meses
        )
    
    elif categoria == "Libro":
        autor = input("Autor: ").strip()
        if not autor:
            raise ValidationError("El autor no puede estar vacío.")
        
        es_texto_str = input("¿Es libro de texto? (s/n): ").strip().lower()
        if es_texto_str not in ['s', 'n', 'si', 'no']:
            raise ValidationError(
                "Respuesta inválida. Ingrese 's' para sí o 'n' para no."
            )
        es_texto = es_texto_str in ['s', 'si']
        
        producto = Libro(
            nombre=nombre,
            precio_base=precio_base,
            stock=stock,
            autor=autor,
            es_texto=es_texto
        )
    
    else:
        # Este caso no debería ocurrir si validar_categoria funciona correctamente
        raise ValidationError(f"Categoría no soportada: {categoria}")
    
    # Agregar al inventario
    inventario[contador_id] = producto
    print(f"\n✓ Producto registrado correctamente.")
    print(f"  ID asignado: {contador_id}")
    
    return contador_id + 1


def listar_productos(inventario: Dict[int, Producto]) -> None:
    """
    Opción 2: Lista todos los productos del inventario.
    
    Muestra el ID y la descripción de cada producto registrado.
    
    Args:
        inventario: Diccionario de productos por ID.
    """
    print("\n--- INVENTARIO ---")
    
    if not inventario:
        print("No hay productos registrados.")
        return
    
    print(f"\nTotal de productos: {len(inventario)}\n")
    for producto_id, producto in inventario.items():
        print(f"ID: {producto_id} | {producto}")


def calcular_precio_producto(inventario: Dict[int, Producto]) -> None:
    """
    Opción 3: Calcula y muestra el precio final de un producto.
    
    Solicita el ID del producto, lo busca en el inventario y calcula
    su precio final aplicando las reglas de negocio correspondientes.
    
    Args:
        inventario: Diccionario de productos por ID.
    
    Raises:
        NotFoundError: Si el ID no existe en el inventario.
        ValidationError: Si el ID tiene formato inválido.
    """
    print("\n--- CALCULAR PRECIO FINAL ---")
    
    id_str = input("Ingrese el ID del producto: ").strip()
    producto_id = validar_numero(id_str, int, 1)
    
    # Buscar producto
    if producto_id not in inventario:
        raise NotFoundError(
            f"No existe un producto con ID {producto_id}."
        )
    
    producto = inventario[producto_id]
    precio_final = producto.calcular_precio_final()
    
    # Mostrar resultado
    print("\n" + "=" * 50)
    print("=== CÁLCULO DE PRECIO FINAL ===")
    print("=" * 50)
    print(f"ID: {producto_id}")
    print(f"Producto: {producto.nombre}")
    print(f"Categoría: {producto.__class__.__name__}")
    print(f"Precio base: S/ {producto.precio_base:.2f}")
    print(f"Precio final: S/ {precio_final:.2f}")
    print("=" * 50)


def main() -> None:
    """
    Función principal que orquesta el sistema.
    
    Mantiene el inventario en memoria, gestiona el menú interactivo
    y coordina las operaciones del sistema.
    """
    # Inicialización
    inventario: Dict[int, Producto] = {}
    contador_id: int = 1
    
    print("\n╔═══════════════════════════════════════════════════╗")
    print("║  SISTEMA DE GESTIÓN DE PRODUCTOS                 ║")
    print("║  Universidad Nacional del Centro del Perú        ║")
    print("║  Facultad de Ingeniería de Sistemas              ║")
    print("╚═══════════════════════════════════════════════════╝")
    
    # Ciclo principal
    while True:
        try:
            menu()
            opcion = input("Opción > ").strip()
            
            if opcion == "1":
                # Agregar producto
                contador_id = agregar_producto(inventario, contador_id)
            
            elif opcion == "2":
                # Listar productos
                listar_productos(inventario)
            
            elif opcion == "3":
                # Calcular precio final
                calcular_precio_producto(inventario)
            
            elif opcion == "4":
                # Salir
                print("\n" + "=" * 50)
                print("Cerrando sistema...")
                print("Gracias por utilizar el Sistema de Gestión de Productos.")
                print("=" * 50 + "\n")
                break
            
            else:
                # Opción inválida
                raise ValidationError(
                    f"Opción '{opcion}' no válida. Seleccione una opción entre 1 y 4."
                )
        
        except ValidationError as e:
            # Error de validación: mostrar mensaje al usuario
            print(f"\n✗ Error de validación: {e.message}")
        
        except NotFoundError as e:
            # Recurso no encontrado: informar al usuario
            print(f"\n✗ No encontrado: {e.message}")
        
        except (EOFError, KeyboardInterrupt):
            # Interrupción del usuario: salir limpiamente
            print("\n\nInterrupción detectada. Cerrando sistema...")
            break
        
        except Exception as e:
            # Error inesperado: registrar y mostrar mensaje genérico
            logging.exception("Error inesperado en el sistema")
            print(f"\n✗ Error inesperado: {type(e).__name__}")
            print("   El sistema continuará funcionando.")
        
        else:
            # Bloque else: se ejecuta si no hubo excepciones
            # En este diseño, los mensajes de éxito ya se muestran
            # dentro de cada función, por lo que este bloque permanece
            # disponible para extensiones futuras
            pass
        
        finally:
            # Bloque finally: se ejecuta siempre
            # Útil para limpieza de recursos temporales
            # En este caso, se mantiene para demostrar la estructura completa
            # requerida por la guía (try/except/else/finally)
            pass


if __name__ == "__main__":
    main()
