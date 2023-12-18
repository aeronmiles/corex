from core.std.types import Numeric, dataclass, pd


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


class Periods:
    s1 = Period('1s', 1.0 / 60.0)
    m1 = Period('1m', 1.0)
    m3 = Period('3m', 3.0)
    m5 = Period('5m', 5.0)
    m15 = Period('15m', 15.0)
    m30 = Period('30m', 30.0)
    h1 = Period('1h', 60.0)
    h2 = Period('2h', 60.0 * 2)
    h4 = Period('4h', 60.0 * 4)
    h6 = Period('6h', 60.0 * 6)
    h8 = Period('8h', 60.0 * 8)
    h12 = Period('12h', 60.0 * 12)
    d1 = Period('1d', 60.0 * 24)
    d3 = Period('3d', 60.0 * 24 * 3)
    w1 = Period('1w', 60.0 * 24 * 7)
    M1 = Period('1M', (60.0 * 24) * (365 / 12))
    y1 = Period('1y', 60.0 * 24 * 365)

    __periods = {
        '1m': m1,
        '3m': m3,
        '5m': m5,
        '15m': m15,
        '30m': m30,
        '1h': h1,
        '2h': h2,
        '4h': h4,
        '6h': h6,
        '8h': h8,
        '12h': h12,
        '1d': d1,
        '3d': d3,
        '1w': w1,
        '1M': M1,
        '1y': y1
    }

    @staticmethod
    def from_interval(interval: str) -> Period:
        return Periods.__periods[interval]

    @staticmethod
    def posix(series: pd.Series) -> pd.Series:
        """
        Returns: pd.Series of POSIX datetime (seconds)
        Args: series: pd.Series of datetime.datetime

        """
        dt = pd.to_datetime(series.index.values, format="%Y-%m-%d")
        return pd.Series(index=series.index, data=dt.map(pd.Timestamp.timestamp))