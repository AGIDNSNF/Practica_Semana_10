"""
Pruebas unitarias para las clases de productos.

Verifica el correcto funcionamiento de Producto, Electronico y Libro,
incluyendo herencia, encapsulamiento, validaciones y cálculos de precio.
"""

import unittest
import math
from models.producto import Producto, Electronico, Libro
from utils.exceptions import ValidationError


class TestProducto(unittest.TestCase):
    """Pruebas para la clase base Producto."""
    
    def test_creacion_valida(self):
        """Verifica la creación exitosa de un producto con datos válidos."""
        # Esta prueba usa Electronico porque Producto es abstracta
        producto = Electronico("Laptop", 2500.0, 10, 12)
        self.assertEqual(producto.nombre, "Laptop")
        self.assertEqual(producto.precio_base, 2500.0)
        self.assertEqual(producto.stock, 10)
    
    def test_nombre_vacio(self):
        """Verifica que se rechace un nombre vacío."""
        with self.assertRaises(ValidationError) as context:
            Electronico("", 100.0, 5, 6)
        self.assertIn("vacío", str(context.exception))
    
    def test_nombre_solo_espacios(self):
        """Verifica que se rechace un nombre con solo espacios."""
        with self.assertRaises(ValidationError):
            Electronico("   ", 100.0, 5, 6)
    
    def test_precio_negativo(self):
        """Verifica que se rechace un precio negativo."""
        with self.assertRaises(ValidationError) as context:
            Electronico("Mouse", -50.0, 10, 6)
        self.assertIn("mayor que cero", str(context.exception))
    
    def test_precio_cero(self):
        """Verifica que se rechace un precio igual a cero."""
        with self.assertRaises(ValidationError):
            Electronico("Teclado", 0.0, 15, 6)
    
    def test_precio_no_numerico_booleano(self):
        """Verifica que se rechace un precio booleano."""
        with self.assertRaises(ValidationError):
            Electronico("Monitor", True, 8, 12)
    
    def test_precio_nan(self):
        """Verifica que se rechace NaN como precio."""
        with self.assertRaises(ValidationError):
            Electronico("Cable", float('nan'), 20, 3)
    
    def test_precio_infinito(self):
        """Verifica que se rechace infinito como precio."""
        with self.assertRaises(ValidationError):
            Electronico("Router", float('inf'), 5, 12)
    
    def test_stock_negativo(self):
        """Verifica que se rechace un stock negativo."""
        with self.assertRaises(ValidationError):
            Electronico("Auriculares", 150.0, -5, 6)
    
    def test_stock_decimal(self):
        """Verifica que se rechace un stock decimal."""
        with self.assertRaises(ValidationError):
            Electronico("Webcam", 200.0, 5.5, 6)
    
    def test_stock_cero_valido(self):
        """Verifica que se acepte stock igual a cero."""
        producto = Electronico("Agotado", 100.0, 0, 6)
        self.assertEqual(producto.stock, 0)
    
    def test_setter_nombre(self):
        """Verifica que el setter de nombre funcione correctamente."""
        producto = Electronico("Original", 100.0, 10, 6)
        producto.nombre = "Modificado"
        self.assertEqual(producto.nombre, "Modificado")
    
    def test_setter_precio_base(self):
        """Verifica que el setter de precio_base funcione correctamente."""
        producto = Electronico("Producto", 100.0, 10, 6)
        producto.precio_base = 150.0
        self.assertEqual(producto.precio_base, 150.0)
    
    def test_setter_stock(self):
        """Verifica que el setter de stock funcione correctamente."""
        producto = Electronico("Producto", 100.0, 10, 6)
        producto.stock = 20
        self.assertEqual(producto.stock, 20)
    
    def test_str_representation(self):
        """Verifica la representación en cadena del producto."""
        producto = Electronico("Laptop HP", 2500.0, 10, 12)
        representacion = str(producto)
        self.assertIn("Electronico", representacion)
        self.assertIn("Laptop HP", representacion)
        self.assertIn("2500.00", representacion)
        self.assertIn("10", representacion)
    
    def test_metodo_abstracto(self):
        """Verifica que la clase base lance NotImplementedError."""
        # Crear una instancia directa de Producto (bypassing validación)
        class ProductoConcreto(Producto):
            pass
        
        with self.assertRaises(NotImplementedError):
            producto = ProductoConcreto("Test", 100.0, 10)
            producto.calcular_precio_final()


