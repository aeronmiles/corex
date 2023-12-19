from corex.types import Numeric
from dataclasses import dataclass


class Epoch:
    def __init__(self, begin: int, end: int):
        self.__begin = begin
        self.__end = end

    @property
    def BEGIN(self) -> int:
        return self.__begin
    
    @property
    def END(self) -> int:
        return self.__end


@dataclass
class Period:
    interval: str
    _minutes: Numeric

    def __init__(self, interval: str, minutes: Numeric):
        self.interval = interval
        self._minutes = minutes

    @property
    def ms(self) -> float:
        return self._minutes * 60000.0

    @property
    def seconds(self) -> float:
        return self._minutes * 60.0

    @property
    def minutes(self) -> float:
        return self._minutes

    @property
    def hours(self) -> float:
        return self._minutes / 60.0

    @property
    def days(self) -> float:
        return self._minutes / (60.0 * 24.0)

    @property
    def weeks(self) -> float:
        return self._minutes / (60.0 * 24.0 * 7.0)

    @property
    def months(self) -> float:
        return self._minutes / (60.0 * 24.0 * 30.5)

    @property
    def years(self) -> float:
        return self._minutes / (60.0 * 24.0 * 365.0)

    def __str__(self) -> str:
        return self.interval

    def __repr__(self) -> str:
        return self.interval