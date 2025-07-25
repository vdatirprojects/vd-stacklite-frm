import logging
import coloredlogs


def get_logger(name: str = __name__) -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    coloredlogs.install(
        level="DEBUG",
        fmt="[%(asctime)s.%(msecs)03d] [%(hostname)s] [%(name)s] [%(process)d] [%(levelname)s] : %(message)s",
    )

    return logger
