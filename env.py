import os
from pathlib import Path
from typing import Any, List, TypeVar, get_type_hints
from dotenv import load_dotenv
from .logging import logger
from .types.base import ImmutableAttr


load_dotenv()


T = TypeVar("T")


def env_var(name: str, default: Any=None) -> Any:
    k = os.getenv(name)
    if k:
        return k
    else:
        logger.error(f"Environment variable: {name} is not set, returning default value: {default}")
        return default


class EnvVars(ImmutableAttr):
    def __init__(self):
        for attr, attr_type in get_type_hints(self.__class__).items():
            if isinstance(attr_type, type) and issubclass(attr_type, EnvVars):
                nested_env_var_instance = attr_type()
                object.__setattr__(self, attr, nested_env_var_instance)
            else:
                env_value = os.getenv(attr)
                if env_value is not None:
                    object.__setattr__(self, attr, self._convert_type(env_value, attr_type))

    def _convert_type(self, value: str, target_type: Any) -> Any:
        """Converts the string value to the specified target type."""
        if target_type is bool:
            return value.lower() in ['true', '1', 'yes']
        elif target_type is int:
            return int(value)
        elif target_type is float:
            return float(value)
        elif target_type is List[str]:
            return value.split(',')
        elif target_type is Path:
            return Path(value)
        else:
            return value