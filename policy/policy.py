from abc import ABC, abstractmethod


class Policy(ABC):
    """Policy is an abstract class that defines the interface for all policies."""
    @abstractmethod
    def validate(self, data) -> bool:
        raise NotImplementedError("Policy::validate() is not implemented.")