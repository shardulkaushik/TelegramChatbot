"""
$File: config_reader.py
$Comment: config_reader reads the configuration
"""
import configparser
import os
import logger
from logger.log import log


def get_parser():
    parser = configparser.ConfigParser()
    parser.read(os.path.join(os.getcwd(), 'utilities', 'bot_config.ini'))
    return parser


def get_attribute_str(section, attribute, default=""):
    parser = get_parser()
    try:
        value = parser.get(section, attribute)
    except Exception as e:
        log.exception(e)
        return default
    else:
        return value


def get_attribute_bool(section, attribute, default=True):
    parser = get_parser()
    try:
        value = parser.getboolean(section, attribute)
    except Exception as e:
        log.exception(e)
        return default
    else:
        return value
