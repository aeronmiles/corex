import os
from dotenv import load_dotenv
from loguru import logger


load_dotenv()


def _env(name: str) -> str:
    k = os.getenv(name)
    if k:
        return k
    else:
        e = "Environment variable {} is not set".format(name)
        raise Exception(e)


logger.add(
    sink=_env("LOG_FILE_PATH"),
    level=_env("LOG_LEVEL"),
    rotation="10 MB",
    # async
    enqueue=True,
    catch=True,
    # log as json
    serialize=False,
    backtrace=_env("LOG_LEVEL") == "DEBUG",
    diagnose=_env("LOG_LEVEL") == "DEBUG",)