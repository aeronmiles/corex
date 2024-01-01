from functools import reduce as _reduce
import json
import os
import time
from typing import Callable


def check_path(path: str) -> str:
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def compose(*functions):
    return _reduce(lambda f, g: lambda x: f(g(x)), functions)


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
