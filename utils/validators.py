"""
Funciones de validación y normalización de datos de entrada.

Este módulo proporciona utilidades para validar y normalizar datos
recibidos del usuario antes de su procesamiento.
"""

import math
import unicodedata
from typing import Union
from .exceptions import ValidationError


def validar_numero(
    valor: str,
    tipo: type = float,
    min_val: float = 0,
    max_val: Union[float, None] = None
) -> Union[int, float]:
    """
    Valida y convierte una cadena a un número del tipo especificado.
    
    Args:
        valor: Cadena que representa el número a validar.
        tipo: Tipo de dato numérico esperado (int o float).
        min_val: Valor mínimo permitido (inclusive).
        max_val: Valor máximo permitido (inclusive). None indica sin límite superior.
    
    Returns:
        El número convertido al tipo especificado.
    
    Raises:
        ValidationError: Si el valor no es numérico, está fuera de rango,
                        es NaN, infinito o es booleano disfrazado de número.
    
    Examples:
        >>> validar_numero("15", int, 0)
        15
        >>> validar_numero("99.50", float, 0)
        99.5
        >>> validar_numero("-5", int, 0)
        ValidationError: El valor debe ser mayor o igual a 0
    """
    # Rechazar valores booleanos
    if isinstance(valor, bool):
        raise ValidationError(
            f"El valor no puede ser booleano. Se esperaba {tipo.__name__}."
        )
    
    # Intentar conversión
    try:
        numero = tipo(valor)
    except (ValueError, TypeError):
        raise ValidationError(
            f"El valor '{valor}' no es un {tipo.__name__} válido."
        )
    
    # Validar NaN e infinito para float
    if tipo == float:
        if math.isnan(numero):
            raise ValidationError("El valor no puede ser NaN (Not a Number).")
        if math.isinf(numero):
            raise ValidationError("El valor no puede ser infinito.")
    
    # Validar límite inferior
    if numero < min_val:
        raise ValidationError(
            f"El valor debe ser mayor o igual a {min_val}."
        )
    
    # Validar límite superior si existe
    if max_val is not None and numero > max_val:
        raise ValidationError(
            f"El valor debe ser menor o igual a {max_val}."
        )
    
    return numero


def validar_categoria(categoria: str) -> str:
    """
    Valida y normaliza el nombre de una categoría de producto.
    
    Acepta variaciones en mayúsculas, minúsculas y tildes, devolviendo
    la forma canónica de la categoría.
    
    Args:
        categoria: Nombre de la categoría ingresado por el usuario.
    
    Returns:
        La categoría normalizada: "Electronico" o "Libro".
    
    Raises:
        ValidationError: Si la categoría no es reconocida.
    
    Examples:
        >>> validar_categoria("electronico")
        'Electronico'
        >>> validar_categoria("LIBRO")
        'Libro'
        >>> validar_categoria("Electrónico")
        'Electronico'
        >>> validar_categoria("Hardware")
        ValidationError: Categoría inválida...
    """
    # Normalizar espacios y mayúsculas
    categoria_normalizada = categoria.strip().lower()
    
    # Remover tildes (normalización NFD y eliminación de marcas diacríticas)
    categoria_sin_tildes = ''.join(
        c for c in unicodedata.normalize('NFD', categoria_normalizada)
        if unicodedata.category(c) != 'Mn'
    )
    
    # Mapeo de categorías aceptadas
    categorias_validas = {
        'electronico': 'Electronico',
        'electrónico': 'Electronico',
        'libro': 'Libro'
    }
    
    # Buscar coincidencia
    if categoria_sin_tildes in categorias_validas:
        return categorias_validas[categoria_sin_tildes]
    
    # Si la entrada original tenía tilde y coincide
    if categoria_normalizada in categorias_validas:
        return categorias_validas[categoria_normalizada]
    
    # Categoría no reconocida
    raise ValidationError(
        f"Categoría inválida: '{categoria}'. "
        "Las categorías válidas son: Electronico, Libro."
    )
