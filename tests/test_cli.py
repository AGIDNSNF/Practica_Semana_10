"""
Pruebas unitarias para la funcionalidad del CLI.

Verifica el comportamiento del menú interactivo, registro de productos,
listado, búsqueda y manejo de errores mediante simulación de entrada.
"""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from models.producto import Electronico, Libro
from utils.exceptions import ValidationError, NotFoundError
import main


class TestAgregarProducto(unittest.TestCase):
    """Pruebas para la función agregar_producto."""
    
    @patch('builtins.input', side_effect=[
        'Electronico',  # Categoría
        'Laptop HP',    # Nombre
        '2500',         # Precio
        '10',           # Stock
        '12'            # Garantía
    ])
    def test_agregar_electronico_exitoso(self, mock_input):
        """Verifica el registro exitoso de un producto electrónico."""
        inventario = {}
        contador = 1
        
        nuevo_contador = main.agregar_producto(inventario, contador)
        
        self.assertEqual(nuevo_contador, 2)
        self.assertEqual(len(inventario), 1)
        self.assertIsInstance(inventario[1], Electronico)
        self.assertEqual(inventario[1].nombre, "Laptop HP")
    
    @patch('builtins.input', side_effect=[
        'Libro',                    # Categoría
        'Cien Años de Soledad',    # Nombre
        '80',                       # Precio
        '15',                       # Stock
        'García Márquez',          # Autor
        'n'                         # No es texto
    ])
    def test_agregar_libro_exitoso(self, mock_input):
        """Verifica el registro exitoso de un libro."""
        inventario = {}
        contador = 1
        
        nuevo_contador = main.agregar_producto(inventario, contador)
        
        self.assertEqual(nuevo_contador, 2)
        self.assertEqual(len(inventario), 1)
        self.assertIsInstance(inventario[1], Libro)
        self.assertEqual(inventario[1].autor, "García Márquez")
        self.assertFalse(inventario[1].es_texto)
    
    @patch('builtins.input', side_effect=[
        'Libro',
        'Matemática Básica',
        '120',
        '30',
        'Stewart',
        's'  # Es texto
    ])
    def test_agregar_libro_texto(self, mock_input):
        """Verifica el registro de un libro de texto."""
        inventario = {}
        contador = 1
        
        nuevo_contador = main.agregar_producto(inventario, contador)
        
        self.assertIsInstance(inventario[1], Libro)
        self.assertTrue(inventario[1].es_texto)
    
    @patch('builtins.input', side_effect=[
        'Hardware',  # Categoría inválida
    ])
    def test_categoria_invalida(self, mock_input):
        """Verifica que se rechace una categoría inválida."""
        inventario = {}
        contador = 1
        
        with self.assertRaises(ValidationError):
            main.agregar_producto(inventario, contador)
    
    @patch('builtins.input', side_effect=[
        'Electronico',
        'Mouse',
        '-50',  # Precio negativo
    ])
    def test_precio_negativo(self, mock_input):
        """Verifica que se rechace un precio negativo."""
        inventario = {}
        contador = 1
        
        with self.assertRaises(ValidationError):
            main.agregar_producto(inventario, contador)


class TestListarProductos(unittest.TestCase):
    """Pruebas para la función listar_productos."""
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_inventario_vacio(self, mock_stdout):
        """Verifica el mensaje cuando el inventario está vacío."""
        inventario = {}
        main.listar_productos(inventario)
        
        salida = mock_stdout.getvalue()
        self.assertIn("No hay productos", salida)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_inventario_con_productos(self, mock_stdout):
        """Verifica el listado con productos registrados."""
        inventario = {
            1: Electronico("Laptop", 2500.0, 10, 12),
            2: Libro("Novela", 80.0, 20, "Autor")
        }
        
        main.listar_productos(inventario)
        
        salida = mock_stdout.getvalue()
        self.assertIn("ID: 1", salida)
        self.assertIn("ID: 2", salida)
        self.assertIn("Laptop", salida)
        self.assertIn("Novela", salida)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_formato_listado(self, mock_stdout):
        """Verifica que el formato del listado sea correcto."""
        inventario = {
            1: Electronico("Mouse", 50.0, 25, 6)
        }
        
        main.listar_productos(inventario)
        
        salida = mock_stdout.getvalue()
        self.assertIn("INVENTARIO", salida)
        self.assertIn("Total de productos", salida)


