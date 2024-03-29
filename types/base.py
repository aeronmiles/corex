from decimal import Decimal
from typing import (Dict, List, Tuple, Callable, NamedTuple, Optional, TypeVar, Union, Any, Awaitable, Iterable, Coroutine)
from abc import (ABC, abstractmethod)
from dataclasses import dataclass
from enum import Enum


Numeric = Union[int, float]


class ImmutableAttr(ABC):
    """Base class for immutable objects."""
    def __setattr__(self, key, value):
        raise AttributeError("Cannot modify immutable attr")

