from abc import ABC, abstractmethod
import os
from typing import Any, List, Tuple
from dotenv import load_dotenv
from .logging import logger


load_dotenv()


def env_var(name: str, default: Any=None) -> Any:
    k = os.getenv(name)
    if k:
        return k
    else:
        logger.error(f"Environment variable: {name} is not set, returning default value: {default}")
        return default


class EnvValidator(ABC):
    def __init__(self):
        required_vars = self._required_env_vars()
        for var_name, var_type in required_vars:
            value = os.getenv(var_name)
            if value is None:
                raise ValueError(f"Environment variable {var_name} is not set")
            try:
                # Convert to the specified type
                var_type(value)
            except ValueError:
                raise ValueError(f"Environment variable {var_name} cannot be converted to {var_type}")

    @abstractmethod
    def _required_env_vars(self) -> List[Tuple[str, type]]:
        """
        Returns a list of tuples with required environment variables and their expected types.
        """
        raise NotImplementedError("All subclasses must implement the _required_env_vars method")