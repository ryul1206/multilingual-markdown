import os
import time
import logging
import click

_SAVE_LOG_FILE = False


def set_log_dir(log_dir: str):
    # Check
    if log_dir is None:
        return
    if not os.path.isdir(log_dir):
        raise click.FileError(log_dir, hint=f"Log directory is not found: {log_dir}")
    # Name
    global _SAVE_LOG_FILE
    _SAVE_LOG_FILE = True
    fname = time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".log"
    fname = os.path.join(log_dir, fname)
    # Config
    logging.basicConfig(level=logging.DEBUG, format="%(message)s", filename=fname)


def log_info(message: str, fg: str = "white"):
    click.secho(message, fg=fg)
    if _SAVE_LOG_FILE:
        logging.info(message)


def log_warn(message: str, fg: str = "yellow"):
    click.secho(message, fg=fg)
    if _SAVE_LOG_FILE:
        logging.warning(message)


def log_error(message: str, fg: str = "red"):
    click.secho(message, fg=fg)
    if _SAVE_LOG_FILE:
        logging.error(message)
