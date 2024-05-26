from .base import Numeric


class Epoch:
    """Interval of time in milliseconds"""
    def __init__(self, begin: int, end: int):
        self.__begin = begin
        self.__end = end

    @property
    def BEGIN(self) -> int:
        return self.__begin
    
    @property
    def END(self) -> int:
        return self.__end


class Period:
    """Interval of time in minutes"""
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
      
    @property
    def pandas_freq(self) -> str:
        """Convert to Pandas time string for resampling"""
        if self._minutes < 1:
            return f'{int(self._minutes * 60)}S'
        elif self._minutes < 60:
            return f'{int(self._minutes)}T'
        elif self._minutes < 1440:
            return f'{int(self._minutes / 60)}H'
        elif self._minutes < 10080:
            return f'{int(self._minutes / 1440)}D'
        elif self._minutes < 43800:
            return f'{int(self._minutes / 10080)}W'
        elif self._minutes < 525600:
            return f'{int(self._minutes / 43800)}M'
        else:
            return f'{int(self._minutes / 525600)}Y'