"""
This module provides a singleton pattern for classes.
"""
from typing import Any, Dict, Optional, Type, TypeVar


T = TypeVar('T')


class Singletons:
    """
    A class for managing singletons.
    """
    _instances: Dict[str, Any] = {}

    @classmethod
    def get(cls, instance_class: Type[T], kwargs: Optional[Dict]=None, namespace: str="") -> T:
        """
        Get an instance of a given class associated with a specific namespace.

        :param instance_class: The class of the instance to be retrieved.
        :param namespace: A unique identifier for the instance.
        :return: The instance.
        """
        if kwargs is None:
            kwargs = {}
        
        key = f"{namespace}{instance_class.__name__}{tuple(sorted(kwargs.items()))}"
        
        if key not in cls._instances:
            cls._instances[key] = instance_class(**kwargs)
            
        return cls._instances[key]