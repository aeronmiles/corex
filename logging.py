import os
import atexit as _atexit
import sys as _sys
from typing import Any
from dotenv import load_dotenv
from loguru._logger import Logger, Core
from loguru import _defaults
from .manager import Singletons


load_dotenv()


def _env(name: str, default: Any = None) -> str:
    k = os.getenv(name)
    if k:
        return k
    else:
        e = "Environment variable {} is not set".format(name)
        raise Exception(e)


class _Logger(Logger):
    def __init__(self):
        super().__init__( 
            core=Core(),
            exception=None,
            depth=0,
            record=False,
            lazy=False,
            colors=False,
            raw=False,
            capture=True,
            patchers=[],
            extra={},
        )
        self.add(
            sink=_env("LOG_FILE_PATH"),
            level=_env("LOG_LEVEL"),
            rotation="10 MB",
            # async
            enqueue=True,
            catch=True,
            # log as json
            serialize=False,
            backtrace="DEBUG" in _env("LOG_LEVEL"),
            diagnose="DEBUG" in _env("LOG_LEVEL"),
            )
        
        if _defaults.LOGURU_AUTOINIT and _sys.stderr:
            self.add(_sys.stderr)
            
        self.__exit_on_error = _env("EXIT_ON_ERROR")
        _atexit.register(self.remove)
        
    def error(self, __message, *args, **kwargs):
        super().error(__message, *args, **kwargs)
        if self.__exit_on_error:
            exit(1)


logger = Singletons.get(_Logger, {}, "corex")

