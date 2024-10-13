import sys

from loguru import logger


def init_logger():
    logger.remove(0)
    logger.add(
        sys.stderr,
        level="INFO"
    )


init_logger()