class TestElectronico(unittest.TestCase):
    """Pruebas para la clase Electronico."""
    
    def test_herencia(self):
        """Verifica que Electronico herede de Producto."""
        producto = Electronico("Laptop", 2500.0, 10, 12)
        self.assertIsInstance(producto, Producto)
        self.assertIsInstance(producto, Electronico)
    
    def test_inicializacion_super(self):
        """Verifica que se inicialicen correctamente los atributos heredados."""
        producto = Electronico("Mouse", 50.0, 25, 6)
        self.assertEqual(producto.nombre, "Mouse")
        self.assertEqual(producto.precio_base, 50.0)
        self.assertEqual(producto.stock, 25)
        self.assertEqual(producto.garantia_meses, 6)
    
    def test_garantia_valida(self):
        """Verifica la aceptación de garantías válidas."""
        producto = Electronico("Tablet", 800.0, 15, 24)
        self.assertEqual(producto.garantia_meses, 24)
    
    def test_garantia_minima(self):
        """Verifica que se acepte garantía de 1 mes."""
        producto = Electronico("Cable", 20.0, 100, 1)
        self.assertEqual(producto.garantia_meses, 1)
    
    def test_garantia_invalida_cero(self):
        """Verifica que se rechace garantía de 0 meses."""
        with self.assertRaises(ValidationError):
            Electronico("Producto", 100.0, 10, 0)
    
    def test_garantia_invalida_negativa(self):
        """Verifica que se rechace garantía negativa."""
        with self.assertRaises(ValidationError):
            Electronico("Producto", 100.0, 10, -3)
    
    def test_calculo_precio_base(self):
        """Verifica el cálculo de precio con IGV sin descuento."""
        producto = Electronico("Mouse", 100.0, 10, 6)
        precio_final = producto.calcular_precio_final()
        self.assertEqual(precio_final, 118.0)
    
    def test_calculo_stock_bajo(self):
        """Verifica que no se aplique descuento con stock <= 50."""
        producto = Electronico("Teclado", 100.0, 50, 6)
        precio_final = producto.calcular_precio_final()
        self.assertEqual(precio_final, 118.0)
    
    def test_calculo_stock_justo_umbral(self):
        """Verifica que con stock exactamente 50 no haya descuento."""
        producto = Electronico("Monitor", 1000.0, 50, 12)
        precio_final = producto.calcular_precio_final()
        esperado = 1000.0 * 1.18
        self.assertEqual(precio_final, round(esperado, 2))
    
    def test_calculo_stock_alto(self):
        """Verifica que se aplique descuento con stock > 50."""
        producto = Electronico("Cable HDMI", 100.0, 51, 3)
        precio_final = producto.calcular_precio_final()
        # Precio con IGV: 118.0
        # Con descuento 5%: 118.0 * 0.95 = 112.1
        self.assertEqual(precio_final, 112.1)
    
    def test_descuento_aplicado_correctamente(self):
        """Verifica la aplicación correcta del descuento por stock alto."""
        producto = Electronico("Memoria USB", 50.0, 100, 6)
        precio_final = producto.calcular_precio_final()
        # 50 * 1.18 = 59.0
        # 59.0 * 0.95 = 56.05
        self.assertAlmostEqual(precio_final, 56.05, places=2)
    
    def test_str_incluye_garantia(self):
        """Verifica que la representación incluya la garantía."""
        producto = Electronico("Laptop", 2500.0, 10, 12)
        representacion = str(producto)
        self.assertIn("Garantía", representacion)
        self.assertIn("12", representacion)


