from functools import reduce
import json
import time
from typing import Callable


def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)


def apply(x, func: Callable):
    func(x)
    return x


def convert_list_to_json_array(symbols):
    if symbols is None:
        return symbols
    res = json.dumps(symbols)
    return res.replace(" ", "")


def get_timestamp():
    return int(time.time() * 1000)
