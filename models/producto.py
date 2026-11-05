"""
Modelos de productos para el Sistema de Gestión de Productos.

Este módulo implementa la jerarquía de clases de productos utilizando
programación orientada a objetos: herencia, encapsulamiento, polimorfismo
y propiedades.
"""

import logging
from typing import Union
from utils.exceptions import ValidationError

# Configurar logging para mensajes del destructor
logging.basicConfig(level=logging.INFO, format='%(message)s')


class Producto:
    """
    Clase base abstracta que representa un producto genérico.
    
    Implementa encapsulamiento mediante atributos privados y propiedades.
    Define la interfaz común para todos los productos del sistema.
    
    Attributes:
        nombre (str): Nombre descriptivo del producto.
        precio_base (float): Precio base antes de impuestos y descuentos.
        stock (int): Cantidad disponible en inventario.
    """
    
    def __init__(
        self,
        nombre: str,
        precio_base: float,
        stock: int
    ):
        """
        Inicializa un producto con validaciones mediante setters.
        
        Args:
            nombre: Nombre del producto (no vacío).
            precio_base: Precio base mayor que cero.
            stock: Cantidad en inventario (entero no negativo).
        
        Raises:
            ValidationError: Si algún parámetro no cumple las validaciones.
        """
        # Utilizar setters para aplicar validaciones
        self.nombre = nombre
        self.precio_base = precio_base
        self.stock = stock
    
    @property
    def nombre(self) -> str:
        """Obtiene el nombre del producto."""
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor: str) -> None:
        """
        Establece el nombre del producto con validación.
        
        Args:
            valor: Nuevo nombre del producto.
        
        Raises:
            ValidationError: Si el nombre está vacío o no es una cadena.
        """
        if not isinstance(valor, str):
            raise ValidationError("El nombre debe ser una cadena de texto.")
        
        nombre_limpio = valor.strip()
        if not nombre_limpio:
            raise ValidationError("El nombre no puede estar vacío.")
        
        self.__nombre = nombre_limpio
    
    @property
    def precio_base(self) -> float:
        """Obtiene el precio base del producto."""
        return self.__precio_base
    
    @precio_base.setter
    def precio_base(self, valor: Union[int, float]) -> None:
        """
        Establece el precio base con validación.
        
        Args:
            valor: Nuevo precio base.
        
        Raises:
            ValidationError: Si el precio no es válido.
        """
        # Rechazar booleanos explícitamente
        if isinstance(valor, bool):
            raise ValidationError(
                "El precio no puede ser booleano. Debe ser un número."
            )
        
        # Validar tipo numérico
        if not isinstance(valor, (int, float)):
            raise ValidationError(
                "El precio base debe ser un número."
            )
        
        # Validar que sea finito
        if isinstance(valor, float):
            import math
            if math.isnan(valor):
                raise ValidationError("El precio no puede ser NaN.")
            if math.isinf(valor):
                raise ValidationError("El precio no puede ser infinito.")
        
        # Validar que sea positivo
        if valor <= 0:
            raise ValidationError(
                "El precio base debe ser mayor que cero."
            )
        
        self.__precio_base = float(valor)
    
    @property
    def stock(self) -> int:
        """Obtiene la cantidad en stock del producto."""
        return self.__stock
    
    @stock.setter
    def stock(self, valor: Union[int, float]) -> None:
        """
        Establece el stock con validación.
        
        Args:
            valor: Nueva cantidad en stock.
        
        Raises:
            ValidationError: Si el stock no es válido.
        """
        # Rechazar booleanos
        if isinstance(valor, bool):
            raise ValidationError(
                "El stock no puede ser booleano. Debe ser un número entero."
            )
        
        # Validar que sea numérico
        if not isinstance(valor, (int, float)):
            raise ValidationError("El stock debe ser un número entero.")
        
        # Rechazar valores decimales
        if isinstance(valor, float):
            if valor != int(valor):
                raise ValidationError(
                    "El stock debe ser un número entero, no decimal."
                )
            valor = int(valor)
        
        # Validar que no sea negativo
        if valor < 0:
            raise ValidationError(
                "El stock no puede ser negativo."
            )
        
        self.__stock = int(valor)
    
    def calcular_precio_final(self) -> float:
        """
        Calcula el precio final del producto.
        
        Este método debe ser implementado por las subclases concretas.
        
        Returns:
            El precio final calculado según las reglas de la subclase.
        
        Raises:
            NotImplementedError: Si se invoca desde la clase base.
        """
        raise NotImplementedError(
            "Las subclases deben implementar el método calcular_precio_final()."
        )
    
    def __str__(self) -> str:
        """
        Representación legible del producto.
        
        Returns:
            Cadena con el formato: [Tipo] Nombre | S/ Precio | Stock: Cantidad
        """
        tipo = self.__class__.__name__
        return (
            f"[{tipo}] {self.nombre} | "
            f"S/ {self.precio_base:.2f} | "
            f"Stock: {self.stock}"
        )
    
    def __del__(self):
        """
        Destructor del producto.
        
        Nota: Este método se incluye con fines demostrativos para la guía.
        La ejecución del destructor no es determinista en Python y no debe
        utilizarse para lógica crítica de limpieza de recursos.
        """
        logging.info(f"Destructor: Producto '{self.nombre}' eliminado de memoria.")


