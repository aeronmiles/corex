from typing import List
import numpy as np
from corex import logger


class Stats:
    @staticmethod
    def round_to_non_zero(data, decimals=2):
        if data == 0:
            return 0
        else:
            # Find the scale to round to two significant digits
            scale = 10 ** (decimals - int(np.floor(np.log10(abs(data)))) - 1)
            return round(data * scale) / scale

    @staticmethod
    def print(data: List[float], prepend: str = ""):
        min_val = Stats.round_to_non_zero(np.min(data))
        max_val = Stats.round_to_non_zero(np.max(data))
        mean_val = Stats.round_to_non_zero(np.mean(data))
        median_val = Stats.round_to_non_zero(np.median(data))
        stddev_val = Stats.round_to_non_zero(np.std(data))

        logger.info(
            f"{prepend} :: Min: {min_val}, Max: {max_val}, Mean: {mean_val}, Median: {median_val}, StdDev: {stddev_val}"
        )