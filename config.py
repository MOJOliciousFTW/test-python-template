"""
Module docstring. Write something clever.
"""
import json
import logging
import os
from datetime import datetime

import tzlocal
from colorlog import ColoredFormatter


class Formatter(ColoredFormatter):
    """
    Class docstring. Write something clever.
    Maybe something about inputs and outputs.
    """
    def formatTime(self, record, datefmt=None):
        if datefmt:
            return_value = datetime.fromtimestamp(
                record.created,
                tzlocal.get_localzone()
            ).strftime(datefmt)
        else:
            return_value = self.default_msec_format % (
                datetime.fromtimestamp(
                    record.created,
                    tzlocal.get_localzone()
                ).strftime(
                    self.default_time_format
                ),
                record.msecs
            )
        return return_value


_LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logging.getLogger().handlers[0].setFormatter(Formatter(
    fmt='%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s%(reset)s',
    datefmt='%Y-%m-%dT%H:%M:%S%z',
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red',
    }
))


if os.path.exists('./local_config.json'):
    with open('./local_config.json', encoding="utf8") as f:
        config = json.load(f)
else:
    config = {"user": "ci"}


def get_config():
    """ got get`em. """
    _LOGGER.debug('Have some configs.')
    return config
