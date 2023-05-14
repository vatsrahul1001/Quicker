import logging
import sys
import os


def get_logger():
    logger = logging.getLogger(__name__)
    if not len(logger.handlers):
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        if not os.path.exists("logs"):
            os.makedirs("logs")
        file_handler = logging.FileHandler("logs/execution_logfile.log", mode="w")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)
    return logger
