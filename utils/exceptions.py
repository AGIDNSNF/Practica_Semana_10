"""
Excepciones personalizadas para el Sistema de Gestión de Productos.

Este módulo define las excepciones específicas del dominio utilizadas
para el manejo de errores en validaciones y operaciones del sistema.
"""


class ValidationError(Exception):
    """
    Excepción lanzada cuando los datos de entrada no cumplen las reglas de validación.
    
    Se utiliza para errores de formato, tipo, rango o requisitos de negocio.
    
    Attributes:
        message: Descripción detallada del error de validación.
    """
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class NotFoundError(Exception):
    """
    Excepción lanzada cuando no se encuentra el recurso solicitado.
    
    Se utiliza típicamente cuando se busca un producto por ID inexistente.
    
    Attributes:
        message: Descripción del recurso no encontrado.
    """
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
