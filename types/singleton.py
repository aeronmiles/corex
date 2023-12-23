"""
This module provides a singleton pattern for classes.
"""
from abc import ABC
from typing import Any, Dict, TypeVar, Type


T = TypeVar('T', bound='Singleton')


class Singleton(ABC):
    """
    This class provides a singleton pattern for classes.
    """
    _instance: Dict[str, Any] = {}

    def __new__(cls: Type[T], namespace: str) -> T:
        cls._default_instance = namespace
        if namespace not in cls._instance:
            cls._instance[namespace] = super(cls, cls).__new__(cls, namespace)

        return cls._instance[namespace]

    @classmethod
    def I(cls: Type[T], namespace: str) -> T:
        if not namespace:
            if not cls._default_instance:
                raise ValueError('No instance initialized.')
            
            namespace = cls._default_instance
            
        return cls._instance[namespace]