class Electronico(Producto):
    """
    Clase que representa un producto electrónico.
    
    Extiende Producto añadiendo garantía y aplicando reglas de precio
    específicas: IGV del 18% y descuento del 5% si stock > 50.
    
    Attributes:
        garantia_meses (int): Duración de la garantía en meses.
    """
    
    # Constantes para cálculo de precio
    IGV = 0.18
    DESCUENTO_STOCK_ALTO = 0.05
    UMBRAL_STOCK = 50
    
    def __init__(
        self,
        nombre: str,
        precio_base: float,
        stock: int,
        garantia_meses: int
    ):
        """
        Inicializa un producto electrónico.
        
        Args:
            nombre: Nombre del producto.
            precio_base: Precio base sin impuestos.
            stock: Cantidad disponible.
            garantia_meses: Duración de la garantía en meses (mínimo 1).
        
        Raises:
            ValidationError: Si los parámetros no son válidos.
        """
        # Inicializar atributos de la clase base
        super().__init__(nombre, precio_base, stock)
        
        # Inicializar atributo específico
        self.garantia_meses = garantia_meses
    
    @property
    def garantia_meses(self) -> int:
        """Obtiene la duración de la garantía en meses."""
        return self._garantia_meses
    
    @garantia_meses.setter
    def garantia_meses(self, valor: int) -> None:
        """
        Establece la garantía con validación.
        
        Args:
            valor: Duración de la garantía en meses.
        
        Raises:
            ValidationError: Si la garantía no es válida.
        """
        # Rechazar booleanos
        if isinstance(valor, bool):
            raise ValidationError(
                "La garantía no puede ser booleana. Debe ser un número entero."
            )
        
        # Validar tipo
        if not isinstance(valor, int):
            raise ValidationError(
                "La garantía debe ser un número entero de meses."
            )
        
        # Validar rango
        if valor < 1:
            raise ValidationError(
                "La garantía debe ser de al menos 1 mes."
            )
        
        self._garantia_meses = valor
    
    def calcular_precio_final(self) -> float:
        """
        Calcula el precio final del producto electrónico.
        
        Aplica las siguientes reglas:
        1. Agrega IGV del 18% sobre el precio base.
        2. Si stock > 50, aplica descuento del 5% sobre el precio con IGV.
        
        Returns:
            Precio final con impuestos y descuentos aplicados.
        
        Examples:
            >>> e = Electronico("Laptop", 100, 10, 12)
            >>> e.calcular_precio_final()
            118.0
            >>> e2 = Electronico("Mouse", 100, 51, 6)
            >>> e2.calcular_precio_final()
            112.1
        """
        # Aplicar IGV
        precio_con_igv = self.precio_base * (1 + self.IGV)
        
        # Aplicar descuento si el stock es alto
        if self.stock > self.UMBRAL_STOCK:
            precio_final = precio_con_igv * (1 - self.DESCUENTO_STOCK_ALTO)
        else:
            precio_final = precio_con_igv
        
        return round(precio_final, 2)
    
    def __str__(self) -> str:
        """
        Representación legible del producto electrónico.
        
        Returns:
            Cadena con información completa incluyendo garantía.
        """
        base = super().__str__()
        return f"{base} | Garantía: {self.garantia_meses} meses"


class Libro(Producto):
    """
    Clase que representa un libro.
    
    Extiende Producto añadiendo información del autor y tipo de libro.
    Aplica descuento del 10% para libros de texto.
    
    Attributes:
        autor (str): Nombre del autor del libro.
        es_texto (bool): Indica si es un libro de texto (True) o no (False).
    """
    
    # Constante para cálculo de precio
    DESCUENTO_LIBRO_TEXTO = 0.10
    
    def __init__(
        self,
        nombre: str,
        precio_base: float,
        stock: int,
        autor: str,
        es_texto: bool = False
    ):
        """
        Inicializa un libro.
        
        Args:
            nombre: Título del libro.
            precio_base: Precio base del libro.
            stock: Cantidad disponible.
            autor: Nombre del autor (no vacío).
            es_texto: Si es libro de texto (aplica descuento del 10%).
        
        Raises:
            ValidationError: Si los parámetros no son válidos.
        
        Note:
            El parámetro es_texto es una ampliación necesaria para implementar
            la regla de descuento especificada en la guía del docente.
        """
        # Inicializar atributos de la clase base
        super().__init__(nombre, precio_base, stock)
        
        # Inicializar atributos específicos
        self.autor = autor
        self.es_texto = es_texto
    
    @property
    def autor(self) -> str:
        """Obtiene el nombre del autor."""
        return self.__autor
    
    @autor.setter
    def autor(self, valor: str) -> None:
        """
        Establece el autor con validación.
        
        Args:
            valor: Nombre del autor.
        
        Raises:
            ValidationError: Si el autor no es válido.
        """
        if not isinstance(valor, str):
            raise ValidationError("El autor debe ser una cadena de texto.")
        
        autor_limpio = valor.strip()
        if not autor_limpio:
            raise ValidationError("El autor no puede estar vacío.")
        
        self.__autor = autor_limpio
    
    @property
    def es_texto(self) -> bool:
        """Indica si el libro es de texto."""
        return self.__es_texto
    
    @es_texto.setter
    def es_texto(self, valor: bool) -> None:
        """
        Establece si el libro es de texto.
        
        Args:
            valor: True si es libro de texto, False en caso contrario.
        
        Raises:
            ValidationError: Si el valor no es booleano.
        """
        if not isinstance(valor, bool):
            raise ValidationError(
                "El indicador 'es_texto' debe ser booleano (True/False)."
            )
        
        self.__es_texto = valor
    
    def calcular_precio_final(self) -> float:
        """
        Calcula el precio final del libro.
        
        Aplica descuento del 10% si es libro de texto.
        
        Returns:
            Precio final con descuento aplicado si corresponde.
        
        Examples:
            >>> libro = Libro("Novela", 100, 20, "García Márquez", False)
            >>> libro.calcular_precio_final()
            100.0
            >>> texto = Libro("Matemática", 100, 30, "Stewart", True)
            >>> texto.calcular_precio_final()
            90.0
        """
        if self.es_texto:
            precio_final = self.precio_base * (1 - self.DESCUENTO_LIBRO_TEXTO)
        else:
            precio_final = self.precio_base
        
        return round(precio_final, 2)
    
    def __str__(self) -> str:
        """
        Representación legible del libro.
        
        Returns:
            Cadena con información completa incluyendo autor y tipo.
        """
        base = super().__str__()
        tipo_libro = "Libro de texto" if self.es_texto else "Libro general"
        return f"{base} | Autor: {self.autor} | Tipo: {tipo_libro}"