class TestLibro(unittest.TestCase):
    """Pruebas para la clase Libro."""
    
    def test_herencia(self):
        """Verifica que Libro herede de Producto."""
        libro = Libro("Cien Años", 80.0, 15, "García Márquez")
        self.assertIsInstance(libro, Producto)
        self.assertIsInstance(libro, Libro)
    
    def test_autor_valido(self):
        """Verifica la aceptación de un autor válido."""
        libro = Libro("Don Quijote", 120.0, 8, "Cervantes")
        self.assertEqual(libro.autor, "Cervantes")
    
    def test_autor_vacio(self):
        """Verifica que se rechace un autor vacío."""
        with self.assertRaises(ValidationError):
            Libro("Libro Sin Autor", 50.0, 10, "")
    
    def test_autor_solo_espacios(self):
        """Verifica que se rechace un autor con solo espacios."""
        with self.assertRaises(ValidationError):
            Libro("Libro", 50.0, 10, "   ")
    
    def test_atributo_privado_autor(self):
        """Verifica que el autor use encapsulamiento privado."""
        libro = Libro("Python Básico", 90.0, 20, "Lutz")
        # Verificar que no existe __autor directamente
        self.assertFalse(hasattr(libro, 'autor'))
        # Pero sí existe _Libro__autor (name mangling)
        self.assertTrue(hasattr(libro, '_Libro__autor'))
    
    def test_precio_libro_normal(self):
        """Verifica el precio de un libro que no es de texto."""
        libro = Libro("Novela", 100.0, 10, "Autor", False)
        precio_final = libro.calcular_precio_final()
        self.assertEqual(precio_final, 100.0)
    
    def test_descuento_libro_texto(self):
        """Verifica el descuento del 10% para libros de texto."""
        libro = Libro("Matemática Básica", 100.0, 25, "Stewart", True)
        precio_final = libro.calcular_precio_final()
        self.assertEqual(precio_final, 90.0)
    
    def test_es_texto_default_false(self):
        """Verifica que es_texto sea False por defecto."""
        libro = Libro("Libro", 50.0, 10, "Autor")
        self.assertFalse(libro.es_texto)
    
    def test_validacion_es_texto_booleano(self):
        """Verifica que es_texto solo acepte booleanos."""
        libro = Libro("Libro", 50.0, 10, "Autor", False)
        with self.assertRaises(ValidationError):
            libro.es_texto = "si"
    
    def test_str_incluye_autor(self):
        """Verifica que la representación incluya el autor."""
        libro = Libro("1984", 75.0, 20, "Orwell")
        representacion = str(libro)
        self.assertIn("Autor", representacion)
        self.assertIn("Orwell", representacion)
    
    def test_str_incluye_tipo(self):
        """Verifica que la representación incluya el tipo de libro."""
        libro_texto = Libro("Cálculo", 120.0, 15, "Thomas", True)
        representacion = str(libro_texto)
        self.assertIn("texto", representacion.lower())


class TestPolimorfismo(unittest.TestCase):
    """Pruebas para verificar el comportamiento polimórfico."""
    
    def test_polimorfismo_calcular_precio(self):
        """Verifica que cada clase use su propia implementación."""
        productos = [
            Electronico("Laptop", 100.0, 10, 12),
            Libro("Novela", 100.0, 10, "Autor", False),
            Libro("Texto", 100.0, 10, "Autor", True)
        ]
        
        precios = [p.calcular_precio_final() for p in productos]
        
        # Cada uno debe tener un precio diferente
        self.assertEqual(precios[0], 118.0)  # Electronico con IGV
        self.assertEqual(precios[1], 100.0)  # Libro normal
        self.assertEqual(precios[2], 90.0)   # Libro de texto
    
    def test_mro_electronico(self):
        """Verifica el Method Resolution Order de Electronico."""
        mro = Electronico.mro()
        self.assertEqual(mro[0], Electronico)
        self.assertEqual(mro[1], Producto)
        self.assertEqual(mro[2], object)
    
    def test_mro_libro(self):
        """Verifica el Method Resolution Order de Libro."""
        mro = Libro.mro()
        self.assertEqual(mro[0], Libro)
        self.assertEqual(mro[1], Producto)
        self.assertEqual(mro[2], object)


if __name__ == '__main__':
    unittest.main()
