"""
This module provides a singleton pattern for classes.
"""
from typing import Any, Dict, Type, TypeVar
from abc import ABC, abstractmethod


T = TypeVar('T')


class Singleton(ABC):
    _instances: Dict[str, Any] = {}

    def __new__(cls) -> Any:
        key = cls.__name__
        
        if key not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[key] = instance
            instance._initialized = False
            instance._init_once()
            
        return cls._instances[key]

    def _init_once(self):
        """
        Custom initialization method that subclasses should override.
        This method will be called only once per class.
        """
        if self._initialized:
            return
        self._initialize()
        self._initialized = True

    @abstractmethod
    def _initialize(self):
        """
        Actual initialization code for the subclass. 
        Subclasses should override this method.
        """
        raise NotImplementedError("All subclasses must implement the _initialize method")
    

class Singletons:
    """
    A class for managing singletons.
    """
    _instances: Dict[str, Any] = {}

    @classmethod
    def get(cls, instance_class: Type[T]) -> T:
        """
        Get a singleton instance of a given classs.

        :param instance_class: The class type of the instance to be retrieved.
        :return: The instance.
        """
        key = instance_class.__name__
        
        if key not in cls._instances:
            cls._instances[key] = instance_class()
            
        return cls._instances[key]