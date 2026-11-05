"""
Pruebas unitarias para las funciones de validación.

Verifica el correcto funcionamiento de validar_numero y validar_categoria
con diferentes tipos de entrada, rangos y casos límite.
"""

import unittest
import math
from utils.validators import validar_numero, validar_categoria
from utils.exceptions import ValidationError


class TestValidarNumero(unittest.TestCase):
    """Pruebas para la función validar_numero."""
    
    def test_entero_valido(self):
        """Verifica la conversión correcta de cadena a entero."""
        resultado = validar_numero("15", int, 0)
        self.assertEqual(resultado, 15)
        self.assertIsInstance(resultado, int)
    
    def test_float_valido(self):
        """Verifica la conversión correcta de cadena a float."""
        resultado = validar_numero("99.50", float, 0)
        self.assertEqual(resultado, 99.5)
        self.assertIsInstance(resultado, float)
    
    def test_entero_negativo_rechazado(self):
        """Verifica que se rechace un número negativo cuando min_val es 0."""
        with self.assertRaises(ValidationError) as context:
            validar_numero("-5", int, 0)
        self.assertIn("mayor o igual", str(context.exception))
    
    def test_cadena_no_numerica(self):
        """Verifica que se rechace una cadena no numérica."""
        with self.assertRaises(ValidationError):
            validar_numero("abc", float, 0)
    
    def test_fuera_de_rango_inferior(self):
        """Verifica que se rechace un número menor al mínimo."""
        with self.assertRaises(ValidationError):
            validar_numero("5", int, 10)
    
    def test_fuera_de_rango_superior(self):
        """Verifica que se rechace un número mayor al máximo."""
        with self.assertRaises(ValidationError):
            validar_numero("100", int, 0, 50)
    
    def test_dentro_de_rango(self):
        """Verifica que se acepte un número dentro del rango."""
        resultado = validar_numero("25", int, 10, 50)
        self.assertEqual(resultado, 25)
    
    def test_valor_nan(self):
        """Verifica que se rechace NaN."""
        with self.assertRaises(ValidationError) as context:
            validar_numero("nan", float, 0)
        # La cadena "nan" podría no convertirse a NaN en todos los contextos
        # pero debería fallar como no numérica o como NaN
        self.assertTrue(True)  # Si llegamos aquí, se rechazó correctamente
    
    def test_valor_infinito_positivo(self):
        """Verifica que se rechace infinito positivo."""
        with self.assertRaises(ValidationError):
            validar_numero("inf", float, 0)
    
    def test_valor_infinito_negativo(self):
        """Verifica que se rechace infinito negativo."""
        with self.assertRaises(ValidationError):
            validar_numero("-inf", float, 0)
    
    def test_entero_en_limite_inferior(self):
        """Verifica que se acepte un valor en el límite inferior."""
        resultado = validar_numero("10", int, 10)
        self.assertEqual(resultado, 10)
    
    def test_entero_en_limite_superior(self):
        """Verifica que se acepte un valor en el límite superior."""
        resultado = validar_numero("50", int, 0, 50)
        self.assertEqual(resultado, 50)
    
    def test_float_con_muchos_decimales(self):
        """Verifica el manejo de floats con muchos decimales."""
        resultado = validar_numero("3.14159265359", float, 0)
        self.assertAlmostEqual(resultado, 3.14159265359, places=10)
    
    def test_cadena_vacia(self):
        """Verifica que se rechace una cadena vacía."""
        with self.assertRaises(ValidationError):
            validar_numero("", int, 0)
    
    def test_espacios_en_cadena(self):
        """Verifica el manejo de espacios en la cadena."""
        # Python strip() maneja esto, pero validar_numero recibe el valor
        # ya procesado por el caller normalmente
        resultado = validar_numero("  42  ", int, 0)
        self.assertEqual(resultado, 42)


class TestValidarCategoria(unittest.TestCase):
    """Pruebas para la función validar_categoria."""
    
    def test_electronico_minusculas(self):
        """Verifica normalización de 'electronico' a 'Electronico'."""
        resultado = validar_categoria("electronico")
        self.assertEqual(resultado, "Electronico")
    
    def test_electronico_mayusculas(self):
        """Verifica normalización de 'ELECTRONICO' a 'Electronico'."""
        resultado = validar_categoria("ELECTRONICO")
        self.assertEqual(resultado, "Electronico")
    
    def test_electronico_mixto(self):
        """Verifica normalización de 'ElEcTrOnIcO' a 'Electronico'."""
        resultado = validar_categoria("ElEcTrOnIcO")
        self.assertEqual(resultado, "Electronico")
    
    def test_electronico_con_tilde(self):
        """Verifica normalización de 'Electrónico' a 'Electronico'."""
        resultado = validar_categoria("Electrónico")
        self.assertEqual(resultado, "Electronico")
    
    def test_libro_minusculas(self):
        """Verifica normalización de 'libro' a 'Libro'."""
        resultado = validar_categoria("libro")
        self.assertEqual(resultado, "Libro")
    
    def test_libro_mayusculas(self):
        """Verifica normalización de 'LIBRO' a 'Libro'."""
        resultado = validar_categoria("LIBRO")
        self.assertEqual(resultado, "Libro")
    
    def test_libro_forma_canonica(self):
        """Verifica que la forma canónica se mantenga."""
        resultado = validar_categoria("Libro")
        self.assertEqual(resultado, "Libro")
    
    def test_categoria_invalida(self):
        """Verifica que se rechace una categoría no reconocida."""
        with self.assertRaises(ValidationError) as context:
            validar_categoria("Hardware")
        self.assertIn("inválida", str(context.exception))
    
    def test_categoria_vacia(self):
        """Verifica que se rechace una categoría vacía."""
        with self.assertRaises(ValidationError):
            validar_categoria("")
    
    def test_categoria_con_espacios(self):
        """Verifica el manejo de espacios alrededor de la categoría."""
        resultado = validar_categoria("  electronico  ")
        self.assertEqual(resultado, "Electronico")
    
    def test_categoria_con_acento_mayuscula(self):
        """Verifica normalización de 'ELECTRÓNICO' a 'Electronico'."""
        resultado = validar_categoria("ELECTRÓNICO")
        self.assertEqual(resultado, "Electronico")
    
    def test_multiples_variaciones(self):
        """Verifica que múltiples variaciones normalicen correctamente."""
        variaciones = [
            "electronico",
            "Electronico",
            "ELECTRONICO",
            "electrónico",
            "Electrónico",
            "ELECTRÓNICO"
        ]
        for variacion in variaciones:
            resultado = validar_categoria(variacion)
            self.assertEqual(resultado, "Electronico",
                           f"Falló con variación: {variacion}")


if __name__ == '__main__':
    unittest.main()
