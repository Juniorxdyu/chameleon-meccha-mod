"""Project-wide logger for chameleon-meccha-mod."""
import logging
import sys
from colorama import Fore, Style, init

init(autoreset=True)


class _ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, "")
        record.msg = f"{color}{record.msg}{Style.RESET_ALL}"
        return super().format(record)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(f"chameleon.{name}")
    if logger.handlers:
        return logger
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(_ColorFormatter("[%(asctime)s] %(name)s :: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger