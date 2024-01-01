import os
import atexit as _atexit
import sys as _sys
from typing import Any, Optional
from dotenv import load_dotenv
from loguru._logger import Logger, Core
from loguru import _defaults


load_dotenv()


def _env(name: str, default: Optional[Any] = None) -> Optional[Any]:
    k = os.getenv(name)
    if k:
        return k
    else:
        e = f"Environment variable {name} is not set"
        raise KeyError(e)


class _CorexLogger(Logger):
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
            backtrace=_env("LOG_LEVEL") == "DEBUG",
            diagnose=_env("LOG_LEVEL") == "DEBUG",
            )
        
        if _defaults.LOGURU_AUTOINIT and _sys.stderr:
            self.add(_sys.stderr)
            
        _atexit.register(self.remove)


logger = _CorexLogger()