class TestCalcularPrecioProducto(unittest.TestCase):
    """Pruebas para la función calcular_precio_producto."""
    
    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=StringIO)
    def test_calcular_precio_existente(self, mock_stdout, mock_input):
        """Verifica el cálculo de precio para un producto existente."""
        inventario = {
            1: Electronico("Laptop", 2500.0, 10, 12)
        }
        
        main.calcular_precio_producto(inventario)
        
        salida = mock_stdout.getvalue()
        self.assertIn("CÁLCULO DE PRECIO FINAL", salida)
        self.assertIn("Laptop", salida)
        self.assertIn("2950.00", salida)  # 2500 * 1.18
    
    @patch('builtins.input', return_value='999')
    def test_producto_inexistente(self, mock_input):
        """Verifica que se lance NotFoundError para ID inexistente."""
        inventario = {
            1: Electronico("Laptop", 2500.0, 10, 12)
        }
        
        with self.assertRaises(NotFoundError):
            main.calcular_precio_producto(inventario)
    
    @patch('builtins.input', return_value='abc')
    def test_id_no_numerico(self, mock_input):
        """Verifica que se rechace un ID no numérico."""
        inventario = {
            1: Electronico("Laptop", 2500.0, 10, 12)
        }
        
        with self.assertRaises(ValidationError):
            main.calcular_precio_producto(inventario)
    
    @patch('builtins.input', return_value='-5')
    def test_id_negativo(self, mock_input):
        """Verifica que se rechace un ID negativo."""
        inventario = {
            1: Electronico("Laptop", 2500.0, 10, 12)
        }
        
        with self.assertRaises(ValidationError):
            main.calcular_precio_producto(inventario)


class TestSolicitudDatosComunes(unittest.TestCase):
    """Pruebas para la función solicitar_datos_comunes."""
    
    @patch('builtins.input', side_effect=['Laptop', '2500', '10'])
    def test_datos_validos(self, mock_input):
        """Verifica la solicitud exitosa de datos comunes."""
        nombre, precio, stock = main.solicitar_datos_comunes()
        
        self.assertEqual(nombre, "Laptop")
        self.assertEqual(precio, 2500.0)
        self.assertEqual(stock, 10)
    
    @patch('builtins.input', side_effect=['', '100', '10'])
    def test_nombre_vacio(self, mock_input):
        """Verifica que se rechace un nombre vacío."""
        with self.assertRaises(ValidationError):
            main.solicitar_datos_comunes()
    
    @patch('builtins.input', side_effect=['Producto', 'abc', '10'])
    def test_precio_no_numerico(self, mock_input):
        """Verifica que se rechace un precio no numérico."""
        with self.assertRaises(ValidationError):
            main.solicitar_datos_comunes()


class TestMenuPrincipal(unittest.TestCase):
    """Pruebas de integración para el flujo del menú principal."""
    
    @patch('builtins.input', side_effect=['4'])  # Opción salir
    @patch('sys.stdout', new_callable=StringIO)
    def test_salida_normal(self, mock_stdout, mock_input):
        """Verifica la salida normal del programa."""
        main.main()
        
        salida = mock_stdout.getvalue()
        self.assertIn("Cerrando sistema", salida)
        self.assertIn("Gracias", salida)
    
    @patch('builtins.input', side_effect=['9', '4'])  # Opción inválida, luego salir
    @patch('sys.stdout', new_callable=StringIO)
    def test_opcion_invalida(self, mock_stdout, mock_input):
        """Verifica el manejo de una opción inválida."""
        main.main()
        
        salida = mock_stdout.getvalue()
        self.assertIn("Error de validación", salida)
    
    @patch('builtins.input', side_effect=['2', '4'])  # Listar, luego salir
    @patch('sys.stdout', new_callable=StringIO)
    def test_listar_inventario_vacio(self, mock_stdout, mock_input):
        """Verifica listar un inventario vacío desde el menú."""
        main.main()
        
        salida = mock_stdout.getvalue()
        self.assertIn("No hay productos", salida)


if __name__ == '__main__':
    unittest.main()
