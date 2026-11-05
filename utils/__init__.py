"""
Paquete de utilidades para el Sistema de Gestión de Productos.

Contiene excepciones personalizadas y funciones de validación.
"""

from .exceptions import ValidationError, NotFoundError
from .validators import validar_numero, validar_categoria

__all__ = [
    'ValidationError',
    'NotFoundError',
    'validar_numero',
    'validar_categoria'
]
