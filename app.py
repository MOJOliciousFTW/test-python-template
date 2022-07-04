"""
Module docstring. Write something clever.
"""
import logging
import json
from src.examplepackage.example_module import Aclass
from config import get_config


_CONFIG = get_config()
_LOGGER = logging.getLogger(__name__)
_LOGGER.debug(" _CONFIG: %s", json.dumps(_CONFIG))
_LOGGER.debug('Starting soonish')


if __name__ == '__main__':
    _LOGGER.debug('Starting')
    aclass = Aclass(first_variable=2)
    _LOGGER.info('Ending')
